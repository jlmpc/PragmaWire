#!/usr/bin/env python3
from __future__ import annotations

import argparse
import base64
import json
import os
import re
import sys
import unicodedata
import urllib.error
import urllib.parse
import urllib.request
from datetime import datetime
from html.parser import HTMLParser
from pathlib import Path
from typing import Any

CATEGORY_IDS = {
    "hogar inteligente": 16,
    "inteligencia artificial": 13,
    "productividad digital": 15,
    "recomendaciones tecnologicas": 5,
    "salud y bienestar": 18,
    "salud y bienestar digital": 18,
    "seguridad digital": 14,
}

REQUIRED_FIELDS = [
    "TITULO",
    "SLUG",
    "META_TITLE",
    "META_DESCRIPTION",
    "CATEGORY",
    "TAGS",
    "STATUS",
]

class PublishError(RuntimeError):
    pass


class _HTMLTextExtractor(HTMLParser):
    def __init__(self) -> None:
        super().__init__()
        self.parts: list[str] = []

    def handle_data(self, data: str) -> None:
        self.parts.append(data)

    def text(self) -> str:
        return "".join(self.parts)


def now_iso() -> str:
    return datetime.now().replace(microsecond=0).isoformat()


def normalize_label(value: str) -> str:
    value = unicodedata.normalize("NFD", value.strip().lower())
    value = "".join(ch for ch in value if unicodedata.category(ch) != "Mn")
    return re.sub(r"\s+", " ", value)


def normalize_text(value: str) -> str:
    return re.sub(r"\s+", " ", value).strip()


def html_to_text(value: str) -> str:
    parser = _HTMLTextExtractor()
    parser.feed(value or "")
    return normalize_text(parser.text())


def read_json(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def write_json(path: Path, data: Any) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(data, ensure_ascii=False, indent=2), encoding="utf-8")


def active_run_path(root: Path, run_path_arg: str | None) -> Path:
    if run_path_arg:
        return Path(run_path_arg).expanduser().resolve()

    current = root / "outputs" / "current-run.json"
    if not current.exists():
        raise PublishError("No existe outputs/current-run.json. Usa --run-path o inicializa un run.")

    data = read_json(current)
    return Path(data["active_run_path"]).expanduser().resolve()


def extract_section(text: str, heading: str) -> str:
    pattern = rf"^##\s+{re.escape(heading)}\s*$\n([\s\S]*?)(?=^##\s+|\Z)"
    match = re.search(pattern, text, flags=re.MULTILINE)
    return match.group(1).strip() if match else ""


def extract_section_until(text: str, heading: str, stop_headings: list[str]) -> str:
    stops = "|".join(re.escape(stop) for stop in stop_headings)
    pattern = rf"^##\s+{re.escape(heading)}\s*$\n([\s\S]*?)(?=^##\s+(?:{stops})\s*$|\Z)"
    match = re.search(pattern, text, flags=re.MULTILINE)
    return match.group(1).strip() if match else ""


def extract_wordpress_block(text: str) -> str:
    match = re.search(
        r"^##\s+WORDPRESS_DRAFT_VALIDADO\s*$\n([\s\S]*?)(?=^---\s*$\n\s*^##\s+NOTAS_PARA_REVISION_HUMANA|^##\s+NOTAS_PARA_REVISION_HUMANA|\Z)",
        text,
        flags=re.MULTILINE,
    )
    if match:
        return match.group(1).strip()

    match = re.search(r"WORDPRESS_DRAFT_VALIDADO:\s*\n([\s\S]*?)(?=^NOTAS_PARA_REVISION_HUMANA:|\Z)", text, flags=re.MULTILINE)
    return match.group(1).strip() if match else ""


def parse_line_fields(block: str) -> dict[str, str]:
    data: dict[str, str] = {}
    for line in block.splitlines():
        match = re.match(r"^([A-Z_]+):\s*(.*)$", line.strip())
        if match:
            data[match.group(1)] = match.group(2).strip()
    return data


def parse_optional_media_id(fields: dict[str, str]) -> int | None:
    for key in ("FEATURED_MEDIA_ID", "FEATURED_IMAGE_ID", "FEATURED_MEDIA"):
        raw = fields.get(key, "").strip()
        if not raw:
            continue
        if not raw.isdigit():
            raise PublishError(f"{key} debe ser un ID numérico si se informa: {raw!r}")
        media_id = int(raw)
        if media_id <= 0:
            raise PublishError(f"{key} debe ser mayor que 0")
        return media_id
    return None


def parse_faq(block: str) -> list[dict[str, str]]:
    faq_block = re.search(r"FAQ_SCHEMA_CANDIDATES:\s*\n([\s\S]*)", block)
    if not faq_block:
        return []

    items: list[dict[str, str]] = []
    current: dict[str, str] = {}
    for line in faq_block.group(1).splitlines():
        q = re.match(r"^\s*(?:-\s*)?Q:\s*(.+)$", line)
        a = re.match(r"^\s*A:\s*(.+)$", line)
        if q:
            if current:
                items.append(current)
            current = {"question": q.group(1).strip(), "answer": ""}
        elif a and current:
            current["answer"] = a.group(1).strip()
    if current:
        items.append(current)
    return [item for item in items if item.get("question") and item.get("answer")]


def article_id_from_path(path: Path) -> str:
    match = re.search(r"articulo_(\d+)_wordpress_ready\.md$", path.name)
    if not match:
        raise PublishError(f"No puedo extraer article_id de {path}")
    return match.group(1)


def extract_body(run_path: Path, article_id: str, ready_text: str) -> str:
    article_markdown = extract_section_until(
        ready_text,
        "ARTICLE_MARKDOWN",
        ["FAQ_SCHEMA_CANDIDATES", "NOTAS_PARA_SUPERVISOR_FINAL", "NOTAS_PARA_REVISION_HUMANA"],
    )
    if article_markdown:
        return article_markdown

    edited_path = run_path / "04-edited" / f"articulo_{article_id}_edited.md"
    if not edited_path.exists():
        raise PublishError(f"Falta cuerpo del artículo: {edited_path}")

    edited_text = edited_path.read_text(encoding="utf-8")
    final_markdown = extract_section_until(edited_text, "ARTICULO_FINAL_MARKDOWN", ["NOTAS_EDITOR_FINAL"])
    return final_markdown or edited_text.strip()


def split_csv(value: str) -> list[str]:
    return [item.strip() for item in value.split(",") if item.strip()]


def category_id(name: str) -> int:
    key = normalize_label(name)
    if key not in CATEGORY_IDS:
        raise PublishError(f"Categoría no mapeada: {name}")
    return CATEGORY_IDS[key]


def excerpt_from_metadata(fields: dict[str, str]) -> str:
    return fields["META_DESCRIPTION"].strip()


def parse_article(path: Path, run_path: Path) -> dict[str, Any]:
    article_id = article_id_from_path(path)
    text = path.read_text(encoding="utf-8")
    block = extract_wordpress_block(text)
    if not block:
        raise PublishError(f"Falta WORDPRESS_DRAFT_VALIDADO en {path}")

    fields = parse_line_fields(block)
    missing = [field for field in REQUIRED_FIELDS if not fields.get(field)]
    if missing:
        raise PublishError(f"{path.name} no tiene metadata obligatoria: {', '.join(missing)}")
    if normalize_label(fields["STATUS"]) != "draft":
        raise PublishError(f"{path.name} tiene STATUS={fields['STATUS']!r}; solo se permite draft")

    tags = split_csv(fields["TAGS"])
    if not tags:
        raise PublishError(f"{path.name} no tiene etiquetas válidas")

    body = extract_body(run_path, article_id, text)
    if not body:
        raise PublishError(f"{path.name} no tiene cuerpo de artículo")

    return {
        "article_id": f"articulo_{article_id}",
        "source_file": str(path.relative_to(run_path)),
        "body_source": f"04-edited/articulo_{article_id}_edited.md",
        "fields": fields,
        "faq_schema_candidates": parse_faq(block),
        "tag_names": tags,
        "category_id": category_id(fields["CATEGORY"]),
        "content": body,
        "featured_media_id": parse_optional_media_id(fields),
        "manual_featured_image": {
            "description": fields.get("FEATURED_IMAGE_DESCRIPTION", ""),
            "alt": fields.get("FEATURED_IMAGE_ALT", ""),
        },
    }


def auth_headers() -> tuple[str, dict[str, str]]:
    wp_url = os.environ.get("WP_URL") or os.environ.get("WP_API_URL")
    wp_user = os.environ.get("WP_USER") or os.environ.get("WP_API_USERNAME")
    wp_password = os.environ.get("WP_APP_PASSWORD") or os.environ.get("WP_API_PASSWORD")

    if not wp_url or not wp_user or not wp_password:
        raise PublishError(
            "Faltan credenciales. Define WP_URL/WP_USER/WP_APP_PASSWORD "
            "o WP_API_URL/WP_API_USERNAME/WP_API_PASSWORD."
        )

    auth = base64.b64encode(f"{wp_user}:{wp_password}".encode()).decode()
    return wp_url.rstrip("/"), {
        "Authorization": f"Basic {auth}",
        "Content-Type": "application/json",
        "User-Agent": "PragmaWire-Draft-Publisher/1.0",
    }


def wp_request(base_url: str, headers: dict[str, str], method: str, path: str, payload: Any | None = None) -> Any:
    data = None
    if payload is not None:
        data = json.dumps(payload, ensure_ascii=False).encode("utf-8")

    req = urllib.request.Request(f"{base_url}{path}", data=data, headers=headers, method=method)
    try:
        with urllib.request.urlopen(req, timeout=45) as resp:
            body = resp.read().decode("utf-8")
            return json.loads(body) if body else {}
    except urllib.error.HTTPError as exc:
        body = exc.read().decode("utf-8", errors="replace")
        raise PublishError(f"HTTP {exc.code} {path}: {body[:500]}") from exc
    except urllib.error.URLError as exc:
        raise PublishError(f"Error de conexión {path}: {exc}") from exc


def find_existing_post(base_url: str, headers: dict[str, str], slug: str) -> dict[str, Any] | None:
    query = urllib.parse.urlencode(
        {
            "slug": slug,
            "status[]": ["draft", "pending", "private", "publish", "future"],
            "context": "edit",
        },
        doseq=True,
    )
    posts = wp_request(base_url, headers, "GET", f"/wp-json/wp/v2/posts?{query}")
    return posts[0] if isinstance(posts, list) and posts else None


def find_or_create_tag(base_url: str, headers: dict[str, str], name: str) -> int:
    query = urllib.parse.urlencode({"search": name, "per_page": 100})
    tags = wp_request(base_url, headers, "GET", f"/wp-json/wp/v2/tags?{query}")
    for tag in tags:
        if normalize_label(tag.get("name", "")) == normalize_label(name):
            return int(tag["id"])

    try:
        created = wp_request(base_url, headers, "POST", "/wp-json/wp/v2/tags", {"name": name})
    except PublishError as exc:
        if "term_exists" not in str(exc):
            raise
        tags = wp_request(base_url, headers, "GET", f"/wp-json/wp/v2/tags?{query}")
        for tag in tags:
            if normalize_label(tag.get("name", "")) == normalize_label(name):
                return int(tag["id"])
        raise
    return int(created["id"])


def build_payload(article: dict[str, Any], tag_ids: list[int] | None = None) -> dict[str, Any]:
    fields = article["fields"]
    meta = {
        "jetpack_seo_html_title": fields["META_TITLE"],
        "advanced_seo_description": fields["META_DESCRIPTION"],
        "jetpack_seo_noindex": False,
        "jetpack_publicize_feature_enabled": False,
    }

    payload = {
        "title": fields["TITULO"],
        "content": article["content"],
        "excerpt": excerpt_from_metadata(fields),
        "slug": fields["SLUG"],
        "status": "draft",
        "categories": [article["category_id"]],
        "tags": tag_ids or [],
        "meta": meta,
    }
    if article.get("featured_media_id"):
        payload["featured_media"] = article["featured_media_id"]
    return payload


def fetch_post(base_url: str, headers: dict[str, str], post_id: int) -> dict[str, Any]:
    return wp_request(base_url, headers, "GET", f"/wp-json/wp/v2/posts/{post_id}?context=edit")


def excerpt_value(post: dict[str, Any]) -> str:
    excerpt = post.get("excerpt") or {}
    raw = excerpt.get("raw")
    if isinstance(raw, str) and raw.strip():
        return normalize_text(raw)
    rendered = excerpt.get("rendered")
    if isinstance(rendered, str):
        return html_to_text(rendered)
    return ""


def confirm_post(post: dict[str, Any], article: dict[str, Any], expected_tag_ids: list[int]) -> dict[str, Any]:
    fields = article["fields"]
    meta = post.get("meta") or {}
    expected_excerpt = normalize_text(excerpt_from_metadata(fields))
    checks = {
        "slug": post.get("slug") == fields["SLUG"],
        "excerpt": excerpt_value(post) == expected_excerpt,
        "categories": article["category_id"] in (post.get("categories") or []),
        "tags": set(expected_tag_ids).issubset(set(post.get("tags") or [])),
        "seo_title": meta.get("jetpack_seo_html_title") == fields["META_TITLE"],
        "seo_description": meta.get("advanced_seo_description") == fields["META_DESCRIPTION"],
        "seo_noindex": meta.get("jetpack_seo_noindex") is False,
    }
    if article.get("featured_media_id"):
        checks["featured_media"] = post.get("featured_media") == article["featured_media_id"]

    confirmed = {
        "slug": post.get("slug"),
        "excerpt": excerpt_value(post),
        "categories": post.get("categories") or [],
        "tags": post.get("tags") or [],
        "meta": {
            "jetpack_seo_html_title": meta.get("jetpack_seo_html_title"),
            "advanced_seo_description": meta.get("advanced_seo_description"),
            "jetpack_seo_noindex": meta.get("jetpack_seo_noindex"),
        },
    }
    if article.get("featured_media_id"):
        confirmed["featured_media"] = post.get("featured_media")

    return {"checks": checks, "confirmed": confirmed, "ok": all(checks.values())}


def update_manifest(run_path: Path, log: dict[str, Any]) -> None:
    manifest_path = run_path / "run-manifest.json"
    if not manifest_path.exists():
        return

    manifest = read_json(manifest_path)
    manifest["updated_at"] = now_iso()
    manifest["wordpress_creation"] = {
        "status": "complete" if log["error_count"] == 0 else "failed",
        "created_at": log["fecha"],
        "success_count": log["success_count"],
        "error_count": log["error_count"],
        "log_path": "06-wordpress-creation-log.json",
        "payload_preview_path": "wordpress-payload-preview.json",
    }
    write_json(manifest_path, manifest)


def load_articles(run_path: Path) -> list[dict[str, Any]]:
    ready_dir = run_path / "05-wordpress-ready"
    if not (ready_dir / "_STAGE_COMPLETE").exists():
        raise PublishError("Falta 05-wordpress-ready/_STAGE_COMPLETE")

    paths = sorted(ready_dir.glob("articulo_*_wordpress_ready.md"))
    if not paths:
        raise PublishError("No hay artículos en 05-wordpress-ready")

    return [parse_article(path, run_path) for path in paths]


def make_preview(articles: list[dict[str, Any]]) -> dict[str, Any]:
    return {
        "generated_at": now_iso(),
        "publish": False,
        "total": len(articles),
        "articles": [
            {
                "article_id": article["article_id"],
                "source_file": article["source_file"],
                "slug": article["fields"]["SLUG"],
                "title": article["fields"]["TITULO"],
                "category_id": article["category_id"],
                "category": article["fields"]["CATEGORY"],
                "tag_names": article["tag_names"],
                "excerpt": excerpt_from_metadata(article["fields"]),
                "payload_template": build_payload(article),
                "tag_resolution": "resolved_or_created_at_publish_time",
                "manual_featured_image": article["manual_featured_image"],
                "featured_media_id": article.get("featured_media_id"),
                "faq_schema_candidates_count": len(article["faq_schema_candidates"]),
                "content_chars": len(article["content"]),
            }
            for article in articles
        ],
    }


def publish_articles(run_path: Path, articles: list[dict[str, Any]], update_existing: bool) -> dict[str, Any]:
    base_url, headers = auth_headers()
    results: list[dict[str, Any]] = []

    for article in articles:
        fields = article["fields"]
        entry: dict[str, Any] = {
            "article_id": article["article_id"],
            "slug": fields["SLUG"],
            "title": fields["TITULO"],
            "category_id": article["category_id"],
            "tag_names": article["tag_names"],
            "success": False,
            "manual_featured_image": article["manual_featured_image"],
            "warnings": [],
        }
        try:
            existing = find_existing_post(base_url, headers, fields["SLUG"])
            if existing and not update_existing:
                raise PublishError(f"Ya existe una entrada con slug {fields['SLUG']} (ID {existing.get('id')})")

            tag_ids = [find_or_create_tag(base_url, headers, name) for name in article["tag_names"]]
            payload = build_payload(article, tag_ids)
            if not article.get("featured_media_id") and (
                article["manual_featured_image"].get("description") or article["manual_featured_image"].get("alt")
            ):
                entry["warnings"].append("Imagen destacada descrita pero sin media ID; queda pendiente de revisión humana.")

            if existing:
                post = wp_request(base_url, headers, "POST", f"/wp-json/wp/v2/posts/{existing['id']}?context=edit", payload)
                entry["action"] = "updated"
            else:
                post = wp_request(base_url, headers, "POST", "/wp-json/wp/v2/posts?context=edit", payload)
                entry["action"] = "created"

            post_id = int(post["id"])
            confirmed_post = fetch_post(base_url, headers, post_id)
            verification = confirm_post(confirmed_post, article, tag_ids)
            if not verification["ok"]:
                raise PublishError(f"Verificación fallida: {verification['checks']}")

            entry.update(
                {
                    "success": True,
                    "wp_post_id": confirmed_post.get("id"),
                    "wp_post_link": confirmed_post.get("link"),
                    "wp_status": confirmed_post.get("status"),
                    "sent": {
                        "slug": payload["slug"],
                        "excerpt": payload["excerpt"],
                        "categories": payload["categories"],
                        "tags": tag_ids,
                        "meta": payload["meta"],
                        **({"featured_media": payload["featured_media"]} if "featured_media" in payload else {}),
                    },
                    "confirmed": verification["confirmed"],
                    "tag_ids": tag_ids,
                    "verified": verification["checks"],
                }
            )
            print(f"OK {article['article_id']} -> WP ID {entry['wp_post_id']} ({fields['SLUG']})")
        except PublishError as exc:
            entry["error"] = str(exc)
            print(f"ERR {article['article_id']} -> {exc}")
        results.append(entry)

    log = {
        "run_id": run_path.name,
        "fecha": now_iso(),
        "total": len(results),
        "success_count": sum(1 for result in results if result["success"]),
        "error_count": sum(1 for result in results if not result["success"]),
        "publish": False,
        "results": results,
    }
    write_json(run_path / "06-wordpress-creation-log.json", log)
    update_manifest(run_path, log)
    return log


def main() -> None:
    parser = argparse.ArgumentParser(description="Crea borradores WordPress con metadata completa para PragmaWire.")
    parser.add_argument("--run-path", help="Ruta al run. Por defecto usa outputs/current-run.json.")
    parser.add_argument("--dry-run", action="store_true", help="Solo valida y genera wordpress-payload-preview.json.")
    parser.add_argument("--update-existing", action="store_true", help="Actualiza un borrador existente con el mismo slug en vez de bloquear.")
    args = parser.parse_args()

    root = Path.cwd()
    try:
        run_path = active_run_path(root, args.run_path)
        articles = load_articles(run_path)
        preview = make_preview(articles)
        write_json(run_path / "wordpress-payload-preview.json", preview)
        print(f"Preview generado: {run_path / 'wordpress-payload-preview.json'}")

        if args.dry_run:
            print(f"Dry-run OK: {len(articles)} artículos validados.")
            return

        log = publish_articles(run_path, articles, args.update_existing)
        if log["error_count"]:
            raise PublishError(f"{log['error_count']} artículos fallaron. Revisa 06-wordpress-creation-log.json")
    except PublishError as exc:
        print(f"FAIL: {exc}", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()

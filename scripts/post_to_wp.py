#!/usr/bin/env python3
"""
Crea borradores en WordPress desde los outputs del pipeline PragmaWire.

El script respeta el contrato completo de WORDPRESS_DRAFT/WORDPRESS_DRAFT_VALIDADO:
slug, extracto, categoría, etiquetas y metadata SEO Jetpack. Nunca publica.

Uso:
    python3 scripts/post_to_wp.py --dry-run
    export WP_URL=https://pragmawire.com
    export WP_USER=usuario
    export WP_APP_PASSWORD="xxxx xxxx xxxx xxxx"
    python3 scripts/post_to_wp.py
"""

from __future__ import annotations

import argparse
import base64
import html
import json
import os
import re
import sys
import unicodedata
import urllib.error
import urllib.parse
import urllib.request
from datetime import datetime
from pathlib import Path
from typing import Any

try:
    import markdown
except ImportError:
    markdown = None


CATEGORY_IDS = {
    "hogar inteligente": 16,
    "inteligencia artificial": 13,
    "productividad digital": 15,
    "recomendaciones tecnologicas": 5,
    "salud y bienestar digital": 18,
    "salud y bienestar": 18,
    "seguridad digital": 14,
}

REQUIRED_FIELDS = [
    "title",
    "slug",
    "excerpt",
    "category_primary",
    "tags",
    "meta_title",
    "meta_description",
]


class PublishError(RuntimeError):
    pass


def now_iso() -> str:
    return datetime.now().replace(microsecond=0).isoformat()


def normalize_label(value: str) -> str:
    value = unicodedata.normalize("NFD", value.strip().lower())
    value = "".join(ch for ch in value if unicodedata.category(ch) != "Mn")
    return re.sub(r"\s+", " ", value)


def read_json(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def write_json(path: Path, data: Any) -> None:
    path.write_text(json.dumps(data, ensure_ascii=False, indent=2), encoding="utf-8")


def active_run_path(root: Path, run_path_arg: str | None) -> Path:
    if run_path_arg:
        return Path(run_path_arg).expanduser().resolve()

    current_run_file = root / "outputs" / "current-run.json"
    if not current_run_file.exists():
        raise PublishError("outputs/current-run.json no encontrado. Ejecuta init_run.py primero.")

    current_run = read_json(current_run_file)
    return Path(current_run["active_run_path"]).expanduser().resolve()


def extract_block(text: str, names: list[str]) -> str:
    for name in names:
        pattern = rf"^{re.escape(name)}:\s*\n([\s\S]*?)(?=^NOTAS_PARA_REVISION_HUMANA:|^ESTADO_SUPERVISION_FINAL:|^NO_CREAR_WORDPRESS_DRAFT:|\Z)"
        match = re.search(pattern, text, flags=re.MULTILINE)
        if match:
            return match.group(1).strip()
    return text.strip()


def split_top_level_sections(text: str) -> tuple[str, str]:
    marker = "ARTICLE_MARKDOWN:"
    if marker not in text:
        return text, text

    metadata, article = text.split(marker, 1)
    for end_marker in [
        "\nFAQ_SCHEMA_CANDIDATES:",
        "\nFINAL_CHECKLIST:",
        "\nNOTAS_PARA_SUPERVISOR_FINAL:",
        "\nNOTAS_PARA_REVISION_HUMANA:",
    ]:
        if end_marker in article:
            article = article.split(end_marker, 1)[0]
    return metadata.strip(), article.strip()


def parse_scalar_metadata(metadata_text: str) -> dict[str, str]:
    fields: dict[str, str] = {}
    current_key: str | None = None
    current_lines: list[str] = []

    def flush() -> None:
        nonlocal current_key, current_lines
        if current_key:
            fields[current_key] = "\n".join(current_lines).strip()
        current_key = None
        current_lines = []

    for raw_line in metadata_text.splitlines():
        line = raw_line.rstrip()
        match = re.match(r"^([A-Za-zÁÉÍÓÚÜÑáéíóúüñ_ ]+):\s*(.*)$", line)
        if match and not line.startswith((" ", "\t", "- ")):
            flush()
            current_key = normalize_key(match.group(1))
            current_lines = [match.group(2).strip()] if match.group(2).strip() else []
        elif current_key:
            current_lines.append(line)
    flush()
    return fields


def normalize_key(key: str) -> str:
    key = normalize_label(key).replace(" ", "_")
    aliases = {
        "titulo": "title",
        "titulo_wordpress": "title",
        "title": "title",
        "slug": "slug",
        "extracto": "excerpt",
        "excerpt": "excerpt",
        "descripcion": "excerpt",
        "meta_description": "meta_description",
        "meta_descripcion": "meta_description",
        "meta_title": "meta_title",
        "categoria": "category_primary",
        "category": "category_primary",
        "category_primary": "category_primary",
        "tags": "tags",
        "tags_wp": "tags",
        "etiquetas": "tags",
        "focus_keyword": "focus_keyword",
        "secondary_keywords": "secondary_keywords",
        "search_intent": "search_intent",
        "content_type": "content_type",
        "ai_summary": "ai_summary",
        "quotable_sentence": "quotable_sentence",
        "main_entities": "main_entities",
        "internal_links_suggested": "internal_links_suggested",
        "update_level": "update_level",
        "obsolescence_risk": "obsolescence_risk",
    }
    return aliases.get(key, key)


def clean_multiline_value(value: str) -> str:
    lines = [line.strip() for line in value.splitlines()]
    lines = [re.sub(r"^-+\s*", "", line).strip() for line in lines if line.strip()]
    return ", ".join(lines)


def parse_tags(value: str) -> list[str]:
    cleaned = clean_multiline_value(value)
    return [tag.strip() for tag in re.split(r"[,;]", cleaned) if tag.strip()]


def parse_featured_image_note(metadata_text: str) -> str:
    if "suggested_featured_image:" not in metadata_text:
        return ""
    note = metadata_text.split("suggested_featured_image:", 1)[1].strip()
    if not note:
        return ""
    return f"\n\n---\n**Imagen destacada sugerida:**\n\n```text\n{note}\n```"


def parse_article(article_path: Path) -> dict[str, Any]:
    content = article_path.read_text(encoding="utf-8")
    block = extract_block(content, ["WORDPRESS_DRAFT_VALIDADO", "WORDPRESS_DRAFT"])
    metadata_text, article_markdown = split_top_level_sections(block)
    fields = parse_scalar_metadata(metadata_text)

    missing = [field for field in REQUIRED_FIELDS if not fields.get(field)]
    if missing:
        raise PublishError(f"{article_path.name}: faltan campos obligatorios: {', '.join(missing)}")

    tags = parse_tags(fields["tags"])
    if not tags:
        raise PublishError(f"{article_path.name}: no hay etiquetas válidas")

    if not article_markdown.strip():
        raise PublishError(f"{article_path.name}: falta ARTICLE_MARKDOWN")

    featured_note = parse_featured_image_note(metadata_text)
    if featured_note and "Imagen destacada sugerida" not in article_markdown:
        article_markdown = article_markdown.rstrip() + featured_note

    return {
        "file": article_path.name,
        "title": clean_multiline_value(fields["title"]),
        "slug": clean_multiline_value(fields["slug"]),
        "excerpt": clean_multiline_value(fields["excerpt"]),
        "category_primary": clean_multiline_value(fields["category_primary"]),
        "tags": tags,
        "meta_title": clean_multiline_value(fields["meta_title"]),
        "meta_description": clean_multiline_value(fields["meta_description"]),
        "focus_keyword": clean_multiline_value(fields.get("focus_keyword", "")),
        "article_markdown": article_markdown,
    }


def category_ids(category_name: str) -> list[int]:
    key = normalize_label(category_name)
    if key not in CATEGORY_IDS:
        raise PublishError(f"Categoría no mapeada: {category_name}")
    return [CATEGORY_IDS[key]]


def markdown_to_html(markdown_text: str) -> str:
    if markdown is not None:
        md = markdown.Markdown(extensions=["tables", "fenced_code"])
        return md.convert(markdown_text)

    blocks: list[str] = []
    paragraph: list[str] = []
    list_items: list[str] = []

    def flush_paragraph() -> None:
        nonlocal paragraph
        if paragraph:
            text = " ".join(line.strip() for line in paragraph)
            blocks.append(f"<p>{inline_markdown(text)}</p>")
            paragraph = []

    def flush_list() -> None:
        nonlocal list_items
        if list_items:
            items = "".join(f"<li>{inline_markdown(item)}</li>" for item in list_items)
            blocks.append(f"<ul>{items}</ul>")
            list_items = []

    for raw_line in markdown_text.splitlines():
        line = raw_line.rstrip()
        if not line.strip():
            flush_paragraph()
            flush_list()
            continue

        heading = re.match(r"^(#{1,6})\s+(.+)$", line)
        item = re.match(r"^\s*[-*]\s+(.+)$", line)
        if heading:
            flush_paragraph()
            flush_list()
            level = len(heading.group(1))
            blocks.append(f"<h{level}>{inline_markdown(heading.group(2).strip())}</h{level}>")
        elif item:
            flush_paragraph()
            list_items.append(item.group(1).strip())
        else:
            flush_list()
            paragraph.append(line)

    flush_paragraph()
    flush_list()
    return "\n".join(blocks)


def inline_markdown(text: str) -> str:
    escaped = html.escape(text)
    escaped = re.sub(r"\*\*(.+?)\*\*", r"<strong>\1</strong>", escaped)
    escaped = re.sub(r"`([^`]+)`", r"<code>\1</code>", escaped)
    escaped = re.sub(r"\[([^\]]+)\]\(([^)]+)\)", r'<a href="\2">\1</a>', escaped)
    return escaped


def base_headers() -> tuple[str, dict[str, str]]:
    wp_url = os.environ.get("WP_URL", "").rstrip("/")
    wp_user = os.environ.get("WP_USER", "")
    wp_password = os.environ.get("WP_APP_PASSWORD", "")

    if not all([wp_url, wp_user, wp_password]):
        raise PublishError("Faltan variables WP_URL, WP_USER o WP_APP_PASSWORD")

    auth = base64.b64encode(f"{wp_user}:{wp_password}".encode()).decode()
    return wp_url, {
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


def find_or_create_tag(base_url: str, headers: dict[str, str], name: str) -> int:
    query = urllib.parse.urlencode({"search": name, "per_page": 100})
    tags = wp_request(base_url, headers, "GET", f"/wp-json/wp/v2/tags?{query}")
    for tag in tags:
        if normalize_label(tag.get("name", "")) == normalize_label(name):
            return int(tag["id"])

    created = wp_request(base_url, headers, "POST", "/wp-json/wp/v2/tags", {"name": name})
    return int(created["id"])


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


def build_payload(article: dict[str, Any], tag_ids: list[int]) -> dict[str, Any]:
    return {
        "title": article["title"],
        "content": markdown_to_html(article["article_markdown"]),
        "status": "draft",
        "slug": article["slug"],
        "excerpt": article["excerpt"],
        "categories": category_ids(article["category_primary"]),
        "tags": tag_ids,
        "meta": {
            "jetpack_seo_html_title": article["meta_title"],
            "advanced_seo_description": article["meta_description"],
            "jetpack_seo_noindex": False,
            "jetpack_publicize_feature_enabled": False,
        },
    }


def preview_payload(article: dict[str, Any]) -> dict[str, Any]:
    return {
        "file": article["file"],
        "title": article["title"],
        "slug": article["slug"],
        "excerpt": article["excerpt"],
        "category_primary": article["category_primary"],
        "category_ids": category_ids(article["category_primary"]),
        "tags": article["tags"],
        "meta": {
            "jetpack_seo_html_title": article["meta_title"],
            "advanced_seo_description": article["meta_description"],
            "jetpack_seo_noindex": False,
            "jetpack_publicize_feature_enabled": False,
        },
        "content_chars": len(article["article_markdown"]),
    }


def verify_post(post: dict[str, Any], article: dict[str, Any], tag_ids: list[int]) -> dict[str, bool]:
    meta = post.get("meta") or {}
    return {
        "slug": post.get("slug") == article["slug"],
        "excerpt": bool((post.get("excerpt") or {}).get("raw") or (post.get("excerpt") or {}).get("rendered")),
        "categories": set(category_ids(article["category_primary"])).issubset(set(post.get("categories") or [])),
        "tags": set(tag_ids).issubset(set(post.get("tags") or [])),
        "seo_title": meta.get("jetpack_seo_html_title") == article["meta_title"],
        "seo_description": meta.get("advanced_seo_description") == article["meta_description"],
    }


def publish_article(article: dict[str, Any], base_url: str, headers: dict[str, str], update_existing: bool) -> dict[str, Any]:
    existing = find_existing_post(base_url, headers, article["slug"])
    if existing and not update_existing:
        raise PublishError(f"Ya existe una entrada con slug {article['slug']} (ID {existing.get('id')})")

    tag_ids = [find_or_create_tag(base_url, headers, tag) for tag in article["tags"]]
    payload = build_payload(article, tag_ids)

    if existing:
        post = wp_request(base_url, headers, "POST", f"/wp-json/wp/v2/posts/{existing['id']}?context=edit", payload)
        action = "updated"
    else:
        post = wp_request(base_url, headers, "POST", "/wp-json/wp/v2/posts?context=edit", payload)
        action = "created"

    checks = verify_post(post, article, tag_ids)
    if not all(checks.values()):
        raise PublishError(f"Verificación fallida para {article['slug']}: {checks}")

    return {
        "file": article["file"],
        "wp_id": post.get("id"),
        "link": post.get("link", ""),
        "title": article["title"],
        "slug": article["slug"],
        "tag_ids": tag_ids,
        "category_ids": payload["categories"],
        "verified": checks,
        "action": action,
        "status": "ok",
    }


def load_articles(run_path: Path) -> list[dict[str, Any]]:
    wp_ready_dir = run_path / "05-wordpress-ready"
    if not wp_ready_dir.exists():
        raise PublishError(f"{wp_ready_dir} no existe")

    articles = sorted(
        f
        for f in wp_ready_dir.glob("*.md")
        if not f.name.startswith("_") and "index" not in f.name.lower() and "assessment" not in f.name.lower()
    )
    if not articles:
        raise PublishError("No se encontraron artículos en 05-wordpress-ready/")
    return [parse_article(article) for article in articles]


def main() -> None:
    parser = argparse.ArgumentParser(description="Crea borradores WordPress con metadata completa.")
    parser.add_argument("--dry-run", action="store_true", help="Valida y genera wordpress-payload-preview.json sin llamar a WordPress.")
    parser.add_argument("--run-path", help="Ruta explícita del run. Por defecto usa outputs/current-run.json.")
    parser.add_argument("--update-existing", action="store_true", help="Actualiza borradores existentes con el mismo slug en vez de bloquear.")
    args = parser.parse_args()

    root = Path(__file__).parent.parent
    try:
        run_path = active_run_path(root, args.run_path)
        articles = load_articles(run_path)

        preview = {
            "generated_at": now_iso(),
            "publish": False,
            "total": len(articles),
            "articles": [preview_payload(article) for article in articles],
        }
        write_json(run_path / "wordpress-payload-preview.json", preview)

        if args.dry_run:
            print(f"Dry-run OK: {len(articles)} artículos validados. Preview: {run_path / 'wordpress-payload-preview.json'}")
            return

        base_url, headers = base_headers()
        results = []
        for article in articles:
            try:
                result = publish_article(article, base_url, headers, args.update_existing)
                print(f"OK {article['file']} -> ID {result['wp_id']} | {result['link']}")
                results.append(result)
            except PublishError as exc:
                print(f"ERR {article['file']} -> {exc}")
                results.append({"file": article["file"], "slug": article["slug"], "error": str(exc), "status": "error"})

        success = sum(1 for result in results if result.get("status") == "ok")
        log = {
            "generated_at": now_iso(),
            "publish": False,
            "total": len(results),
            "success": success,
            "error_count": len(results) - success,
            "results": results,
        }
        write_json(run_path / "06-wordpress-creation-log.json", log)

        print(f"\nResultado: {success}/{len(results)} borradores creados o actualizados")
        sys.exit(0 if success == len(results) else 1)
    except PublishError as exc:
        print(f"ERROR: {exc}", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()

#!/usr/bin/env python3
"""
Publica borradores en WordPress desde los outputs del pipeline PragmaWire.
Lee los artículos de 05-wordpress-ready/, convierte markdown a HTML
y los sube como borradores via la REST API de WordPress.

Uso:
    export WP_URL=https://pragmawire.com
    export WP_USER=usuario
    export WP_APP_PASSWORD="xxxx xxxx xxxx xxxx"
    python3 scripts/post_to_wp.py
"""

import json
import os
import re
import subprocess
import sys
from pathlib import Path

# Instalar dependencias si no están disponibles
try:
    import markdown
except ImportError:
    subprocess.check_call([sys.executable, "-m", "pip", "install", "markdown", "-q"])
    import markdown

try:
    import requests
except ImportError:
    subprocess.check_call([sys.executable, "-m", "pip", "install", "requests", "-q"])
    import requests

# IDs de categorías de pragmawire.com
CATEGORY_IDS = {
    "hogar inteligente": 16,
    "inteligencia artificial": 13,
    "productividad digital": 15,
    "recomendaciones tecnológicas": 5,
    "recomendaciones tecnologicas": 5,
    "salud y bienestar digital": 18,
    "salud y bienestar": 18,
    "seguridad digital": 14,
}


def get_category_id(category_name: str) -> list:
    if not category_name:
        return [1]
    normalized = category_name.lower().strip()
    for key, val in CATEGORY_IDS.items():
        if key in normalized or normalized in key:
            return [val]
    return [1]


def parse_wordpress_draft(content: str) -> dict:
    """Extrae metadatos del bloque WORDPRESS_DRAFT_VALIDADO."""
    meta = {"title": "", "slug": "", "excerpt": "", "category": "", "tags": []}

    # Buscar el bloque WORDPRESS_DRAFT_VALIDADO
    wp_block = ""
    if "WORDPRESS_DRAFT_VALIDADO:" in content:
        parts = content.split("WORDPRESS_DRAFT_VALIDADO:", 1)
        if len(parts) > 1:
            # Termina en ARTICLE_MARKDOWN o el siguiente bloque ---
            end_markers = ["ARTICLE_MARKDOWN:", "\n---\n\nARTICLE_MARKDOWN"]
            wp_block = parts[1]
            for marker in end_markers:
                if marker in wp_block:
                    wp_block = wp_block.split(marker, 1)[0]
                    break

    if wp_block:
        for line in wp_block.split("\n"):
            line = line.strip()
            if line.startswith("title:"):
                meta["title"] = line[6:].strip()
            elif line.startswith("slug:"):
                meta["slug"] = line[5:].strip()
            elif line.startswith("excerpt:"):
                meta["excerpt"] = line[8:].strip()
            elif line.startswith("category_primary:"):
                meta["category"] = line[17:].strip()
            elif line.startswith("tags:"):
                raw = line[5:].strip()
                meta["tags"] = [t.strip() for t in raw.split(",") if t.strip()]

    return meta


def extract_article_body(content: str) -> str:
    """Extrae el cuerpo del artículo desde ARTICLE_MARKDOWN:"""
    for marker in ["ARTICLE_MARKDOWN:\n", "ARTICLE_MARKDOWN:"]:
        if marker in content:
            body = content.split(marker, 1)[1]
            # Cortar antes de FAQ_SCHEMA_CANDIDATES si existe
            if "\nFAQ_SCHEMA_CANDIDATES:" in body:
                body = body.split("\nFAQ_SCHEMA_CANDIDATES:")[0]
            return body.strip()
    return content.strip()


def post_article(article_path: Path, wp_url: str, wp_user: str, wp_password: str) -> tuple:
    content = article_path.read_text(encoding="utf-8")
    meta = parse_wordpress_draft(content)
    body = extract_article_body(content)

    # Markdown → HTML
    md = markdown.Markdown(extensions=["tables", "fenced_code"])
    html = md.convert(body)

    title = meta["title"] or article_path.stem
    payload = {
        "title": title,
        "content": html,
        "status": "draft",
        "categories": get_category_id(meta["category"]),
    }
    if meta["slug"]:
        payload["slug"] = meta["slug"]
    if meta["excerpt"]:
        payload["excerpt"] = meta["excerpt"]

    endpoint = f"{wp_url}/wp-json/wp/v2/posts"

    def do_post(url, verify_ssl=True):
        # Do NOT auto-follow redirects on POST — a 301/302 would convert POST to GET
        r = requests.post(
            url,
            json=payload,
            auth=(wp_user, wp_password),
            headers={"Accept": "application/json"},
            allow_redirects=False,
            timeout=60,
            verify=verify_ssl,
        )
        # Follow redirect manually, keeping POST method and auth
        if r.status_code in (301, 302, 307, 308):
            location = r.headers.get("Location", "")
            if location:
                r = requests.post(
                    location,
                    json=payload,
                    auth=(wp_user, wp_password),
                    headers={"Accept": "application/json"},
                    allow_redirects=False,
                    timeout=60,
                    verify=verify_ssl,
                )
        return r

    try:
        resp = do_post(endpoint, verify_ssl=True)
    except requests.exceptions.SSLError:
        try:
            resp = do_post(endpoint, verify_ssl=False)
        except Exception as e2:
            return False, f"SSL error + retry failed: {e2}"
    except requests.exceptions.ConnectionError as e:
        return False, f"Connection error: {e}"
    except requests.exceptions.Timeout:
        return False, "Timeout (60s)"
    except Exception as e:
        return False, f"Request error: {e}"

    if resp.status_code not in (200, 201):
        return False, f"HTTP {resp.status_code} at {resp.url}: {resp.text[:300]}"

    try:
        data = resp.json()
    except Exception:
        return False, f"Respuesta inválida (HTTP {resp.status_code}): {resp.text[:200]}"

    if isinstance(data, list):
        return False, f"API returned list instead of post object (HTTP {resp.status_code}, url={resp.url})"

    if "id" in data:
        return True, {"id": data["id"], "link": data.get("link", ""), "title": title}
    return False, data.get("message") or data.get("code") or str(data)[:200]


def main():
    wp_url = os.environ.get("WP_URL", "").strip().strip("<>").rstrip("/")
    wp_user = os.environ.get("WP_USER", "")
    wp_password = os.environ.get("WP_APP_PASSWORD", "")

    if not all([wp_url, wp_user, wp_password]):
        print("ERROR: Faltan variables WP_URL, WP_USER o WP_APP_PASSWORD")
        sys.exit(1)

    root = Path(__file__).parent.parent
    current_run_file = root / "outputs" / "current-run.json"

    if not current_run_file.exists():
        print("ERROR: outputs/current-run.json no encontrado. Ejecuta init_run.py primero.")
        sys.exit(1)

    current_run = json.loads(current_run_file.read_text())
    run_path = Path(current_run["active_run_path"])
    wp_ready_dir = run_path / "05-wordpress-ready"

    if not wp_ready_dir.exists():
        print(f"ERROR: {wp_ready_dir} no existe")
        sys.exit(1)

    articles = sorted(
        f for f in wp_ready_dir.glob("*.md")
        if not f.name.startswith("_") and "index" not in f.name.lower()
    )

    if not articles:
        print("No se encontraron artículos en 05-wordpress-ready/")
        sys.exit(1)

    print(f"Publicando {len(articles)} borradores en WordPress ({wp_url})...")
    results = []
    success = 0

    for article in articles:
        print(f"  Procesando {article.name}...")
        ok, data = post_article(article, wp_url, wp_user, wp_password)
        if ok:
            print(f"  OK {article.name} → ID {data['id']} | {data['link']}")
            results.append({
                "file": article.name,
                "wp_id": data["id"],
                "link": data["link"],
                "title": data["title"],
                "status": "ok",
            })
            success += 1
        else:
            print(f"  ERR {article.name} → {data}")
            results.append({"file": article.name, "error": str(data), "status": "error"})

    log_path = run_path / "06-wordpress-creation-log.json"
    log_path.write_text(
        json.dumps({"results": results, "total": len(articles), "success": success}, ensure_ascii=False, indent=2)
    )

    print(f"\nResultado: {success}/{len(articles)} borradores creados")
    print(f"Log: {log_path}")
    sys.exit(0 if success == len(articles) else 1)


if __name__ == "__main__":
    main()

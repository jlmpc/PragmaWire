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

# Instalar markdown si no está disponible
try:
    import markdown
except ImportError:
    subprocess.check_call([sys.executable, "-m", "pip", "install", "markdown", "-q"])
    import markdown

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


def parse_article(content: str) -> tuple:
    """Extrae metadatos y cuerpo del artículo."""
    meta = {"title": "", "slug": "", "excerpt": "", "category": "", "tags": []}

    # Si el output viene del supervisor (sub-agente), extraer solo WORDPRESS_DRAFT_VALIDADO
    working = content
    if "WORDPRESS_DRAFT_VALIDADO:" in content:
        working = content.split("WORDPRESS_DRAFT_VALIDADO:", 1)[1].strip()
        for end in ["NOTAS_PARA_REVISION_HUMANA:", "ESTADO_SUPERVISION_FINAL:"]:
            if end in working:
                working = working.split(end)[0].strip()

    lines = working.split("\n")

    # Título: primera línea con #
    for line in lines:
        if line.startswith("# ") and not meta["title"]:
            meta["title"] = line[2:].strip()
            break

    # Metadatos en formato **Campo:** valor
    for line in lines:
        m = re.match(r"\*\*([^*]+)\*\*:?\s*(.*)", line)
        if not m:
            continue
        key = m.group(1).lower().strip()
        val = m.group(2).strip().strip("*").strip()
        if "título" in key or "title" in key:
            if val:
                meta["title"] = val
        elif "slug" in key:
            meta["slug"] = val
        elif "excerpt" in key or "extracto" in key or "descripción" in key:
            meta["excerpt"] = val
        elif "categoría" in key or "categoria" in key:
            meta["category"] = val
        elif "palabras clave" in key or "tags" in key or "etiquetas" in key:
            meta["tags"] = [t.strip() for t in re.split(r"[,;]", val) if t.strip()]

    # Extraer suggested_featured_image para añadirlo al final del borrador
    featured_image_note = ""
    if "suggested_featured_image:" in working:
        img_raw = working.split("suggested_featured_image:", 1)[1]
        img_end = img_raw.find("\nARTICLE_MARKDOWN:")
        if img_end == -1:
            img_end = img_raw.find("\n## ARTICULO")
        if img_end > 0:
            img_raw = img_raw[:img_end]
        img_raw = img_raw.strip()
        if img_raw:
            featured_image_note = f"\n\n---\n**🖼 Imagen destacada sugerida:**\n```\n{img_raw}\n```"

    # Cuerpo: buscar ARTICLE_MARKDOWN (editor) o marcadores alternativos
    body = working
    for marker in ["ARTICLE_MARKDOWN:", "## ARTICULO_FINAL_MARKDOWN", "## CONTENIDO_FINAL", "## CONTENIDO"]:
        if marker in working:
            body = working.split(marker, 1)[1].strip()
            # Cortar en la siguiente sección mayor (excepto FAQ que forma parte del artículo)
            for end_section in ["\nFAQ_SCHEMA_CANDIDATES:", "\nupdate_level:", "\nobsolescence_risk:"]:
                if end_section in body:
                    body = body.split(end_section)[0].strip()
            break

    # Añadir imagen sugerida al final del borrador (visible al editar, eliminar antes de publicar)
    if featured_image_note:
        body += featured_image_note

    return meta, body


def post_article(article_path: Path, wp_url: str, wp_user: str, wp_password: str) -> tuple:
    content = article_path.read_text(encoding="utf-8")
    meta, body = parse_article(content)

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

    result = subprocess.run(
        [
            "curl", "-s", "-X", "POST",
            f"{wp_url}/wp-json/wp/v2/posts",
            "-u", f"{wp_user}:{wp_password}",
            "-H", "Content-Type: application/json",
            "-d", json.dumps(payload, ensure_ascii=False),
            "--max-time", "30",
        ],
        capture_output=True,
        text=True,
    )

    if result.returncode != 0:
        return False, f"curl error: {result.stderr}"

    try:
        resp = json.loads(result.stdout)
    except json.JSONDecodeError:
        return False, f"Respuesta inválida: {result.stdout[:200]}"

    if "id" in resp:
        return True, {"id": resp["id"], "link": resp.get("link", ""), "title": title}
    return False, resp.get("message") or resp.get("code") or result.stdout[:200]


def update_memory(root: Path, run_id: str, articles_posted: list):
    """Actualiza memory/articulos_publicados.json con los artículos subidos a WordPress."""
    from datetime import date

    memory_file = root / "memory" / "articulos_publicados.json"
    try:
        existing = json.loads(memory_file.read_text(encoding="utf-8")) if memory_file.exists() else []
    except (json.JSONDecodeError, OSError):
        existing = []

    existing_slugs = {a.get("slug", "") for a in existing}

    for item in articles_posted:
        slug = item.get("slug", "")
        if slug and slug in existing_slugs:
            # Actualizar entrada existente con datos de WordPress
            for entry in existing:
                if entry.get("slug") == slug:
                    entry["wp_id"] = item.get("wp_id")
                    entry["wp_link"] = item.get("wp_link")
                    entry["estado"] = "borrador_wp"
                    break
        else:
            new_entry = {
                "title": item.get("title", ""),
                "slug": slug,
                "categoria": item.get("categoria", ""),
                "fecha_publicacion": date.today().isoformat(),
                "estado": "borrador_wp",
                "wp_id": item.get("wp_id"),
                "wp_link": item.get("wp_link"),
                "run_id": run_id,
            }
            existing.append(new_entry)
            if slug:
                existing_slugs.add(slug)

    memory_file.write_text(json.dumps(existing, ensure_ascii=False, indent=2), encoding="utf-8")


def update_run_history(root: Path, run_id: str, results: list, success: int):
    """Actualiza memory/run-history.json con el resumen de esta ejecución."""
    from datetime import date

    history_file = root / "memory" / "run-history.json"
    try:
        history = json.loads(history_file.read_text(encoding="utf-8")) if history_file.exists() else []
    except (json.JSONDecodeError, OSError):
        history = []

    entry = {
        "run_id": run_id,
        "fecha": date.today().isoformat(),
        "articulos_enviados_wp": success,
        "articulos_fallidos": len(results) - success,
        "slugs": [r.get("slug", r.get("file", "")) for r in results if r.get("status") == "ok"],
    }
    history.append(entry)

    history_file.write_text(json.dumps(history, ensure_ascii=False, indent=2), encoding="utf-8")


def main():
    wp_url = os.environ.get("WP_URL", "").rstrip("/")
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
    run_id = current_run.get("active_run_id", "unknown")
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

    print(f"Publicando {len(articles)} borradores en WordPress...")
    results = []
    memory_updates = []
    success = 0

    for article in articles:
        meta, _ = parse_article(article.read_text(encoding="utf-8"))
        ok, data = post_article(article, wp_url, wp_user, wp_password)
        if ok:
            print(f"  OK {article.name} → ID {data['id']} | {data['link']}")
            results.append({"file": article.name, "wp_id": data["id"], "link": data["link"], "title": data["title"], "status": "ok"})
            memory_updates.append({
                "title": data["title"],
                "slug": meta.get("slug", ""),
                "categoria": meta.get("category", ""),
                "wp_id": data["id"],
                "wp_link": data["link"],
            })
            success += 1
        else:
            print(f"  ERR {article.name} → {data}")
            results.append({"file": article.name, "error": str(data), "status": "error"})

    log_path = run_path / "06-wordpress-creation-log.json"
    log_path.write_text(json.dumps({"results": results, "total": len(articles), "success": success}, ensure_ascii=False, indent=2))

    if memory_updates:
        try:
            update_memory(root, run_id, memory_updates)
            print(f"  Memoria actualizada: {len(memory_updates)} artículos registrados en articulos_publicados.json")
        except Exception as e:
            print(f"  AVISO: No se pudo actualizar articulos_publicados.json: {e}")

        try:
            update_run_history(root, run_id, results, success)
        except Exception as e:
            print(f"  AVISO: No se pudo actualizar run-history.json: {e}")

    print(f"\nResultado: {success}/{len(articles)} borradores creados")
    sys.exit(0 if success == len(articles) else 1)


if __name__ == "__main__":
    main()

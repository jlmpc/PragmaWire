#!/usr/bin/env python3
"""Creates WordPress drafts for all 12 articles from the current run."""

import os
import re
import json
import base64
import urllib.request
import urllib.error

WP_URL = os.environ["WP_URL"].strip("<>").rstrip("/")
WP_USER = os.environ["WP_USER"]
WP_APP_PASSWORD = os.environ["WP_APP_PASSWORD"]

AUTH = base64.b64encode(f"{WP_USER}:{WP_APP_PASSWORD}".encode()).decode()
HEADERS = {
    "Authorization": f"Basic {AUTH}",
    "Content-Type": "application/json",
}

RUN_DIR = "/home/user/PragmaWire/outputs/runs/2026-04-29T1502_pragmawire_2f44"

ARTICLES = [
    {"id": "001", "title": "Qué es Matter: el protocolo que hace que todos tus dispositivos inteligentes se entiendan por fin", "slug": "que-es-matter-domotica", "excerpt": "Matter es el protocolo que hace que dispositivos de Amazon, Google y Apple funcionen juntos. Cómo funciona, qué dispositivos son compatibles y cómo reconocerlo en la caja."},
    {"id": "002", "title": "Home Assistant para principiantes: automatiza tu casa aunque no sepas nada de tecnología", "slug": "home-assistant-principiantes", "excerpt": "Instala Home Assistant desde cero: hardware, configuración en menos de una hora y automatizaciones sin programar. Guía práctica para principiantes 2026."},
    {"id": "003", "title": "Agentes de IA: qué son, para qué sirven y cómo puedes usarlos hoy mismo", "slug": "que-son-agentes-de-ia", "excerpt": "Los agentes de IA no solo responden preguntas: toman acciones por ti. Te explicamos qué son, en qué se diferencian de un chatbot y cómo activar tus primeras automatizaciones hoy."},
    {"id": "004", "title": "ChatGPT, Claude o Gemini: cuál usar en 2026 según lo que necesitas", "slug": "chatgpt-vs-claude-vs-gemini-2026", "excerpt": "No hay una IA mejor: hay la más adecuada para lo que haces. Comparamos ChatGPT, Claude y Gemini en 2026 con tabla, casos de uso y recomendación por perfil."},
    {"id": "005", "title": "Notion para principiantes: cómo empezar sin perderte en la configuración", "slug": "notion-para-principiantes", "excerpt": "Abriste Notion y no sabes por dónde empezar. Esta guía te explica los 3 conceptos clave, las 3 páginas que necesitas crear el primer día y cuándo Notion no es la mejor opción."},
    {"id": "006", "title": "Cómo automatizar tareas repetitivas con IA sin saber programar (2026)", "slug": "automatizar-tareas-ia-sin-programar", "excerpt": "5 automatizaciones reales que puedes activar hoy con ChatGPT Tasks, Gemini, Notion AI, Zapier y Make. Sin código, sin conocimientos técnicos. Guía paso a paso."},
    {"id": "007", "title": "Anillos inteligentes 2026: Oura Ring, Galaxy Ring y RingConn comparados", "slug": "anillos-inteligentes-cual-comprar-2026", "excerpt": "Comparamos los tres mejores anillos inteligentes de 2026 (Oura Ring 4, Samsung Galaxy Ring, RingConn) con tabla, precios y recomendación por perfil. Sin hype."},
    {"id": "008", "title": "Gadgets de viaje 2026: los que sí valen la pena (y los que dejarías en casa)", "slug": "gadgets-viaje-2026", "excerpt": "Los 5 gadgets de viaje con retorno real: cargador GaN, rastreador Bluetooth, eSIM, power bank y cable multiconector. Sin listas de 25 artículos que nadie usa."},
    {"id": "009", "title": "Tecnología para dormir mejor: apps y hábitos que funcionan de verdad (2026)", "slug": "mejorar-sueno-tecnologia", "excerpt": "Entre tantas apps de sueño, ¿cuáles funcionan de verdad? Te explicamos qué puede y qué no puede hacer la tecnología por tu sueño, con checklist de rutina nocturna."},
    {"id": "010", "title": "Bienestar digital: cómo reducir el tiempo de pantalla sin afectar a tu trabajo", "slug": "bienestar-digital-limites-pantallas", "excerpt": "Reduce tu tiempo de pantalla con las herramientas que ya tienes en el teléfono: Screen Time (iOS) y Digital Wellbeing (Android). Guía práctica con checklist de 15 minutos."},
    {"id": "011", "title": "Quishing: qué es el phishing con códigos QR y cómo protegerte en 5 pasos", "slug": "que-es-el-quishing", "excerpt": "El quishing usa códigos QR para llevarte a webs fraudulentas. Te explicamos qué es, por qué es más peligroso que el phishing clásico y 5 pasos para protegerte."},
    {"id": "012", "title": "Las estafas digitales más usadas en España en 2026: cómo detectarlas y qué hacer si caes", "slug": "estafas-digitales-espana-2026", "excerpt": "Las 5 estafas digitales más activas en España en 2026: phishing bancario, smishing de Hacienda, fraude por WhatsApp, falsas ofertas de trabajo y quishing. Con qué hacer si caes."},
]


def extract_article_body(article_id: str) -> str:
    """Extracts ARTICULO_FINAL_MARKDOWN section from edited file."""
    path = f"{RUN_DIR}/04-edited/articulo_{article_id}_edited.md"
    with open(path, "r", encoding="utf-8") as f:
        content = f.read()

    # Extract between ## ARTICULO_FINAL_MARKDOWN and ## NOTAS_EDITOR_FINAL
    match = re.search(
        r"## ARTICULO_FINAL_MARKDOWN\s*\n(.*?)(?=\n## NOTAS_EDITOR_FINAL|\Z)",
        content,
        re.DOTALL,
    )
    if match:
        return match.group(1).strip()
    return content


def create_wp_draft(article: dict, body: str) -> dict:
    """POSTs a draft to WordPress REST API and returns the response."""
    payload = json.dumps({
        "title": article["title"],
        "content": body,
        "excerpt": article["excerpt"],
        "slug": article["slug"],
        "status": "draft",
    }).encode("utf-8")

    req = urllib.request.Request(
        f"{WP_URL}/wp-json/wp/v2/posts",
        data=payload,
        headers=HEADERS,
        method="POST",
    )
    try:
        with urllib.request.urlopen(req, timeout=30) as resp:
            return {"success": True, "status_code": resp.status, "data": json.loads(resp.read())}
    except urllib.error.HTTPError as e:
        body_err = e.read().decode("utf-8", errors="replace")
        return {"success": False, "status_code": e.code, "error": body_err}
    except Exception as e:
        return {"success": False, "status_code": 0, "error": str(e)}


results = []
for article in ARTICLES:
    body = extract_article_body(article["id"])
    result = create_wp_draft(article, body)
    entry = {
        "articulo_id": f"articulo_{article['id']}",
        "slug": article["slug"],
        "success": result["success"],
        "status_code": result["status_code"],
    }
    if result["success"]:
        data = result.get("data", {})
        entry["wp_post_id"] = data.get("id")
        entry["wp_post_link"] = data.get("link")
        entry["wp_status"] = data.get("status")
        print(f"  OK  articulo_{article['id']} → WP ID {entry['wp_post_id']} ({article['slug']})")
    else:
        entry["error"] = result.get("error", "")[:200]
        print(f"  ERR articulo_{article['id']} → HTTP {result['status_code']}: {entry['error'][:120]}")
    results.append(entry)

# Save results
out_path = f"{RUN_DIR}/06-wordpress-creation-log.json"
with open(out_path, "w", encoding="utf-8") as f:
    json.dump({
        "run_id": "2026-04-29T1502_pragmawire_2f44",
        "fecha": "2026-04-29T17:45:00",
        "total": len(results),
        "success_count": sum(1 for r in results if r["success"]),
        "error_count": sum(1 for r in results if not r["success"]),
        "publish": False,
        "results": results,
    }, f, indent=2, ensure_ascii=False)

print(f"\nLog saved to {out_path}")
success_count = sum(1 for r in results if r["success"])
print(f"Result: {success_count}/{len(results)} drafts created successfully")

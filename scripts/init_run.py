#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
import secrets
from datetime import datetime
from pathlib import Path

CATEGORIES = [
    "Hogar Inteligente",
    "Inteligencia Artificial",
    "Productividad Digital",
    "Recomendaciones Tecnológicas",
    "Salud y Bienestar Digital",
    "Seguridad Digital",
]

def now_iso() -> str:
    return datetime.now().replace(microsecond=0).isoformat()

def make_run_id() -> str:
    stamp = datetime.now().strftime("%Y-%m-%dT%H%M")
    suffix = secrets.token_hex(2)
    return f"{stamp}_pragmawire_{suffix}"

def write_json(path: Path, data: dict) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(data, ensure_ascii=False, indent=2), encoding="utf-8")

def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--mode", choices=["SIMULACION", "PRODUCCION_DRAFT", "AUDITORIA"], default="SIMULACION")
    args = parser.parse_args()

    root = Path.cwd()
    run_id = make_run_id()
    run_path = root / "outputs" / "runs" / run_id

    for folder in [
        "01-run-context",
        "02-briefings",
        "03-drafts",
        "04-edited",
        "05-wordpress-ready",
        "logs",
    ]:
        (run_path / folder).mkdir(parents=True, exist_ok=True)

    created_at = now_iso()

    current_run = {
        "active_run_id": run_id,
        "active_run_path": str(run_path),
        "current_stage": "01-run-context",
        "next_agent": "supervisor-inicial",
        "status": "initialized",
        "execution_mode": args.mode,
        "wordpress_destination": "WORDPRESS_DRAFT",
        "publish_allowed": False,
        "updated_at": created_at,
    }

    manifest = {
        "run_id": run_id,
        "run_path": str(run_path),
        "created_at": created_at,
        "updated_at": created_at,
        "execution_mode": args.mode,
        "wordpress_destination": "WORDPRESS_DRAFT",
        "publish_allowed": False,
        "overall_status": "initialized",
        "current_stage": "01-run-context",
        "next_agent": "supervisor-inicial",
        "stages": {
            "01-run-context": {"agent": "supervisor-inicial", "status": "pending", "stage_complete": False, "output_paths": []},
            "02-briefings": {"agent": "agente-investigador", "status": "pending", "stage_complete": False, "output_paths": [], "valid_outputs_count": 0},
            "03-drafts": {"agent": "agente-redactor", "status": "pending", "stage_complete": False, "output_paths": [], "valid_outputs_count": 0},
            "04-edited": {"agent": "agente-editor-estrategico", "status": "pending", "stage_complete": False, "output_paths": [], "approved_wordpress_drafts": 0},
            "05-wordpress-ready": {"agent": "supervisor-final", "status": "pending", "stage_complete": False, "output_paths": [], "approved_for_wordpress_draft": 0}
        },
        "category_coverage": {category: 0 for category in CATEGORIES},
        "errors": [],
        "warnings": [],
        "blocked_reason": "",
    }

    write_json(root / "outputs" / "current-run.json", current_run)
    write_json(run_path / "run-manifest.json", manifest)

    (run_path / "logs" / "pipeline-log.md").write_text(
        f"# Pipeline Log\n\nRUN_ID: `{run_id}`\n\nCreated at: `{created_at}`\n\nMode: `{args.mode}`\n",
        encoding="utf-8",
    )

    print(f"RUN inicializado: {run_id}")
    print(f"Ruta: {run_path}")
    print("Siguiente agente: supervisor-inicial")

if __name__ == "__main__":
    main()

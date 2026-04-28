#!/usr/bin/env python3
from __future__ import annotations

import json
import sys
from pathlib import Path

def fail(msg: str) -> None:
    print(f"FAIL: {msg}")
    sys.exit(1)

def ok(msg: str) -> None:
    print(f"OK: {msg}")

def load_json(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))

def main() -> None:
    root = Path.cwd()
    current = root / "outputs" / "current-run.json"
    if not current.exists():
        fail("No existe outputs/current-run.json. Ejecuta python scripts/init_run.py")

    data = load_json(current)
    run_path = Path(data["active_run_path"])

    if not run_path.exists():
        fail(f"No existe la carpeta activa: {run_path}")

    manifest = run_path / "run-manifest.json"
    if not manifest.exists():
        fail("No existe run-manifest.json")

    m = load_json(manifest)

    if m.get("publish_allowed") is not False:
        fail("publish_allowed debe ser false")

    if m.get("wordpress_destination") != "WORDPRESS_DRAFT":
        fail("wordpress_destination debe ser WORDPRESS_DRAFT")

    ok("Estructura básica correcta")
    print(f"RUN activo: {data['active_run_id']}")
    print(f"Siguiente agente: {data['next_agent']}")

if __name__ == "__main__":
    main()

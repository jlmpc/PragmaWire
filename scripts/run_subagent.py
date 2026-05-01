#!/usr/bin/env python3
"""
Sub-agente PragmaWire — llamada API con contexto limpio.
Evita timeouts de streaming ejecutando editor y supervisor
como llamadas independientes fuera del contexto del orquestador.

Uso:
    python scripts/run_subagent.py --agent editor --article 1
    python scripts/run_subagent.py --agent supervisor --article 2
"""

import argparse
import json
import sys
from pathlib import Path

try:
    import anthropic
except ImportError:
    import subprocess
    subprocess.check_call([sys.executable, "-m", "pip", "install", "anthropic", "-q"])
    import anthropic

AGENT_CONFIG = {
    "editor": {
        "instructions_file": "agents/agente-editor-estrategico.md",
        "input_dir": "03-drafts",
        "input_suffix": "_draft.md",
        "output_dir": "04-edited",
        "output_suffix": "_edited.md",
        "needs_briefing": True,
    },
    "supervisor": {
        "instructions_file": "agents/supervisor-final.md",
        "input_dir": "04-edited",
        "input_suffix": "_edited.md",
        "output_dir": "05-wordpress-ready",
        "output_suffix": "_wordpress_ready.md",
        "needs_briefing": False,
    },
}


def main():
    parser = argparse.ArgumentParser(description="Ejecuta un sub-agente PragmaWire con contexto limpio")
    parser.add_argument("--agent", required=True, choices=list(AGENT_CONFIG.keys()),
                        help="Agente a ejecutar: editor o supervisor")
    parser.add_argument("--article", required=True, type=int,
                        help="Número de artículo (1, 2 o 3)")
    args = parser.parse_args()

    root = Path(__file__).parent.parent
    cfg = AGENT_CONFIG[args.agent]
    num = f"{args.article:03d}"

    current_run_file = root / "outputs" / "current-run.json"
    if not current_run_file.exists():
        print(f"ERROR: No existe outputs/current-run.json. Ejecuta init_run.py primero.")
        sys.exit(1)

    current_run = json.loads(current_run_file.read_text())
    run_path = Path(current_run["active_run_path"])

    input_file = run_path / cfg["input_dir"] / f"articulo_{num}{cfg['input_suffix']}"
    output_file = run_path / cfg["output_dir"] / f"articulo_{num}{cfg['output_suffix']}"

    if not input_file.exists():
        print(f"ERROR: Archivo de entrada no encontrado: {input_file}")
        sys.exit(1)

    instructions_path = root / cfg["instructions_file"]
    if not instructions_path.exists():
        print(f"ERROR: Instrucciones de agente no encontradas: {instructions_path}")
        sys.exit(1)

    system_prompt = instructions_path.read_text()

    article_content = input_file.read_text()
    user_content = (
        "El contenido a procesar está incluido directamente a continuación. "
        "No necesitas leer archivos adicionales del sistema de archivos.\n\n"
        f"## Artículo\n\n{article_content}"
    )

    if cfg["needs_briefing"]:
        briefing_candidates = sorted(
            (run_path / "02-briefings").glob(f"briefing_{num}*.md")
        )
        if briefing_candidates:
            user_content += f"\n\n## Briefing de referencia\n\n{briefing_candidates[0].read_text()}"
        else:
            print(f"[AVISO] No se encontró briefing_{num}*.md — editando sin briefing")

    client = anthropic.Anthropic()

    print(f"[sub-agente:{args.agent}] procesando artículo {num}...")

    message = client.messages.create(
        model="claude-sonnet-4-6",
        max_tokens=8000,
        system=system_prompt,
        messages=[{"role": "user", "content": user_content}],
    )

    result = message.content[0].text

    output_file.parent.mkdir(parents=True, exist_ok=True)
    output_file.write_text(result, encoding="utf-8")

    print(f"[sub-agente:{args.agent}] artículo {num} guardado → {output_file.name}")
    sys.exit(0)


if __name__ == "__main__":
    main()

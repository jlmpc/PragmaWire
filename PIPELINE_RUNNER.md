# PIPELINE RUNNER — PragmaWire

Este archivo explica cómo ejecutar el sistema sin mezclar outputs.

## Inicio

Ejecuta desde la raíz del repo:

```bash
python scripts/init_run.py
```

Esto crea:

```text
outputs/current-run.json
outputs/runs/[RUN_ID]/
outputs/runs/[RUN_ID]/run-manifest.json
```

## Después

Usa el prompt de:

```text
PROMPT_MAESTRO_RUN_ID.md
```

en Claude Code.

## Validación

Cuando quieras comprobar que la estructura está bien:

```bash
python scripts/validate_run.py
```

## Prohibición

No publicar automáticamente en WordPress.

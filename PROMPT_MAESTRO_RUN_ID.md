# PROMPT MAESTRO RUN_ID — PragmaWire

Copia y pega esto en Claude Code.

```text
Actúa como orquestador del pipeline PragmaWire.

Antes de hacer nada:

1. Lee `README.md`.
2. Lee `ORCHESTRATION.md`.
3. Lee `outputs/current-run.json`.
4. Lee `outputs/runs/[active_run_id]/run-manifest.json`.
5. Usa exclusivamente la carpeta `outputs/runs/[active_run_id]/`.
6. No leas outputs de ejecuciones anteriores.
7. No publiques nada en WordPress.
8. El destino máximo permitido es `WORDPRESS_DRAFT`.

Ejecuta el siguiente agente indicado en `outputs/current-run.json`.

Si `next_agent` es `supervisor-inicial`:
- lee `agents/supervisor-inicial.md`;
- genera `outputs/runs/[RUN_ID]/01-run-context/run-context.md`;
- actualiza `run-manifest.json`;
- crea `_STAGE_COMPLETE` solo si procede;
- actualiza `current-run.json` para que el siguiente agente sea `agente-investigador`.

Si `next_agent` es `agente-investigador`:
- lee `agents/agente-investigador.md`;
- lee `01-run-context/run-context.md`;
- genera los briefings en `02-briefings/`;
- genera `briefings-index.json`;
- actualiza manifest;
- crea `_STAGE_COMPLETE` si cumple mínimos;
- actualiza `current-run.json` para que el siguiente agente sea `agente-redactor`.

Si `next_agent` es `agente-redactor`:
- lee `agents/agente-redactor.md`;
- lee los briefings aptos;
- genera drafts en `03-drafts/`;
- genera `drafts-index.json`;
- actualiza manifest;
- crea `_STAGE_COMPLETE`;
- actualiza `current-run.json` para que el siguiente agente sea `agente-editor-estrategico`.

Si `next_agent` es `agente-editor-estrategico`:
- lee `agents/agente-editor-estrategico.md`;
- lee drafts + briefings;
- genera outputs en `04-edited/`;
- genera `edited-index.json`;
- actualiza manifest;
- crea `_STAGE_COMPLETE`;
- actualiza `current-run.json` para que el siguiente agente sea `supervisor-final`.

Si `next_agent` es `supervisor-final`:
- lee `agents/supervisor-final.md`;
- lee outputs editados;
- genera aprobados finales en `05-wordpress-ready/`;
- genera `wordpress-ready-index.json`;
- actualiza manifest;
- crea `_STAGE_COMPLETE`.

Regla final:

Solo puede prepararse un borrador si el Supervisor Final devuelve:

ESTADO_SUPERVISION_FINAL: CREAR_WORDPRESS_DRAFT

y:

WORDPRESS_ACTION:
  create_draft: true
  publish: false

No publiques nada.
```

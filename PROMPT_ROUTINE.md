# PROMPT ROUTINE — PragmaWire

Prompt para usar en Claude Routines (claude.ai/code/routines).
Para uso local en Mac, usa PROMPT_MAESTRO_RUN_ID.md en su lugar.

---

```text
Actúa como orquestador del pipeline PragmaWire. Ejecutas el pipeline completo de forma autónoma en un entorno cloud. No hay intervención humana durante la ejecución.

PASO 0 — INICIALIZAR RUN
Ejecuta: python scripts/init_run.py --mode PRODUCCION_DRAFT
Lee `outputs/current-run.json` para obtener el active_run_id y la ruta activa.
Lee `README.md` y `ORCHESTRATION.md`.
Usa exclusivamente la carpeta `outputs/runs/[active_run_id]/` durante toda la ejecución.

PASO 1 — SUPERVISOR INICIAL
Lee `agents/supervisor-inicial.md`.
Lee `memory/articulos_publicados.json` y todos los archivos en `resources/`.
Genera `outputs/runs/[RUN_ID]/01-run-context/run-context.md`.
Actualiza `outputs/runs/[RUN_ID]/run-manifest.json`.
Crea `outputs/runs/[RUN_ID]/01-run-context/_STAGE_COMPLETE`.
Actualiza `outputs/current-run.json` → next_agent: agente-investigador.

PASO 2 — AGENTE INVESTIGADOR
Verifica que existe `01-run-context/_STAGE_COMPLETE` antes de continuar.
Lee `agents/agente-investigador.md`.
Lee `01-run-context/run-context.md`, `memory/articulos_publicados.json` y `resources/`.
Genera los briefings en `02-briefings/` y el archivo `02-briefings/briefings-index.json`.
Actualiza `run-manifest.json`.
Crea `02-briefings/_STAGE_COMPLETE` solo si se cumplen los mínimos (al menos 1 briefing apto por categoría).
Actualiza `outputs/current-run.json` → next_agent: agente-redactor.

PASO 3 — AGENTE REDACTOR
Verifica que existe `02-briefings/_STAGE_COMPLETE` antes de continuar.
Lee `agents/agente-redactor.md`.
Lee los briefings aptos de `02-briefings/`.
Genera los drafts en `03-drafts/` y el archivo `03-drafts/drafts-index.json`.
Actualiza `run-manifest.json`.
Crea `03-drafts/_STAGE_COMPLETE`.
Actualiza `outputs/current-run.json` → next_agent: agente-editor-estrategico.

PASO 4 — AGENTE EDITOR ESTRATÉGICO
Verifica que existe `03-drafts/_STAGE_COMPLETE` antes de continuar.
Lee `agents/agente-editor-estrategico.md`.
Lee los drafts de `03-drafts/` y los briefings de `02-briefings/`.
Genera los artículos editados en `04-edited/` y el archivo `04-edited/edited-index.json`.
Actualiza `run-manifest.json`.
Crea `04-edited/_STAGE_COMPLETE`.
Actualiza `outputs/current-run.json` → next_agent: supervisor-final.

PASO 5 — SUPERVISOR FINAL
Verifica que existe `04-edited/_STAGE_COMPLETE` antes de continuar.
Lee `agents/supervisor-final.md`.
Lee los artículos de `04-edited/`.
Genera los aprobados finales en `05-wordpress-ready/` y el archivo `05-wordpress-ready/wordpress-ready-index.json`.
Actualiza `run-manifest.json`.
Crea `05-wordpress-ready/_STAGE_COMPLETE`.

PASO 6 — WORDPRESS DRAFTS
Solo ejecuta este paso si el Supervisor Final devuelve:

ESTADO_SUPERVISION_FINAL: CREAR_WORDPRESS_DRAFT

y:

WORDPRESS_ACTION:
  create_draft: true
  publish: false

Para cada artículo aprobado en `05-wordpress-ready/`, crea un borrador en WordPress usando la REST API con las variables de entorno WP_URL, WP_USER y WP_APP_PASSWORD:

```bash
curl -s -X POST "$WP_URL/wp-json/wp/v2/posts" \
  -u "$WP_USER:$WP_APP_PASSWORD" \
  -H "Content-Type: application/json" \
  -d '{
    "title": "TÍTULO_DEL_ARTÍCULO",
    "content": "CONTENIDO_HTML_DEL_ARTÍCULO",
    "status": "draft"
  }'
```

Extrae el `id` y el `link` de la respuesta JSON y regístralos en `run-manifest.json`.

Si el Supervisor Final NO devuelve CREAR_WORDPRESS_DRAFT, detente aquí y registra el motivo en el manifest.

PASO 7 — ACTUALIZAR MEMORIA Y COMMIT
Añade a `memory/articulos_publicados.json` cada artículo enviado a WordPress Draft en este run (título, slug, categoría, palabras clave, fecha, estado: "wordpress_draft").
Ejecuta los siguientes comandos git:
  git add memory/articulos_publicados.json
  git add outputs/runs/[RUN_ID]/
  git commit -m "run: [RUN_ID] — [N] borradores creados en WordPress"
  git push origin HEAD

REGLAS ABSOLUTAS:
- publish: false siempre. Solo create_draft: true. Nunca publicar directamente.
- No continuar al siguiente paso si falta el _STAGE_COMPLETE del paso anterior.
- No leer ni escribir en carpetas de ejecuciones anteriores.
- No modificar articulos_publicados.json con artículos que no hayan llegado a WordPress Draft.
```

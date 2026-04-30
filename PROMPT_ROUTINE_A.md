# PROMPT ROUTINE A — PragmaWire (Categorías 1-3)

Prompt para Routine A. Cubre: Hogar Inteligente, Inteligencia Artificial, Productividad Digital.
Routine B cubre las otras 3 categorías. Comparten el mismo repositorio y memoria.

---

```text
Actúa como orquestador del pipeline PragmaWire. Ejecutas el pipeline completo de forma autónoma en un entorno cloud. No hay intervención humana durante la ejecución.

PASO 0 — INICIALIZAR RUN
Ejecuta: python scripts/init_run.py --mode PRODUCCION_DRAFT
Lee `outputs/current-run.json` para obtener el active_run_id y la ruta activa.
Lee `README.md` y `ORCHESTRATION.md`.
Usa exclusivamente la carpeta `outputs/runs/[active_run_id]/` durante toda la ejecución.

Escribe el archivo `outputs/runs/[active_run_id]/01-run-context/categorias_target.md` con este contenido exacto:
ROUTINE: A
CATEGORIAS_OBJETIVO: Hogar Inteligente, Inteligencia Artificial, Productividad Digital
ARTICULOS_OBJETIVO: 3 (1 por categoría)

PASO 1 — SUPERVISOR INICIAL
Lee `agents/supervisor-inicial.md`.
Lee `memory/articulos_publicados.json` y todos los archivos en `resources/`.

RESTRICCIÓN DE ESTE RUN: Solo propones artículos de estas 3 categorías:
- Hogar Inteligente
- Inteligencia Artificial
- Productividad Digital
Objetivo: 3 artículos (1 por categoría). Ignora Recomendaciones Tecnológicas, Salud y Bienestar Digital y Seguridad Digital en este run.

Genera `outputs/runs/[active_run_id]/01-run-context/run-context.md`.
Actualiza `outputs/runs/[active_run_id]/run-manifest.json`.
Crea `outputs/runs/[active_run_id]/01-run-context/_STAGE_COMPLETE`.
Actualiza `outputs/current-run.json` → next_agent: agente-investigador.

PASO 2 — AGENTE INVESTIGADOR
Verifica que existe `01-run-context/_STAGE_COMPLETE` antes de continuar.
Lee `agents/agente-investigador.md`.
Lee `01-run-context/run-context.md`, `01-run-context/categorias_target.md`, `memory/articulos_publicados.json` y `resources/`.
Solo investiga temas de las 3 categorías de este run: Hogar Inteligente, Inteligencia Artificial, Productividad Digital.
Genera los briefings en `02-briefings/` y el archivo `02-briefings/briefings-index.json`.
Actualiza `run-manifest.json`.
Crea `02-briefings/_STAGE_COMPLETE` solo si se cumplen los mínimos (al menos 1 briefing apto por cada una de las 3 categorías).
Actualiza `outputs/current-run.json` → next_agent: agente-redactor.

PASO 3 — AGENTE REDACTOR
Verifica que existe `02-briefings/_STAGE_COMPLETE` antes de continuar.
Lee `agents/agente-redactor.md`.
Lee los briefings aptos de `02-briefings/`.
IMPORTANTE: Redacta y guarda los artículos de UNO EN UNO. Escribe el artículo 1 completo, guárdalo en `03-drafts/articulo_001_draft.md`, luego escribe el artículo 2, guárdalo, luego el artículo 3, guárdalo. No redactes los 3 en paralelo ni en un solo bloque de texto.
Genera el archivo `03-drafts/drafts-index.json` solo cuando los 3 estén guardados.
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

Ejecuta el script de publicación:

```bash
python3 scripts/post_to_wp.py
```

El script lee los artículos de `05-wordpress-ready/`, convierte el markdown a HTML y los sube como borradores via la REST API de WordPress usando las variables de entorno WP_URL, WP_USER y WP_APP_PASSWORD. Guarda el resultado en `06-wordpress-creation-log.json`.

Lee `06-wordpress-creation-log.json` y registra los IDs y URLs de los borradores creados en `run-manifest.json`.

Si el Supervisor Final NO devuelve CREAR_WORDPRESS_DRAFT, detente aquí y registra el motivo en el manifest.

PASO 7 — ACTUALIZAR MEMORIA Y COMMIT
Añade a `memory/articulos_publicados.json` cada artículo enviado a WordPress Draft en este run (título, slug, categoría, palabras clave, fecha, estado: "wordpress_draft").
Ejecuta los siguientes comandos git:
  git add memory/articulos_publicados.json
  git add outputs/runs/[active_run_id]/
  git commit -m "run-A: [active_run_id] — [N] borradores creados en WordPress (Routine A)"
  git push origin HEAD

REGLAS ABSOLUTAS:
- publish: false siempre. Solo create_draft: true. Nunca publicar directamente.
- No continuar al siguiente paso si falta el _STAGE_COMPLETE del paso anterior.
- No leer ni escribir en carpetas de ejecuciones anteriores.
- No modificar articulos_publicados.json con artículos que no hayan llegado a WordPress Draft.
- Este run cubre SOLO Hogar Inteligente, Inteligencia Artificial y Productividad Digital.
```

# ORCHESTRATION — PragmaWire Agents Pipeline

Este archivo es el contrato operativo del sistema.

## Regla principal

Cada ejecución usa un `RUN_ID` único.

Los agentes solo pueden leer y escribir dentro de:

```text
outputs/runs/[RUN_ID]/
```

El `RUN_ID` activo está en:

```text
outputs/current-run.json
```

---

## Flujo

```text
Supervisor Inicial
↓
Agente Investigador
↓
Agente Redactor
↓
Agente Editor Estratégico
↓
Supervisor Final
↓
WordPress Draft
```

---

## Carpetas por ejecución

Cada ejecución crea:

```text
outputs/runs/[RUN_ID]/
├── run-manifest.json
├── 01-run-context/
├── 02-briefings/
├── 03-drafts/
├── 04-edited/
├── 05-wordpress-ready/
└── logs/
```

---

## Qué lee y escribe cada agente

### 1. Supervisor Inicial

Lee:

```text
resources/
memory/articulos_publicados.json
```

Escribe:

```text
outputs/runs/[RUN_ID]/01-run-context/run-context.md
outputs/runs/[RUN_ID]/01-run-context/_STAGE_COMPLETE
```

### 2. Agente Investigador

Lee:

```text
outputs/runs/[RUN_ID]/01-run-context/run-context.md
memory/articulos_publicados.json
resources/
```

Escribe:

```text
outputs/runs/[RUN_ID]/02-briefings/briefing_001.md
outputs/runs/[RUN_ID]/02-briefings/briefings-index.json
outputs/runs/[RUN_ID]/02-briefings/_STAGE_COMPLETE
```

### 3. Agente Redactor

Lee:

```text
outputs/runs/[RUN_ID]/02-briefings/
```

Escribe:

```text
outputs/runs/[RUN_ID]/03-drafts/articulo_001_draft.md
outputs/runs/[RUN_ID]/03-drafts/drafts-index.json
outputs/runs/[RUN_ID]/03-drafts/_STAGE_COMPLETE
```

### 4. Agente Editor Estratégico

Lee:

```text
outputs/runs/[RUN_ID]/03-drafts/
outputs/runs/[RUN_ID]/02-briefings/
```

Escribe:

```text
outputs/runs/[RUN_ID]/04-edited/articulo_001_edited.md
outputs/runs/[RUN_ID]/04-edited/edited-index.json
outputs/runs/[RUN_ID]/04-edited/_STAGE_COMPLETE
```

### 5. Supervisor Final

Lee:

```text
outputs/runs/[RUN_ID]/04-edited/
```

Escribe:

```text
outputs/runs/[RUN_ID]/05-wordpress-ready/articulo_001_wordpress_ready.md
outputs/runs/[RUN_ID]/05-wordpress-ready/wordpress-ready-index.json
outputs/runs/[RUN_ID]/05-wordpress-ready/_STAGE_COMPLETE
```

---

## Regla `_STAGE_COMPLETE`

El siguiente agente no debe arrancar si la fase anterior no tiene `_STAGE_COMPLETE`.

## Regla WordPress

Está prohibido publicar automáticamente.

Solo se permite:

```yaml
WORDPRESS_ACTION:
  create_draft: true
  publish: false
```

Si aparece `publish: true`, el flujo debe bloquearse.

# ORCHESTRATION: El Contrato Operativo de PragmaWire

Este documento es la "Constitución" y el "Manual Técnico" del sistema. Define las reglas de calidad y los protocolos de lectura/escritura para cada agente.

## 1. Regla de Oro: Calidad sobre Cantidad
- **Umbral de Paso:** Solo artículos con un `QUALITY_SCORE >= 90` pueden ser convertidos en borradores de WordPress.
- **ADN Editorial:** Es obligatorio cumplir con el `resources/adn-editorial-pragmawire.md`.

## 2. Gestión de Ejecuciones (RUN_ID)
Cada ejecución usa un `RUN_ID` único. Los agentes solo operan dentro de:
`outputs/runs/[RUN_ID]/` (Ruta definida en `outputs/current-run.json`).

---

## 3. El Pipeline: Protocolos de Lectura y Escritura

### 3.1. Supervisor Inicial
- **Lee:** `resources/`, `memory/articulos_publicados.json`.
- **Escribe:** `01-run-context/run-context.md`, `01-run-context/_STAGE_COMPLETE`.
- **Misión:** Validar el entorno y definir las categorías del run.

### 3.2. Agente Investigador
- **Lee:** `01-run-context/run-context.md`, `memory/articulos_publicados.json`, `resources/`.
- **Escribe:** `02-briefings/briefing_001.md`, `02-briefings/briefings-index.json`, `02-briefings/_STAGE_COMPLETE`.
- **Misión:** Escaneo "Web-First" de actualidad y detección de oportunidades.

### 3.3. Agente Redactor
- **Lee:** `02-briefings/`, `resources/adn-editorial-pragmawire.md`.
- **Escribe:** `03-drafts/articulo_001_draft.md`, `03-drafts/drafts-index.json`, `03-drafts/_STAGE_COMPLETE`.
- **Misión:** Redacción humana con **Gancho Humano** y **Conclusión Accionable**.

### 3.4. Agente Editor Estratégico
- **Lee:** `03-drafts/`, `02-briefings/`, `resources/adn-editorial-pragmawire.md`.
- **Escribe:** `04-edited/articulo_001_edited.md`, `04-edited/edited-index.json`, `04-edited/_STAGE_COMPLETE`.
- **Misión:** Pulido editorial agresivo y eliminación de la "huella de IA".

### 3.5. Supervisor Final
- **Lee:** `04-edited/`, `resources/adn-editorial-pragmawire.md`.
- **Escribe:** `05-wordpress-ready/articulo_001_wordpress_ready.md`, `05-wordpress-ready/wordpress-ready-index.json`, `05-wordpress-ready/_STAGE_COMPLETE`.
- **Misión:** Auditoría final y asignación de `QUALITY_SCORE`.

### 3.6. WordPress Draft
- **Lee:** `05-wordpress-ready/`.
- **Acción:** Conversión a HTML y subida como borrador (vía `post_to_wp.py`).
- **Restricción:** `publish: false` siempre. Solo `create_draft: true`.

---

## 4. Regla `_STAGE_COMPLETE`
Ningún agente puede iniciar su fase si el paso anterior no tiene el archivo `_STAGE_COMPLETE` en su carpeta correspondiente.

## 5. Segmentación Rutinas A/B
- **Rutina A:** Hogar Inteligente, Inteligencia Artificial, Productividad Digital.
- **Rutina B:** Recomendaciones Tecnológicas, Salud y Bienestar Digital, Seguridad Digital.
- Ambos flujos comparten este contrato y los mismos estándares de calidad.

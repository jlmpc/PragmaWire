# CLAUDE.md — Memoria de Proyecto PragmaWire

> Este fichero es la fuente de verdad para nuevas sesiones de Claude Code.
> Léelo completo antes de hacer cualquier cambio al proyecto.

---

## Qué es PragmaWire

Blog de tecnología práctica para personas de a pie. Explica tecnología útil con voz cercana, experta y empática. El pipeline multiagente genera artículos optimizados para lectores humanos, SEO, AEO (Answer Engine), GEO/IA y E-E-A-T.

**URL:** pragmawire.com  
**Rama de desarrollo:** `claude/analyze-repository-5C67c`  
**Repositorio:** `jlmpc/PragmaWire`

---

## Arquitectura del pipeline

```
Supervisor Inicial
↓  (genera RUN_CONTEXT + instrucción al investigador)
Agente Investigador
↓  (genera briefings con fuente origen real)
Agente Redactor
↓  (genera artículos draft)
Agente Editor Estratégico
↓  (audita, optimiza, empaqueta WORDPRESS_DRAFT)
Supervisor Final
↓  (valida y actualiza memoria)
post_to_wp.py
↓  (publica borradores en WordPress via REST API)
WordPress Draft (revisión humana obligatoria)
```

**Regla absoluta:** El pipeline NUNCA publica automáticamente. Destino máximo: `WORDPRESS_DRAFT`.

---

## Modelo de ejecución actual (post-refactor)

### Rutinas A y B

El pipeline se ejecuta en dos rutinas alternadas:

| Rutina | Categorías |
|--------|-----------|
| A | Hogar Inteligente, Inteligencia Artificial, Productividad Digital |
| B | Recomendaciones Tecnológicas, Salud y Bienestar Digital, Seguridad Digital |

**Objetivo por run:** 1 artículo por categoría activa = **3 artículos por run**.  
**Mínimo obligatorio:** 1 artículo apto por cada categoría activa del run.  
**El README y agents/README están desactualizados** — todavía dicen "12 artículos" (modelo antiguo). No tomar como referencia.

### Metodología SOURCE-FIRST

Cada briefing DEBE estar anclado a un artículo real publicado en las últimas 48h por la competencia. Sin URL real verificada con WebFetch (via Jina Reader), el briefing es inválido.

### Jina Reader

Todas las webs de la competencia usan JavaScript y no devuelven contenido con WebFetch directo. Se usa Jina Reader como proxy:

```
WebFetch("https://r.jina.ai/[URL]")
```

Jina Reader está en `allowedDomains` en `.claude/settings.json`. No requiere API key.

### Sistema de scoring (11 criterios, umbral 70)

Unificado en supervisor-inicial.md y agente-investigador.md:

1. Relevancia a la categoría: 0-10
2. Potencial de ángulo PragmaWire: 0-10
3. Utilidad para el lector: 0-15
4. Frescura o actualidad: 0-15
5. Oportunidad SEO: 0-10
6. Oportunidad AEO: 0-10
7. Oportunidad GEO / IA: 0-10
8. Claridad de intención de búsqueda: 0-5
9. Facilidad de verificación: 0-5
10. Encaje con PragmaWire: 0-5
11. Potencial de enlaces internos: 0-5

**Umbral mínimo:** 70 puntos. Por debajo: descartar.

---

## Estado de cada agente — qué se ha revisado y cambiado

### ✅ supervisor-inicial.md — REVISADO Y CERRADO

**Cambios realizados en esta sesión:**
- Reemplazadas referencias a "WordPress MCP" y "Firecrawl" por "WordPress REST API" y "WebFetch + Jina Reader".
- REGLAS DE BLOQUEO: eliminada referencia a "WordPress MCP" (bug residual en ejemplos de PIPELINE_BLOCKED).
- PRINCIPIO DE CALIDAD: eliminadas referencias a Reddit/LinkedIn/Twitter/HN como fuentes (contradecían la metodología source-first).
- SCORING DE TEMAS: actualizado de 10 criterios (umbral 75) a 11 criterios (umbral 70) — sistema unificado con el investigador.
- CRITERIOS DE CALIDAD: separados en dos bloques: Vetos editoriales (descarte absoluto independiente del score) + referencia al scoring.
- TEMAS PROHIBIDOS: sección eliminada — sus 4 ítems únicos absorbidos en los Vetos editoriales. Una sola lista autoritativa.
- FUENTES Y HERRAMIENTAS: simplificado, referencia a `fuentes-por-categoria.md`.
- RUN_CONTEXT YAML: reescrito — `target_articles_per_run: 3`, `pipeline_routine: A|B`, `research_methodology: source_first`, `minimum_topic_score: 70`.
- VALIDACIONES EDITORIALES INICIALES: eliminada lista de 19 ítems redundantes con el YAML; reemplazada por verificación de coherencia.
- INSTRUCCIÓN COMPLETA PARA INVESTIGADOR: reescrita con 6 pasos source-first.
- INSTRUCCION_PARA_AGENTE_INVESTIGADOR en formato de salida: deja de pedir generar la instrucción desde cero; referencia la plantilla INSTRUCCIÓN COMPLETA.

### ✅ agente-investigador.md — REVISADO Y CERRADO

**Cambios realizados en esta sesión:**
- **PASO 0 OBLIGATORIO** añadido: leer `adn-editorial-pragmawire.md` antes de rastrear ninguna fuente. El ángulo PragmaWire del briefing debe basarse en el ADN editorial, no en intuición de entrenamiento.
- **Fases reordenadas**: FASE 2A (rastreo) → FASE 2B (deduplicación) → FASE 2C (puntuación) → FASE 3 (ángulo) → FASE 4 (briefings). Antes la deduplicación venía después del scoring.
- **FASE 2C scoring**: actualizado de 4 criterios (threshold 60) a 11 criterios unificados (threshold 70). Criterio 2 reescrito para que la lógica de escala sea explícita (mayor espacio de diferenciación = más puntos).
- **Objetivo de candidatos**: reemplazado "15-20 candidatos" (arbitrario) por "3-5 por categoría activa" (operativo).
- **Mínimo de palabras**: corregido 900 → 1.000 palabras (alineado con agente-redactor).
- **SEGUNDA_PASADA_ACTIVA**: nombre unificado (antes: VENTANA_EXTENDIDA_72H en FASE 2A, SEGUNDA_PASADA_ACTIVA en sección separada).
- **Campo `## Lo que el Redactor NO debe copiar`**: añadido a la plantilla de briefing (estructura, ángulo, ejemplos, inicio del artículo origen). FASE 3 lo definía pero no había campo en la plantilla.
- **briefings-index.json**: añadidos campos `run_id` y `pipeline_routine` para trazabilidad.
- **CANDIDATOS_DESCARTADOS**: columna `Tipo_Descarte` (DUPLICADO / VETO_EDITORIAL / SCORE_BAJO / FUERA_VENTANA_TEMPORAL / SIN_URL_VERIFICADA) reemplaza la columna genérica "Motivo".
- **Longitud de artículos**: instrucción para capturar la longitud cuando se hace WebFetch individual de verificación de fecha (única oportunidad sin fetch extra).

### ✅ agente-redactor.md — REVISADO Y CERRADO

**Cambios de sesiones anteriores:**
- PASO 0 (ADN editorial). Reglas de diferenciación (3). Auto-auditoría. AUDITORIA_DIFERENCIACION. CHECKLIST ampliado. 3 truncaciones corregidas.

**Cambios de esta sesión:**
- **PASO 0 ampliado**: lectura obligatoria de `expertise-seo-aeo-geo-copywriting.md` además del ADN editorial.
- **REGLAS TÉCNICAS DE ESCRITURA** (nueva sección con 8 reglas basadas en investigación primaria 2024-2026): bloque 40-60 palabras por H2, párrafos ≤90 palabras, visual break cada 70 palabras, estadísticas obligatorias, citas directas con atribución, fuentes en texto con enlace, idea importante primero en cada párrafo, eliminación de marcadores de IA.
- **SEO/AEO/GEO/E-E-A-T**: 4 secciones extensas comprimidas en 1 concisa. El Redactor escribe bien para humanos; el Editor hace la optimización técnica.
- **Nota sobre metadata**: FAQ, imagen y frase citable son sugerencias para el Editor, no outputs definitivos.
- **CHECKLIST_REDACCION**: completamente rehecho con todos los parámetros técnicos nuevos.

### ✅ agente-editor-estrategico.md — REVISADO Y CERRADO

**Cambios de sesiones anteriores:**
- Veto 8 reforzado. Campo `AUDITORIA_DIFERENCIACION` añadido.

**Cambios de esta sesión:**
- **3 bugs de truncación corregidos**: ROL, CONTEXTO y CUÁNDO CORREGIR estaban cortados con contenido fundido entre secciones.
- **PASO 0 OBLIGATORIO**: leer `expertise-seo-aeo-geo-copywriting.md` antes de auditar.
- **ROL redefinido con 3 dimensiones**: auditoría editorial / metadata exclusiva / correcciones quirúrgicas.
- **Regla absoluta de no-reescritura del cuerpo**: si el cuerpo necesita reescritura → DEVOLVER_A_REDACTOR con feedback concreto.
- **CUÁNDO CORREGIR DIRECTAMENTE**: redefinido como correcciones quirúrgicas a escala de oración/párrafo. Metadata como dominio exclusivo del Editor.
- **CUÁNDO DEVOLVER AL REDACTOR**: criterios concretos de cuándo el problema requiere reescritura.
- **GEO/GXO scoring**: actualizado con criterios evidenciados (bloques 40-60 palabras, estadísticas, citas directas, AI summary, quotable sentence).
- **FINAL_CHECKLIST ampliado**: parámetros técnicos reales de la investigación.

### ✅ supervisor-final.md — PARCIALMENTE REVISADO

**Cambios realizados en esta sesión:**
- **ACTUALIZACIÓN OBLIGATORIA DE MEMORIA**: nuevo protocolo cuando emite `CREAR_WORDPRESS_DRAFT` — leer, actualizar y verificar `memory/articulos_publicados.json` antes de terminar.
- **Campo `MEMORIA_ACTUALIZADA`**: añadido al formato de salida FORMATO A.

**PENDIENTE DE AUDITORÍA COMPLETA**: No se ha hecho la misma pasada exhaustiva.

---

## Estado de scripts

### ✅ scripts/post_to_wp.py — REVISADO

**Cambios críticos:**
- **`update_memory()`**: actualiza `memory/articulos_publicados.json` tras cada publicación exitosa. Para slugs existentes: actualiza wp_id, wp_link, estado. Para nuevos: añade entrada completa.
- **`update_run_history()`**: crea/actualiza `memory/run-history.json` con resumen del run.
- **`main()`**: captura `meta` de `parse_article()`, construye `memory_updates`, llama a ambas funciones tras publicar (con try/except para no romper si falla).

**Antes de este cambio:** `articulos_publicados.json` NUNCA se actualizaba automáticamente tras las publicaciones. Bug crítico de deduplicación.

---

## Archivos de referencia clave

| Fichero | Función |
|---------|---------|
| `resources/adn-editorial-pragmawire.md` | Voz, tono, Gancho Humano, anti-patrones de IA. **Lectura obligatoria para investigador, redactor y editor** |
| `resources/expertise-seo-aeo-geo-copywriting.md` | Mejores prácticas reales 2024-2026: SEO, AEO, GEO/GXO, copywriting. **Lectura obligatoria para redactor y editor** |
| `resources/fuentes-por-categoria.md` | Fuentes primarias y secundarias por categoría. Base de la metodología source-first |
| `resources/categorias.md` | Definición de las 6 categorías editoriales |
| `memory/articulos_publicados.json` | Registro de artículos publicados/en borrador. Base de deduplicación |
| `memory/run-history.json` | Historial de runs (creado por post_to_wp.py) |
| `outputs/current-run.json` | Run activo actual |

---

## Herramientas del pipeline

| Herramienta | Uso | Notas |
|-------------|-----|-------|
| **Jina Reader** | Rastreo de fuentes de la competencia | `https://r.jina.ai/[URL]` — ya en allowedDomains |
| **WebSearch** | Apoyo: verificar fechas, datos adicionales | No como fuente primaria |
| **Google Trends** | Apoyo: desempate entre candidatos con score similar | No como fuente primaria |
| **WordPress REST API** | Publicación de borradores | vars: WP_URL, WP_USER, WP_APP_PASSWORD |
| **Firecrawl** | ~~Rastreo~~ — **ELIMINADO** | Requería API key + MCP setup. Reemplazado por Jina Reader |

---

## Próximos pasos (pendiente al limpiar conversación)

1. **Auditoría completa de `supervisor-final.md`** — mismos criterios que supervisor-inicial e investigador.
2. **Actualizar README.md y agents/README.md** — todavía dicen "12 artículos por run" (modelo antiguo). Corregir a 3 artículos por run, Rutinas A/B.

---

## Criterios de auditoría usados (para aplicar en próximas pasadas)

Estos son los criterios con los que se revisaron supervisor-inicial e investigador. Aplicar exactamente los mismos a los agentes pendientes:

1. **Bugs** — residuales de versiones anteriores, referencias a herramientas eliminadas (Firecrawl, WordPress MCP), nombres inconsistentes entre secciones del mismo fichero.
2. **Contradicciones internas** — dos secciones del mismo fichero diciendo cosas opuestas al mismo agente.
3. **Campos sin destino** — el agente define algo en una fase pero no tiene campo en la plantilla de output donde registrarlo.
4. **Escala confusa en criterios** — cuando la lógica de puntuación es contraintuitiva sin explicación.
5. **Números arbitrarios** — objetivos de cantidad sin relación con el mínimo funcional real.
6. **Redundancia** — secciones que repiten lo que ya dice otra sección del mismo fichero.
7. **Missing pieces** — lecturas obligatorias que el agente debería hacer y no hace (ej: ADN editorial).
8. **Inconsistencias inter-agente** — campos definidos en un agente con valores distintos en otro (ej: mínimo de palabras 900 vs 1000).

---

## Convenciones de código del pipeline

- Todos los outputs se guardan en `outputs/runs/[active_run_id]/`.
- El handoff entre agentes se señaliza con `_STAGE_COMPLETE` (fichero vacío en la carpeta de la fase).
- Cada agente actualiza `run-manifest.json` y `current-run.json` al terminar.
- Los briefings se numeran `briefing_001.md`, `briefing_002.md`, etc.
- Los artículos draft se numeran `articulo_001_draft.md`, etc.
- Los artículos WordPress-ready van a `05-wordpress-ready/`.
- El log de publicación WP es `06-wordpress-creation-log.json`.

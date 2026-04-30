# Run Context — PragmaWire Pipeline
## Run ID: 2026-04-30T1142_pragmawire_3af4

---

### ESTADO_PIPELINE

`PIPELINE_READY_WITH_WARNINGS`

---

### MOTIVO

El pipeline puede arrancar. Las herramientas de búsqueda web (WebSearch, WebFetch) están disponibles para investigación en español e inglés. La memoria `articulos_publicados.json` es legible. El sistema de guardado de outputs está operativo. WordPress se gestiona vía REST API con script `post_to_wp.py`, no vía MCP dedicado (advertencia no crítica). No hay herramienta nativa de Google Trends pero se puede acceder mediante búsqueda web. El destino confirmado es `WORDPRESS_DRAFT` con `publish: false`.

---

### RESTRICCIÓN DE CATEGORÍAS (ACTIVA)

Archivo `categorias_target.md` detectado. Restricción vinculante:

- **ROUTINE:** A
- **CATEGORIAS_OBJETIVO:** Hogar Inteligente, Inteligencia Artificial, Productividad Digital
- **ARTICULOS_OBJETIVO:** 3 (1 por categoría)
- Las categorías Recomendaciones Tecnológicas, Salud y Bienestar Digital y Seguridad Digital quedan excluidas de este run.

---

### VALIDACIONES_TECNICAS

- WordPress MCP: WARNING (no hay MCP WordPress; se usa script REST API post_to_wp.py con variables WP_URL, WP_USER, WP_APP_PASSWORD)
- Firecrawl o búsqueda: OK (WebSearch y WebFetch disponibles)
- Google Trends o tendencias: WARNING (no hay acceso directo a Google Trends; se usa WebSearch para detectar tendencias)
- Scraping/análisis de competencia: OK (WebFetch disponible para leer webs de referencia)
- Fuentes ES/EN disponibles: OK
- Memoria local: OK (articulos_publicados.json legible)
- articulos_publicados.json: OK (1 artículo de ejemplo en Seguridad Digital)
- Categorías editoriales: OK
- Sistema de guardado de outputs: OK
- Destino WordPress Draft: OK (publish_allowed: false confirmado)

---

### VALIDACIONES_EDITORIALES

- Categorías objetivo definidas: OK (3 categorías activas este run)
- Cobertura mínima por categoría definida: OK (mínimo 1 por categoría activa)
- Reglas de deduplicación definidas: OK
- Scoring mínimo definido: OK (≥75)
- Fuentes permitidas definidas: OK
- Fuentes en español e inglés definidas: OK
- Criterios de frescura definidos: OK
- Condiciones de parada definidas: OK
- Prohibición de publicación automática: OK

---

### RUN_CONTEXT

```yaml
run_id: 2026-04-30T1142_pragmawire_3af4
execution_date: 2026-04-30
execution_mode: PRODUCCION_DRAFT
routine: A

# Restricción activa desde categorias_target.md
target_articles: 3
minimum_articles: 3
minimum_per_category: 1
target_per_category: 1
quality_over_quantity: true
wordpress_destination: WORDPRESS_DRAFT
publish_allowed: false

active_categories:
  - Hogar Inteligente
  - Inteligencia Artificial
  - Productividad Digital

excluded_categories_this_run:
  - Recomendaciones Tecnológicas
  - Salud y Bienestar Digital
  - Seguridad Digital

category_distribution_target:
  Hogar Inteligente: 1
  Inteligencia Artificial: 1
  Productividad Digital: 1

category_distribution_minimum:
  Hogar Inteligente: 1
  Inteligencia Artificial: 1
  Productividad Digital: 1

minimum_topic_score: 75

accepted_topic_statuses:
  - NUEVO
  - EXISTE_ANGULO_DIFERENTE

rejected_topic_statuses:
  - EXISTE_IDENTICO

review_topic_statuses:
  - EXISTE_SIMILAR

required_search_intent:
  - informational
  - commercial_investigation
  - practical_how_to
  - explainer

required_source_quality:
  - official_sources_when_available
  - reputable_tech_media
  - recent_sources_for_high_freshness_topics
  - no_unverified_claims
  - sources_in_spanish_and_english

research_languages:
  - Spanish
  - English

research_sources_required:
  trends:
    - Google Trends (vía WebSearch)
    - related_searches
    - social_trends_when_relevant
  spanish_media:
    - Xataka
    - Genbeta
    - Applesfera
    - Computer Hoy
    - Hipertextual
  english_media:
    - The Verge
    - TechCrunch
    - Wired
    - Ars Technica
    - VentureBeat
    - Engadget
  communities:
    - Reddit
    - Hacker News
    - LinkedIn
  official_sources:
    - product_documentation
    - official_blogs
    - support_pages

freshness_rules:
  low: evergreen_content
  medium: verify_recent_changes
  high: requires_recent_sources_and_explicit_verification

deduplication_rules:
  compare_slug: true
  compare_primary_keyword: true
  compare_secondary_keywords: true
  compare_topic_angle: true
  compare_search_intent: true
  compare_existing_articles: true
  compare_main_entities: true

forbidden_topics:
  - rumours_without_sources
  - medical_claims_without_authoritative_sources
  - financial_promises
  - cybersecurity_claims_without_verification
  - clickbait
  - generic_articles_without_practical_value
  - product_recommendations_without_verifiable_data
  - copied_competitor_angles_without_original_value

output_required:
  format: briefing_markdown
  count: 3
  target_count: 3
  minimum_count: 3
  require_minimum_one_per_category: true
  allow_less_than_target_if_quality_low: false
  require_second_research_pass_if_less_than_target: true
  include_topic_score: true
  include_deduplication_status: true
  include_sources: true
  include_source_language: true
  include_pending_verification: true
  include_internal_linking_opportunities: true

stop_conditions:
  - missing_critical_infrastructure
  - cannot_verify_duplicates
  - cannot_save_outputs
  - wordpress_destination_is_not_draft
  - any_category_without_valid_topic_after_expansion
  - high_risk_unverifiable_topics_only
```

---

### WARNINGS

1. WordPress no está disponible vía MCP dedicado; se usa el script `post_to_wp.py` con variables de entorno. Verificar que WP_URL, WP_USER y WP_APP_PASSWORD estén configuradas antes del PASO 6.
2. Google Trends no está disponible directamente; la detección de tendencias se apoya en WebSearch. El Investigador debe compensar con análisis de búsquedas relacionadas y medios de referencia.
3. `articulos_publicados.json` tiene solo 1 artículo de ejemplo (Seguridad Digital). El enlazado interno será limitado en este run. Sin impacto en las 3 categorías activas.

---

### NEXT_AGENT

`Agente Investigador`

---

### INSTRUCCION_PARA_AGENTE_INVESTIGADOR

> Busca y valida temas para PragmaWire.com siguiendo estrictamente el RUN_CONTEXT y el archivo `01-run-context/categorias_target.md`. El objetivo es conseguir **1 tema apto por cada una de las 3 categorías activas de este run** (mínimo obligatorio también de 1 por categoría). No rellenes con temas mediocres: si no llegas al objetivo en la primera pasada, amplía fuentes, idiomas, tendencias y competencia antes de cerrar la tanda.

**Categorías activas este run (ÚNICAS a investigar):**
1. Hogar Inteligente
2. Inteligencia Artificial
3. Productividad Digital

**NO investigues:** Recomendaciones Tecnológicas, Salud y Bienestar Digital, Seguridad Digital.

**Objetivo:** 3 briefings APTOS, 1 por categoría. Score mínimo: 75/100.

**Para cada tema entrega un briefing con los 31 campos estándar del pipeline.**

**Si tras la primera pasada falta alguna categoría, realiza una segunda pasada obligatoria ampliando fuentes antes de cerrar.**

---

### STOP_CONDITIONS

- No hay acceso a búsqueda web (crítico)
- No se puede leer articulos_publicados.json (crítico)
- No se puede guardar outputs (crítico)
- El destino no es WORDPRESS_DRAFT (crítico)
- Alguna categoría activa queda sin ningún tema apto tras ampliar búsqueda
- Solo hay temas de alto riesgo o no verificables

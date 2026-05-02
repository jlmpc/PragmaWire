# Run Context — PragmaWire Pipeline

## ESTADO_PIPELINE

`PIPELINE_READY_WITH_WARNINGS`

## MOTIVO

El pipeline puede arrancar en modo PRODUCCION_DRAFT. La búsqueda web está disponible como herramienta principal de investigación. La memoria de artículos publicados es accesible y los recursos editoriales están completos. WordPress se gestiona vía script `post_to_wp.py` con credenciales en variables de entorno. Se advierte que la memoria de artículos publicados contiene un único artículo de ejemplo (Seguridad Digital), lo que limita el enlazado interno pero no bloquea el pipeline. Las categorías activas del run están restringidas por `categorias_target.md` a 3 categorías: Hogar Inteligente, Inteligencia Artificial y Productividad Digital.

## RESTRICCION_CATEGORIAS

Este run está restringido por `01-run-context/categorias_target.md`:
- **ROUTINE**: A
- **CATEGORIAS_OBJETIVO**: Hogar Inteligente, Inteligencia Artificial, Productividad Digital
- **ARTICULOS_OBJETIVO**: 3 (1 por categoría)
- Las categorías Recomendaciones Tecnológicas, Salud y Bienestar Digital y Seguridad Digital se ignoran en este run.

## VALIDACIONES_TECNICAS

- WordPress MCP: WARNING (se usa script post_to_wp.py con variables de entorno WP_URL, WP_USER, WP_APP_PASSWORD)
- Búsqueda web (WebSearch): OK
- Google Trends o tendencias: OK (vía WebSearch)
- Scraping/análisis de competencia: OK (vía WebSearch + WebFetch)
- Fuentes ES/EN disponibles: OK
- Memoria local: OK
- articulos_publicados.json: OK (1 artículo de ejemplo en Seguridad Digital)
- Categorías editoriales: OK
- Sistema de guardado de outputs: OK
- Destino WordPress Draft: OK (publish_allowed: false, create_draft: true)

## VALIDACIONES_EDITORIALES

- Categorías objetivo definidas: OK (Hogar Inteligente, Inteligencia Artificial, Productividad Digital)
- Cobertura mínima por categoría definida: OK (1 por categoría activa)
- Reglas de deduplicación definidas: OK
- Scoring mínimo definido: OK (≥75)
- Fuentes permitidas definidas: OK
- Fuentes en español e inglés definidas: OK
- Criterios de frescura definidos: OK
- Condiciones de parada definidas: OK
- Prohibición de publicación automática: OK

## RUN_CONTEXT

```yaml
run_id: 2026-05-02T0102_pragmawire_d056
execution_date: 2026-05-02
execution_mode: PRODUCCION_DRAFT
routine: A

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

ignored_categories_this_run:
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

existing_articles_to_deduplicate:
  - slug: que-son-passkeys
    categoria: Seguridad Digital
    tema: passkeys
    (no es una categoría activa en este run, sin riesgo de duplicado)

forbidden_topics:
  - rumours_without_sources
  - medical_claims_without_authoritative_sources
  - financial_promises
  - cybersecurity_claims_without_verification
  - clickbait
  - generic_articles_without_practical_value
  - product_recommendations_without_verifiable_data

output_required:
  format: briefing_markdown
  count: 3
  target_count: 3
  minimum_count: 3
  require_minimum_one_per_category: true
  include_topic_score: true
  include_deduplication_status: true
  include_sources: true

stop_conditions:
  - cannot_save_outputs
  - wordpress_destination_is_not_draft
  - any_active_category_without_valid_topic_after_expansion
  - high_risk_unverifiable_topics_only
```

## WARNINGS

1. `articulos_publicados.json` contiene solo 1 artículo de ejemplo (estado: "ejemplo"). El enlazado interno en los artículos generados será limitado. El Redactor debe evitar referencias forzadas.
2. WordPress se gestiona vía script externo (`post_to_wp.py`). Las credenciales deben estar disponibles en variables de entorno en el momento de ejecutar el PASO 6.
3. Este run es ROUTINE A: solo 3 categorías y 3 artículos. Las demás categorías se ignoran completamente.

## NEXT_AGENT

`agente-investigador`

## INSTRUCCION_PARA_AGENTE_INVESTIGADOR

Busca y valida temas para PragmaWire.com siguiendo estrictamente el RUN_CONTEXT y el archivo `01-run-context/categorias_target.md`.

**Objetivo**: 3 briefings aptos — 1 por cada categoría activa del run:
1. Hogar Inteligente
2. Inteligencia Artificial
3. Productividad Digital

Mínimo obligatorio: 1 tema apto por categoría. No rellenes con temas mediocres. Si no llegas al objetivo en la primera pasada, amplía fuentes, idiomas, tendencias y competencia antes de cerrar la tanda.

Investiga en español e inglés, usando tendencias (Google Trends vía WebSearch), medios tecnológicos en español (Xataka, Genbeta, Hipertextual), medios en inglés (The Verge, TechCrunch, Wired, Engadget), documentación oficial, comunidades (Reddit, Hacker News) y fuentes especializadas.

Score mínimo aceptable: **75/100**. Descarta temas con score inferior a 75 salvo justificación editorial muy sólida.

No hay artículos previos publicados en las 3 categorías activas (el único artículo en memoria es de Seguridad Digital, que está excluida de este run). Todos los temas para Hogar Inteligente, Inteligencia Artificial y Productividad Digital serán NUEVO por defecto, salvo que el Investigador detecte duplicidad por ángulo editorial idéntico.

Por cada tema entrega un briefing completo con los 31 campos estándar del sistema.

## STOP_CONDITIONS

- Si no es posible guardar outputs en `outputs/runs/2026-05-02T0102_pragmawire_d056/`
- Si el destino WordPress no es DRAFT (publish_allowed: false)
- Si alguna categoría activa no obtiene al menos 1 tema apto tras ampliar búsqueda
- Si solo se encuentran temas de alto riesgo no verificables

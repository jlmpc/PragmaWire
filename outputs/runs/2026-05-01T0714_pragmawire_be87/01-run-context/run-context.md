# Run Context — PragmaWire Pipeline

## ESTADO_PIPELINE

`PIPELINE_READY_WITH_WARNINGS`

## MOTIVO

El pipeline puede arrancar en modo PRODUCCION_DRAFT. La memoria de artículos publicados está disponible (1 artículo de ejemplo). No hay acceso verificado a WordPress MCP en este entorno de ejecución cloud autónomo, pero el script `post_to_wp.py` y las variables de entorno WP_URL/WP_USER/WP_APP_PASSWORD están disponibles para crear borradores. La búsqueda web está disponible. Las 3 categorías objetivo del run están definidas y el sistema de guardado de outputs funciona correctamente. Se advierte que la memoria de artículos publicados es reducida (solo 1 entrada de ejemplo), lo cual es una limitación menor para la deduplicación.

---

## VALIDACIONES_TECNICAS

- WordPress MCP: WARNING (se usará script REST API en lugar de MCP)
- Firecrawl o búsqueda: OK (búsqueda web disponible)
- Google Trends o tendencias: OK (búsqueda web disponible)
- Scraping/análisis de competencia: OK (búsqueda web disponible)
- Fuentes ES/EN disponibles: OK
- Memoria local: OK (articulos_publicados.json accesible)
- articulos_publicados.json: OK (1 entrada disponible)
- Categorías editoriales: OK (definidas en resources/categorias.md)
- Sistema de guardado de outputs: OK
- Destino WordPress Draft: OK (publish_allowed: false)

---

## VALIDACIONES_EDITORIALES

- Categorías objetivo definidas: OK (3 categorías del Routine B)
- Cobertura mínima por categoría definida: OK (1 por categoría)
- Reglas de deduplicación definidas: OK
- Scoring mínimo definido: OK (≥75)
- Fuentes permitidas definidas: OK
- Fuentes en español e inglés definidas: OK
- Criterios de frescura definidos: OK
- Condiciones de parada definidas: OK
- Prohibición de publicación automática: OK

---

## RUN_CONTEXT

```yaml
run_id: 2026-05-01T0714_pragmawire_be87
execution_date: "2026-05-01"
execution_mode: PRODUCCION_DRAFT
routine: B

# RESTRICCIÓN DE CATEGORÍAS — ROUTINE B
target_articles: 3
minimum_articles: 3
minimum_per_category: 1
target_per_category: 1
quality_over_quantity: true
wordpress_destination: WORDPRESS_DRAFT

target_categories:
  - Recomendaciones Tecnológicas
  - Salud y Bienestar Digital
  - Seguridad Digital

# Categorías excluidas de este run (Routine B)
excluded_categories:
  - Hogar Inteligente
  - Inteligencia Artificial
  - Productividad Digital

category_distribution_target:
  Recomendaciones Tecnológicas: 1
  Salud y Bienestar Digital: 1
  Seguridad Digital: 1

category_distribution_minimum:
  Recomendaciones Tecnológicas: 1
  Salud y Bienestar Digital: 1
  Seguridad Digital: 1

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
    - Google Trends
    - related_searches
    - social_trends_when_relevant
  spanish_media:
    - Xataka
    - Genbeta
    - Computer Hoy
    - Hipertextual
  english_media:
    - The Verge
    - TechCrunch
    - Wired
    - Ars Technica
    - VentureBeat
    - Engadget
  security_sources:
    - INCIBE
    - OSI
    - CISA
    - Kaspersky
    - ESET
    - Malwarebytes
    - Krebs on Security
  communities:
    - Reddit
    - Hacker News
    - LinkedIn
    - X/Twitter

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

# Artículos ya publicados (memoria actual)
articulos_publicados:
  - titulo: "Qué son las passkeys y por qué importan"
    slug: que-son-passkeys
    categoria: Seguridad Digital
    palabras_clave: [passkeys, contraseñas, seguridad digital]
    fecha: "2026-04-28"
    estado: ejemplo

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
  allow_less_than_3_if_quality_low: false
  require_second_research_pass_if_less_than_3: true
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
  - fewer_than_3_valid_topics_found
  - any_active_category_without_valid_topic_after_expansion
  - high_risk_unverifiable_topics_only
```

---

## WARNINGS

- La memoria de artículos publicados contiene solo 1 entrada de estado "ejemplo". La deduplicación es posible pero el histórico es muy reducido. El Agente Investigador debe ser especialmente cuidadoso con Seguridad Digital (ya existe un artículo sobre passkeys) y verificar que los nuevos temas no solapan con ese contenido previo.
- No hay verificación directa de acceso a WordPress MCP. Se utilizará el script `post_to_wp.py` con la REST API de WordPress en el Paso 6.

---

## NEXT_AGENT

`Agente Investigador`

---

## INSTRUCCION_PARA_AGENTE_INVESTIGADOR

> Busca y valida temas para PragmaWire.com siguiendo estrictamente el RUN_CONTEXT y el archivo `01-run-context/categorias_target.md`. El objetivo es conseguir 1 tema apto por cada una de las 3 categorías activas de este run (mínimo obligatorio también de 1 por categoría activa). No rellenes con temas mediocres: si no llegas al objetivo en la primera pasada, amplía fuentes, idiomas, tendencias y competencia antes de cerrar la tanda.

**Categorías activas de este run (ROUTINE B):**
1. Recomendaciones Tecnológicas
2. Salud y Bienestar Digital
3. Seguridad Digital

**Categorías excluidas de este run:** Hogar Inteligente, Inteligencia Artificial, Productividad Digital.

**Nota de deduplicación importante:** Ya existe un artículo publicado sobre passkeys (slug: `que-son-passkeys`, categoría: Seguridad Digital). Cualquier tema de Seguridad Digital debe diferenciarse claramente de ese artículo.

**Objetivo:** 3 briefings APTOS (1 por categoría), scoring ≥ 75 por cada uno.

Por cada tema, entrega un briefing completo con los 31 campos definidos en el RUN_CONTEXT. Investiga en español e inglés usando tendencias, medios tecnológicos, fuentes de seguridad (INCIBE, OSI, CISA, Kaspersky, ESET, Krebs on Security), competencia y comunidades.

---

## STOP_CONDITIONS

1. No hay acceso a ningún sistema de búsqueda web.
2. No se puede leer `articulos_publicados.json`.
3. No se pueden guardar outputs en la carpeta del run activo.
4. El destino configurado no es `WORDPRESS_DRAFT`.
5. Hay riesgo de publicación automática.
6. Tras segunda pasada de investigación, alguna categoría activa sigue sin 1 tema apto con score ≥ 75.
7. Solo se encuentran temas de alto riesgo (rumores, afirmaciones no verificables, clickbait).

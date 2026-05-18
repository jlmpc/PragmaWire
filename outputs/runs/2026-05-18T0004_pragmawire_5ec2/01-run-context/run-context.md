# Run Context — PragmaWire Pipeline

## ESTADO_PIPELINE

`PIPELINE_READY_WITH_WARNINGS`

## MOTIVO

El pipeline puede arrancar. Todos los sistemas críticos están operativos: búsqueda web, lectura de memoria, sistema de ficheros y estructura de outputs. El destino WordPress es DRAFT (nunca publicación directa). La única advertencia no crítica es que las credenciales WordPress (WP_URL, WP_USER, WP_APP_PASSWORD) no pueden verificarse en tiempo de inicialización —se comprueban en tiempo de ejecución del script post_to_wp.py. La investigación se limita a 3 categorías (Rutina A) con objetivo de 1 artículo por categoría.

---

## VALIDACIONES_TECNICAS

- WordPress MCP: WARNING (credenciales via env vars, verificables solo en runtime; mecanismo REST API correcto)
- Firecrawl o búsqueda: OK (WebSearch + WebFetch disponibles)
- Google Trends o tendencias: OK (WebSearch puede consultar trends)
- Scraping/análisis de competencia: OK (WebFetch disponible)
- Fuentes ES/EN disponibles: OK
- Memoria local: OK (articulos_publicados.json leído correctamente, 12 artículos registrados)
- articulos_publicados.json: OK
- Categorías editoriales: OK (definidas en categorias_target.md)
- Sistema de guardado de outputs: OK (filesystem local operativo)
- Destino WordPress Draft: OK (publish: false enforced en post_to_wp.py)

---

## VALIDACIONES_EDITORIALES

- Categorías objetivo definidas: OK (Hogar Inteligente, Inteligencia Artificial, Productividad Digital)
- Cobertura mínima por categoría definida: OK (mínimo 1 por categoría activa)
- Reglas de deduplicación definidas: OK
- Scoring mínimo definido: OK (≥75 para apto)
- Fuentes permitidas definidas: OK
- Fuentes en español e inglés definidas: OK
- Criterios de frescura definidos: OK
- Condiciones de parada definidas: OK
- Prohibición de publicación automática: OK (enforce en script y en pipeline)

---

## RESTRICCIÓN DE RUN (RUTINA A)

Este run ejecuta ÚNICAMENTE la Rutina A:
- **Categorías activas:** Hogar Inteligente, Inteligencia Artificial, Productividad Digital
- **Artículos objetivo:** 3 (1 por categoría)
- **Categorías ignoradas:** Recomendaciones Tecnológicas, Salud y Bienestar Digital, Seguridad Digital

---

## RUN_CONTEXT

```yaml
execution_date: "2026-05-18"
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

ignored_categories:
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

articles_already_published_by_active_category:
  Hogar Inteligente:
    - slug: matter-y-thread-guia
      title: "Matter y Thread: qué son y por qué importan antes de comprar un dispositivo inteligente"
      date: "2026-03-30"
  Inteligencia Artificial:
    - slug: 5-trucos-nuevo-muse-spark
      title: "5 trucos gratis con Meta Muse Spark: la nueva IA de Meta que ya supera a ChatGPT"
      date: "2026-04-10"
    - slug: ia-agentica-para-2026
      title: "ChatGPT, Claude o Gemini: cuál usar en 2026 según lo que necesitas"
      date: "2026-04-09"
    - slug: que-es-un-agente-de-ia
      title: "Qué es un agente de IA y cómo configurar uno gratis con ChatGPT, Claude o Gemini"
      date: "2026-04-08"
  Productividad Digital:
    - slug: trampa-apps-productividad
      title: "La trampa de las apps de productividad: cuantas más usas, menos produces"
      date: "2026-04-05"
    - slug: automatizar-tareas-sin-programar
      title: "Cómo automatizar tareas repetitivas sin saber programar: Zapier, Make y n8n explicados"
      date: "2026-04-04"

deduplication_rules:
  compare_slug: true
  compare_primary_keyword: true
  compare_secondary_keywords: true
  compare_topic_angle: true
  compare_search_intent: true
  compare_existing_articles: true
  compare_main_entities: true

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
    - X/Twitter
  official_sources:
    - product_documentation
    - official_blogs
    - support_pages

freshness_rules:
  low: evergreen_content
  medium: verify_recent_changes
  high: requires_recent_sources_and_explicit_verification

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
  - any_category_without_valid_topic_after_expansion
  - high_risk_unverifiable_topics_only
```

---

## WARNINGS

- Las credenciales de WordPress (WP_URL, WP_USER, WP_APP_PASSWORD) no pueden verificarse en tiempo de inicialización. El script post_to_wp.py fallará en PASO 6 si las variables de entorno no están configuradas.
- Inteligencia Artificial tiene 3 artículos publicados recientemente; el Investigador debe encontrar un ángulo claramente diferenciado y evitar repetir la comparación de modelos, los trucos de IA generativa o la explicación básica de agentes.
- Hogar Inteligente solo tiene 1 artículo previo (Matter y Thread), lo que ofrece mayor libertad editorial pero exige que el tema sea suficientemente práctico para usuarios no expertos.

---

## NEXT_AGENT

`Agente Investigador`

---

## INSTRUCCION_PARA_AGENTE_INVESTIGADOR

> Busca y valida temas para PragmaWire.com siguiendo estrictamente el RUN_CONTEXT y el archivo `01-run-context/categorias_target.md`. El objetivo es conseguir 1 tema apto por cada categoría activa del run (mínimo obligatorio también de 1 por categoría activa). No rellenes con temas mediocres: si no llegas al objetivo en la primera pasada, amplía fuentes, idiomas, tendencias y competencia antes de cerrar la tanda.

**Categorías activas de este run (ÚNICAMENTE estas tres):**
1. Hogar Inteligente
2. Inteligencia Artificial
3. Productividad Digital

**Restricciones de deduplicación críticas:**
- Hogar Inteligente: evitar tema Matter/Thread o protocolos de interoperabilidad (ya publicado).
- Inteligencia Artificial: evitar comparación de modelos (ChatGPT vs Claude vs Gemini), trucos de IA generativa con Meta Muse Spark, y explicación básica de agentes de IA (todos publicados).
- Productividad Digital: evitar el ángulo "trampa de las apps" y la guía de automatización sin código con Zapier/Make/n8n (ambos publicados).

**Objetivo:** 3 briefings APTO (1 por categoría). Score mínimo aceptable: 75/100.

Por cada tema entrega un briefing completo con los 31 campos definidos en el RUN_CONTEXT. Investiga en español e inglés. Usa tendencias, competencia, medios tecnológicos, documentación oficial y comunidades. No copies enfoques; úsalos para detectar oportunidades y explicar mejor para usuarios normales.

---

## STOP_CONDITIONS

1. No hay acceso a búsqueda web o herramienta equivalente.
2. No se puede leer `articulos_publicados.json`.
3. No se pueden guardar outputs en el filesystem.
4. El destino WordPress no es DRAFT.
5. Ninguna categoría activa obtiene al menos 1 tema apto tras segunda pasada.
6. Solo se encuentran temas de alto riesgo o no verificables.

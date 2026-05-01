# Run Context — PragmaWire Pipeline

## ESTADO_PIPELINE

`PIPELINE_READY_WITH_WARNINGS`

## MOTIVO

El pipeline puede arrancar. La infraestructura de escritura de outputs, memoria local y escritura de artículos está disponible. Se dispone de WebSearch y WebFetch para investigación, aunque no hay acceso directo a la API de Google Trends ni a Firecrawl MCP. La investigación puede realizarse via búsqueda web y lectura de fuentes directamente. El destino WordPress Draft está confirmado como borrador únicamente. `articulos_publicados.json` está disponible y accesible.

**RESTRICCIÓN ACTIVA**: Este run cubre exclusivamente 3 categorías: Hogar Inteligente, Inteligencia Artificial y Productividad Digital. Objetivo: 3 artículos (1 por categoría). Las categorías Recomendaciones Tecnológicas, Salud y Bienestar Digital y Seguridad Digital quedan fuera de este run.

---

## VALIDACIONES_TECNICAS

- WordPress MCP: WARNING (acceso vía script `post_to_wp.py` con API REST, sin MCP directo)
- Firecrawl o búsqueda: WARNING (WebSearch y WebFetch disponibles; Firecrawl MCP no disponible)
- Google Trends o tendencias: WARNING (sin API directa; se usará WebSearch como sustituto)
- Scraping/análisis de competencia: OK (WebFetch permite lectura de URLs externas)
- Fuentes ES/EN disponibles: OK
- Memoria local: OK
- articulos_publicados.json: OK (leído correctamente, 1 entrada de referencia)
- Categorías editoriales: OK (definidas en resources/categorias.md)
- Sistema de guardado de outputs: OK (filesystem disponible)
- Destino WordPress Draft: OK (publish_allowed: false confirmado en current-run.json)

---

## VALIDACIONES_EDITORIALES

- Categorías objetivo definidas: OK (Hogar Inteligente, Inteligencia Artificial, Productividad Digital)
- Cobertura mínima por categoría definida: OK (mínimo 1 por categoría activa)
- Reglas de deduplicación definidas: OK
- Scoring mínimo definido: OK (≥75 puntos)
- Fuentes permitidas definidas: OK (resources/fuentes-preferentes.md)
- Fuentes en español e inglés definidas: OK
- Criterios de frescura definidos: OK
- Condiciones de parada definidas: OK
- Prohibición de publicación automática: OK (publish_allowed: false)

---

## RUN_CONTEXT

```yaml
run_id: 2026-05-01T0115_pragmawire_237a
execution_date: 2026-05-01
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

excluded_categories:
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
    - WebSearch (sustituto de Google Trends)
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
  - fewer_than_3_valid_topics_found
  - any_active_category_without_valid_topic_after_expansion
  - high_risk_unverifiable_topics_only
```

---

## WARNINGS

1. **Google Trends sin API directa**: El Agente Investigador debe usar WebSearch para buscar tendencias de búsqueda. Buscar queries como "site:trends.google.com" o artículos sobre tendencias tecnológicas de 2026 en los medios de referencia.
2. **Firecrawl no disponible**: Usar WebFetch directamente para leer URLs de fuentes.
3. **Solo 1 artículo publicado previamente**: La base de deduplicación es mínima; el riesgo de duplicados es bajo pero el enlazado interno será limitado.

---

## NEXT_AGENT

`Agente Investigador`

---

## INSTRUCCION_PARA_AGENTE_INVESTIGADOR

> Busca y valida temas para PragmaWire.com siguiendo estrictamente el RUN_CONTEXT y el archivo `01-run-context/categorias_target.md`. El objetivo es conseguir 1 tema apto por cada categoría activa del run (mínimo obligatorio también de 1 por categoría activa). No rellenes con temas mediocres: si no llegas al objetivo en la primera pasada, amplía fuentes, idiomas, tendencias y competencia antes de cerrar la tanda.

**Categorías activas en este run**: Hogar Inteligente, Inteligencia Artificial, Productividad Digital.

**Excluidas en este run**: Recomendaciones Tecnológicas, Salud y Bienestar Digital, Seguridad Digital.

Entrega exactamente **3 briefings** (1 por cada categoría activa), cada uno con:

1. ID del briefing
2. Estado: APTO / DESCARTADO / NECESITA_REVISION
3. Categoría principal
4. Categoría secundaria (si aplica)
5. Tema propuesto
6. Ángulo editorial
7. Intención de búsqueda
8. Tipo de contenido recomendado
9. Palabra clave principal
10. Palabras clave secundarias
11. Entidades principales
12. Público objetivo
13. Problema real que resuelve
14. Por qué merece publicarse ahora
15. Respuesta corta esperada del artículo
16. Fuentes verificables
17. Idioma de las fuentes principales
18. Datos confirmados
19. Datos pendientes de verificar
20. Riesgo de obsolescencia
21. Nivel de actualización necesario
22. Oportunidad SEO
23. Oportunidad AEO
24. Oportunidad GEO / IA
25. Posibles enlaces internos
26. Estado de deduplicación
27. Artículos relacionados ya publicados
28. Score total (0-100, mínimo 75 para ser APTO)
29. Justificación del score
30. Recomendación final: INVESTIGAR / DESCARTAR / RESERVAR
31. Notas para el Redactor

Usa WebSearch para tendencias y WebFetch para leer fuentes directas. Investiga en español e inglés.

---

## STOP_CONDITIONS

- Falta infraestructura crítica (sin sistema de guardado, sin acceso a búsqueda)
- No se pueden verificar duplicados
- No se pueden guardar outputs
- El destino WordPress no es borrador
- Menos de 3 temas válidos tras expansión de búsqueda
- Alguna categoría activa sin tema apto tras segunda pasada
- Solo se encuentran temas de alto riesgo no verificables

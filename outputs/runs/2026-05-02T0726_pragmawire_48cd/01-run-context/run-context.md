# Run Context — PragmaWire Pipeline

## ESTADO_PIPELINE

`PIPELINE_READY_WITH_WARNINGS`

## MOTIVO

El pipeline puede arrancar en modo PRODUCCION_DRAFT. La infraestructura local está operativa: acceso a sistema de archivos, memoria, recursos editoriales y herramientas de búsqueda web. Se aplica la restricción de Routine B: solo 3 categorías activas. Advertencia: WordPress se gestiona via script (`post_to_wp.py`) dependiente de variables de entorno (WP_URL, WP_USER, WP_APP_PASSWORD); se validará en el Paso 6. La memoria de artículos publicados contiene solo 1 entrada (passkeys / Seguridad Digital), lo que limita el enlazado interno en esta ejecución.

---

## VALIDACIONES_TECNICAS

- WordPress MCP: WARNING (se usa `scripts/post_to_wp.py` con vars de entorno; acceso confirmado en Paso 6)
- Firecrawl o búsqueda: OK (WebSearch + WebFetch disponibles)
- Google Trends o tendencias: OK (WebSearch disponible para consultas de tendencias)
- Scraping/análisis de competencia: OK (WebFetch disponible)
- Fuentes ES/EN disponibles: OK
- Memoria local: OK (`memory/articulos_publicados.json` leído correctamente)
- articulos_publicados.json: OK (1 artículo registrado)
- Categorías editoriales: OK (`resources/categorias.md` disponible)
- Sistema de guardado de outputs: OK (filesystem activo)
- Destino WordPress Draft: OK (publish_allowed: false confirmado)

---

## VALIDACIONES_EDITORIALES

- Categorías objetivo definidas: OK (Routine B: 3 categorías activas)
- Cobertura mínima por categoría definida: OK (mínimo 1 por categoría activa)
- Reglas de deduplicación definidas: OK
- Scoring mínimo definido: OK (≥75)
- Fuentes permitidas definidas: OK (`resources/fuentes-preferentes.md`)
- Fuentes en español e inglés definidas: OK
- Criterios de frescura definidos: OK
- Condiciones de parada definidas: OK
- Prohibición de publicación automática: OK (publish: false enforced)

---

## RESTRICCIÓN DE ESTE RUN (ROUTINE B)

```yaml
routine: B
categorias_activas:
  - Recomendaciones Tecnológicas
  - Salud y Bienestar Digital
  - Seguridad Digital
categorias_excluidas:
  - Hogar Inteligente
  - Inteligencia Artificial
  - Productividad Digital
articulos_objetivo: 3
articulos_minimo: 3
distribucion_objetivo:
  Recomendaciones Tecnológicas: 1
  Salud y Bienestar Digital: 1
  Seguridad Digital: 1
distribucion_minima:
  Recomendaciones Tecnológicas: 1
  Salud y Bienestar Digital: 1
  Seguridad Digital: 1
```

---

## RUN_CONTEXT

```yaml
run_id: 2026-05-02T0726_pragmawire_48cd
execution_date: 2026-05-02
execution_mode: PRODUCCION_DRAFT
routine: B

target_articles: 3
minimum_articles: 3
minimum_per_category: 1
target_per_category: 1
quality_over_quantity: true
wordpress_destination: WORDPRESS_DRAFT
publish_allowed: false

target_categories:
  - Recomendaciones Tecnológicas
  - Salud y Bienestar Digital
  - Seguridad Digital

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
  security_sources:
    - INCIBE
    - OSI
    - CISA
    - Kaspersky
    - ESET
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

articulos_ya_publicados_relevantes:
  - titulo: "Qué son las passkeys y por qué importan"
    slug: que-son-passkeys
    categoria: Seguridad Digital
    tema_principal: passkeys
    nota: EXISTE_IDENTICO — no repetir passkeys como tema principal

forbidden_topics:
  - rumours_without_sources
  - medical_claims_without_authoritative_sources
  - financial_promises
  - cybersecurity_claims_without_verification
  - clickbait
  - generic_articles_without_practical_value
  - product_recommendations_without_verifiable_data
  - passkeys (ya publicado — EXISTE_IDENTICO)

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

1. **WordPress via script**: La integración con WordPress se realiza mediante `scripts/post_to_wp.py` que depende de variables de entorno (WP_URL, WP_USER, WP_APP_PASSWORD). Si estas variables no están configuradas, el Paso 6 fallará. No es bloqueante para los pasos 1-5.
2. **Memoria limitada**: Solo hay 1 artículo en `memory/articulos_publicados.json` (passkeys, Seguridad Digital). El enlazado interno será limitado en esta ejecución.
3. **Seguridad Digital — deduplicación**: El único artículo registrado es de Seguridad Digital (passkeys). El Investigador debe proponer un tema de Seguridad Digital distinto.

---

## NEXT_AGENT

`Agente Investigador`

---

## INSTRUCCION_PARA_AGENTE_INVESTIGADOR

Busca y valida temas para PragmaWire.com siguiendo estrictamente el RUN_CONTEXT y el archivo `01-run-context/categorias_target.md`.

**Este run es Routine B.** Solo investiga temas de estas 3 categorías:
1. Recomendaciones Tecnológicas
2. Salud y Bienestar Digital
3. Seguridad Digital

Ignora completamente Hogar Inteligente, Inteligencia Artificial y Productividad Digital.

**Objetivo:** 3 artículos aptos, 1 por cada categoría activa. El mínimo obligatorio también es 1 por categoría.

**Restricción crítica — Seguridad Digital:** Ya existe el artículo "Qué son las passkeys y por qué importan" (slug: `que-son-passkeys`). El tema passkeys está EXISTE_IDENTICO — no proponer passkeys como tema principal. Busca otro ángulo de Seguridad Digital.

Investiga en español e inglés usando tendencias, competencia (Xataka, Genbeta, The Verge, Wired, Ars Technica), fuentes de seguridad (INCIBE, CISA, ESET, Krebs), comunidades (Reddit, HN) y documentación oficial.

Por cada briefing entrega los 31 campos del formato estándar (ID, estado, categoría, tema, ángulo, intención de búsqueda, tipo de contenido, palabra clave principal, palabras clave secundarias, entidades, público, problema que resuelve, por qué ahora, respuesta corta esperada, fuentes verificables, idioma de fuentes, datos confirmados, datos pendientes, riesgo de obsolescencia, nivel de actualización, oportunidad SEO, oportunidad AEO, oportunidad GEO/IA, posibles enlaces internos, estado de deduplicación, artículos relacionados, score 0-100, justificación del score, recomendación final, notas para el Redactor).

Score mínimo aceptable: 75. No aceptes temas por debajo de 75 sin justificación editorial sólida.

Si no encuentras 3 temas aptos en la primera pasada, realiza segunda pasada ampliando fuentes antes de cerrar la tanda.

---

## STOP_CONDITIONS

- No hay acceso a sistema de búsqueda web.
- No se puede leer `articulos_publicados.json`.
- No se pueden guardar outputs en el filesystem.
- El destino configurado permite publicación directa (publish: true).
- Tras dos pasadas de investigación, alguna categoría activa queda sin tema apto.
- Los únicos temas disponibles son de riesgo alto o no verificables.

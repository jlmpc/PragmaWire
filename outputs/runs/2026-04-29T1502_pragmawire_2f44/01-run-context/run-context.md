# Run Context — PragmaWire Pipeline

**RUN_ID:** 2026-04-29T1502_pragmawire_2f44  
**Fecha de ejecución:** 2026-04-29  
**Modo:** PRODUCCION_DRAFT  
**Generado por:** supervisor-inicial-pragmawire

---

## ESTADO_PIPELINE

`PIPELINE_READY_WITH_WARNINGS`

---

## MOTIVO

El pipeline puede arrancar. Toda la infraestructura crítica está operativa: variables de entorno de WordPress confirmadas (WP_URL, WP_USER, WP_APP_PASSWORD), herramientas de búsqueda web y fetch disponibles, sistema de escritura de archivos operativo, categorías editoriales definidas y destino `WORDPRESS_DRAFT` confirmado. Existen dos advertencias no críticas: (1) la memoria de artículos publicados contiene únicamente 1 artículo de ejemplo, lo que limita las oportunidades de enlazado interno en esta tanda; (2) no hay herramienta dedicada de Google Trends, aunque es accesible via búsqueda web. El Agente Investigador debe tenerlo en cuenta al generar oportunidades de enlazado, y compensar la falta de historial con investigación más amplia de competencia y tendencias.

---

## VALIDACIONES_TECNICAS

- WordPress MCP / REST API: **OK** — WP_URL, WP_USER y WP_APP_PASSWORD definidos y operativos
- Firecrawl o búsqueda web: **OK** — WebSearch y WebFetch disponibles
- Google Trends o tendencias: **WARNING** — Accesible via búsqueda web, sin herramienta dedicada
- Scraping / análisis de competencia: **OK** — WebFetch disponible para leer webs referentes
- Fuentes ES/EN disponibles: **OK** — Acceso a medios en español e inglés vía búsqueda
- Memoria local: **OK** — articulos_publicados.json legible
- articulos_publicados.json: **OK** — Leído correctamente (1 artículo de ejemplo)
- Categorías editoriales: **OK** — 6 categorías definidas en resources/categorias.md
- Sistema de guardado de outputs: **OK** — Escritura de archivos operativa
- Destino WordPress Draft: **OK** — WORDPRESS_DRAFT confirmado, publish_allowed: false

---

## VALIDACIONES_EDITORIALES

- Categorías objetivo definidas: **OK** — 6 categorías principales activas
- Cobertura mínima por categoría definida: **OK** — mínimo 1, objetivo 2 por categoría
- Reglas de deduplicación definidas: **OK** — 7 dimensiones de comparación activas
- Scoring mínimo definido: **OK** — umbral mínimo 75/100
- Fuentes permitidas definidas: **OK** — Documentadas en resources/fuentes-preferentes.md
- Fuentes en español e inglés definidas: **OK** — Listadas en supervisor-inicial.md
- Criterios de frescura definidos: **OK** — BAJA / MEDIA / ALTA
- Condiciones de parada definidas: **OK** — Documentadas en run_context YAML
- Prohibición de publicación automática: **OK** — publish_allowed: false en manifest y current-run.json

---

## RUN_CONTEXT

```yaml
run_id: 2026-04-29T1502_pragmawire_2f44
execution_date: "2026-04-29"
execution_mode: PRODUCCION_DRAFT
target_articles: 12
minimum_articles: 6
minimum_per_category: 1
target_per_category: 2
quality_over_quantity: true
wordpress_destination: WORDPRESS_DRAFT
publish_allowed: false

target_categories:
  - Hogar Inteligente
  - Inteligencia Artificial
  - Productividad Digital
  - Recomendaciones Tecnológicas
  - Salud y Bienestar Digital
  - Seguridad Digital

category_distribution_target:
  Hogar Inteligente: 2
  Inteligencia Artificial: 2
  Productividad Digital: 2
  Recomendaciones Tecnológicas: 2
  Salud y Bienestar Digital: 2
  Seguridad Digital: 2

category_distribution_minimum:
  Hogar Inteligente: 1
  Inteligencia Artificial: 1
  Productividad Digital: 1
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
    - Google Trends (via web search)
    - related_searches
    - social_trends_when_relevant
    - YouTube trending topics
  spanish_media:
    - Xataka
    - Genbeta
    - Applesfera
    - Computer Hoy
    - Hipertextual
    - El Androide Libre
  english_media:
    - The Verge
    - TechCrunch
    - Wired
    - Ars Technica
    - VentureBeat
    - Engadget
    - Android Authority
    - 9to5Mac
  communities:
    - Reddit
    - Hacker News
    - LinkedIn
    - X/Twitter
  official_sources:
    - product_documentation
    - official_blogs
    - support_pages
    - security_advisories_INCIBE_OSI_CISA
  competitor_analysis:
    - detect_working_topics
    - detect_editorial_gaps
    - detect_repeated_angles_to_avoid
    - detect_underexplained_topics_for_normal_users

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

articles_already_published:
  - slug: que-son-passkeys
    categoria: Seguridad Digital
    tema: passkeys
    palabra_clave: "qué son las passkeys"
    estado: ejemplo
    nota: "Artículo de ejemplo — evitar duplicado exacto. Ángulo diferente permitido con valor añadido."

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
  count: up_to_12
  target_count: 12
  minimum_count: 6
  require_minimum_one_per_category: true
  allow_less_than_12_if_quality_low: true
  require_second_research_pass_if_less_than_12: true
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
  - fewer_than_6_valid_topics_found
  - any_category_without_valid_topic_after_expansion
  - high_risk_unverifiable_topics_only
```

---

## WARNINGS

1. **Historial de artículos publicados escaso**: Solo existe 1 artículo en `articulos_publicados.json` (estado "ejemplo"), lo que limita las posibilidades de enlazado interno en esta tanda. El Agente Investigador debe identificar qué artículos se crearán en paralelo para sugerir enlaces cruzados dentro del mismo run.
2. **Google Trends sin herramienta dedicada**: El acceso a tendencias se realiza vía búsqueda web general. El Agente Investigador debe compensar realizando búsquedas explícitas de tendencias en Google Trends, Reddit, Hacker News y LinkedIn para validar el interés real de cada tema propuesto.

---

## NEXT_AGENT

`Agente Investigador`

---

## INSTRUCCION_PARA_AGENTE_INVESTIGADOR

> Busca y valida hasta 12 temas para PragmaWire.com siguiendo estrictamente el RUN_CONTEXT. El objetivo es conseguir 2 temas aptos por categoría y un mínimo obligatorio de 1 tema apto por categoría. No rellenes con temas mediocres: si no llegas a 12 en la primera pasada, amplía fuentes, idiomas, tendencias y competencia antes de cerrar la tanda.

**Contexto específico de este run:**

- Fecha: 2026-04-29. Investiga temas con relevancia actual o evergreen sólido.
- Historial publicado: solo 1 artículo (passkeys - Seguridad Digital). Evita duplicar ese tema exacto. El resto de categorías está limpio de historial, lo que permite libertad editorial amplia.
- Prioridad: encontrar temas que sean útiles para un lector hispanohablante no experto, con valor práctico demostrable y potencial SEO/AEO/GEO real.
- No copiar enfoques de competidores. Úsalos para detectar huecos y oportunidades de explicar mejor.

**Categorías objetivo (2 por categoría, mínimo 1):**

1. Hogar Inteligente — domótica, Matter, Thread, Zigbee, Apple Home, Google Home, Alexa, sensores, enchufes, luces, climatización
2. Inteligencia Artificial — ChatGPT, Claude, Gemini, Copilot, Perplexity, agentes, automatización práctica
3. Productividad Digital — apps, organización, automatización, métodos, flujos personales
4. Recomendaciones Tecnológicas — comparativas, compras, gadgets, software, servicios, accesorios
5. Salud y Bienestar Digital — sueño, pantallas, wearables, ergonomía, hábitos digitales
6. Seguridad Digital — privacidad, passkeys (ángulo diferente al existente), phishing, estafas, protección de cuentas

**Por cada tema, entrega un briefing completo con los 31 campos especificados en el RUN_CONTEXT.**

**Score mínimo aceptado: 75/100.**

**Proceso obligatorio:**
1. Primera pasada: busca en tendencias, medios ES/EN, competencia y comunidades.
2. Si no llegas a 12 temas aptos: segunda pasada obligatoria ampliando fuentes.
3. Si tras la segunda pasada una categoría sigue sin tema apto: informa el bloqueo con detalle.

---

## STOP_CONDITIONS

El pipeline debe detenerse si:

- Falta infraestructura crítica (sistema de escritura, búsqueda web o acceso a WordPress)
- No se pueden verificar duplicados
- No se pueden guardar los outputs
- El destino WordPress no es DRAFT
- Se encuentran menos de 6 temas válidos en total
- Alguna categoría queda sin ningún tema apto tras ampliar la búsqueda
- Solo quedan temas de alto riesgo no verificables

# Run Context — PragmaWire Pipeline
# RUN_ID: 2026-05-17T0315_pragmawire_97c1

## ESTADO_PIPELINE

`PIPELINE_READY_WITH_WARNINGS`

## MOTIVO

El pipeline puede arrancar en modo PRODUCCION_DRAFT para Routine B. Las 3 categorías objetivo (Recomendaciones Tecnológicas, Salud y Bienestar Digital, Seguridad Digital) están definidas y el sistema de búsqueda web está disponible. Se registra WARNING porque el acceso a WordPress es por REST API con variables de entorno (no MCP directo), lo cual es técnicamente válido para crear borradores. El inventario de artículos publicados está disponible y permite deduplicación. No hay riesgo de publicación automática.

## VALIDACIONES_TECNICAS

- WordPress REST API (post_to_wp.py): OK
- Búsqueda web (WebSearch/WebFetch): OK
- Tendencias / Google Trends: WARNING (acceso indirecto vía búsqueda web)
- Scraping/análisis competencia: OK (WebFetch disponible)
- Fuentes ES/EN disponibles: OK
- Memoria local: OK
- articulos_publicados.json: OK (12 artículos registrados)
- Categorías editoriales: OK
- Sistema de guardado de outputs: OK
- Destino WordPress Draft: OK (publish: false enforced)

## VALIDACIONES_EDITORIALES

- Categorías objetivo definidas: OK (Routine B — 3 categorías)
- Cobertura mínima por categoría definida: OK (1 artículo por categoría)
- Reglas de deduplicación definidas: OK
- Scoring mínimo definido: OK (≥75)
- Fuentes permitidas definidas: OK
- Fuentes en español e inglés definidas: OK
- Criterios de frescura definidos: OK
- Condiciones de parada definidas: OK
- Prohibición de publicación automática: OK (enforced en código y pipeline)

## RUN_CONTEXT

```yaml
execution_date: "2026-05-17"
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

ignored_categories_this_run:
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

articulos_publicados_por_categoria:
  Recomendaciones Tecnológicas:
    - "Cargadores GaN: qué son y cómo elegir el correcto en 2026" (2026-04-07)
    - "Mejor router WiFi para casa en 2026: cómo elegir bien entre WiFi 6, WiFi 7 o sistema mesh" (2026-04-06)
  Salud y Bienestar Digital:
    - "Tecnología para dormir mejor: apps y hábitos que funcionan de verdad" (2026-04-03)
  Seguridad Digital:
    - "Quishing: qué es la estafa del código QR y cómo protegerte" (2026-04-02)
    - "Cómo detectar estafas tecnológicas: 7 señales claras para evitar fraudes online" (2026-04-01)
    - "Qué es una Passkey y por qué puede sustituir a muchas contraseñas" (2026-03-31)

required_search_intent:
  - informational
  - commercial_investigation
  - practical_how_to
  - explainer

minimum_article_quality_score: 90

research_languages:
  - Spanish
  - English

research_sources_required:
  trends:
    - Google Trends (vía búsqueda web)
    - búsquedas relacionadas
    - tendencias redes sociales cuando sea relevante
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
    - Engadget
  security_specific:
    - INCIBE
    - OSI
    - CISA
    - Kaspersky
    - ESET
  communities:
    - Reddit
    - Hacker News

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

forbidden_topics:
  - rumours_without_sources
  - medical_claims_without_authoritative_sources
  - cybersecurity_claims_without_verification
  - clickbait
  - generic_articles_without_practical_value
  - products_or_prices_without_verifiable_data
  - duplicate_angle_to_existing_articles

output_required:
  format: briefing_markdown
  count: 3
  minimum_count: 3
  require_minimum_one_per_category: true
  include_topic_score: true
  include_deduplication_status: true
  include_sources: true

stop_conditions:
  - any_target_category_without_valid_topic
  - cannot_verify_duplicates
  - wordpress_destination_is_not_draft
  - high_risk_unverifiable_topics_only
```

## WARNINGS

- Acceso a Google Trends indirecto (vía búsqueda web); el Agente Investigador debe buscar tendencias activamente usando queries específicas.
- Salud y Bienestar Digital tiene solo 1 artículo previo (descanso/sueño); amplia disponibilidad de ángulos frescos.
- Seguridad Digital tiene 3 artículos previos (passkeys, quishing, estafas); el Investigador debe buscar ángulos diferenciados.

## NEXT_AGENT

`Agente Investigador`

## INSTRUCCION_PARA_AGENTE_INVESTIGADOR

Busca y valida temas para PragmaWire.com siguiendo estrictamente el RUN_CONTEXT y el archivo `01-run-context/categorias_target.md`. Este es un run Routine B: solo investigas las 3 categorías siguientes:

1. **Recomendaciones Tecnológicas** — 1 artículo objetivo
2. **Salud y Bienestar Digital** — 1 artículo objetivo
3. **Seguridad Digital** — 1 artículo objetivo

**Artículos ya publicados — NO duplicar ángulo:**
- Recomendaciones Tecnológicas: cargadores GaN, routers WiFi
- Salud y Bienestar Digital: tecnología para dormir
- Seguridad Digital: quishing/QR, detección estafas, passkeys

**Briefing requerido por cada tema (31 campos):**
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
28. Score total 0-100
29. Justificación del score
30. Recomendación final: INVESTIGAR / DESCARTAR / RESERVAR
31. Notas para el Redactor

**Scoring mínimo aceptado:** 75. Solo artículos APTO avanzan.
**Si no encuentras 1 tema apto por categoría en la primera pasada:** amplía fuentes, ángulos e idiomas obligatoriamente antes de cerrar.

## STOP_CONDITIONS

- Alguna categoría objetivo sin tema apto tras ampliar búsqueda
- No se puede verificar duplicados
- Destino WordPress no es DRAFT
- Solo se encuentran temas de alto riesgo no verificables

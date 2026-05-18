# Run Context — PragmaWire Pipeline
## RUN_ID: 2026-05-18T0315_pragmawire_fbbf

---

### ESTADO_PIPELINE

`PIPELINE_READY_WITH_WARNINGS`

### MOTIVO

El pipeline puede arrancar en modo PRODUCCION_DRAFT. El entorno dispone de acceso a búsqueda web, fuentes en español e inglés, sistema de escritura local de outputs y ruta de destino WORDPRESS_DRAFT confirmada. No hay acceso directo a WordPress MCP en este entorno cloud, pero el script `post_to_wp.py` gestiona la integración via REST API con las variables de entorno WP_URL, WP_USER y WP_APP_PASSWORD. Las restricciones de categoría (Rutina B) están correctamente definidas en `categorias_target.md`. Se registra advertencia por ausencia de Google Trends nativo, que se suplirá con búsquedas web y análisis competitivo.

---

### VALIDACIONES_TECNICAS

- WordPress MCP: WARNING (sin MCP directo; se usa REST API via post_to_wp.py)
- Firecrawl o búsqueda: OK (WebSearch disponible)
- Google Trends o tendencias: WARNING (sin acceso directo; se infiere de búsquedas y competencia)
- Scraping/análisis de competencia: OK (WebFetch + WebSearch)
- Fuentes ES/EN disponibles: OK
- Memoria local: OK
- articulos_publicados.json: OK (12 artículos registrados, leído correctamente)
- Categorías editoriales: OK (restricción Rutina B activa)
- Sistema de guardado de outputs: OK
- Destino WordPress Draft: OK (create_draft: true, publish: false)

---

### VALIDACIONES_EDITORIALES

- Categorías objetivo definidas: OK (Recomendaciones Tecnológicas, Salud y Bienestar Digital, Seguridad Digital)
- Cobertura mínima por categoría definida: OK (mínimo 1 artículo por categoría)
- Reglas de deduplicación definidas: OK
- Scoring mínimo definido: OK (≥75)
- Fuentes permitidas definidas: OK
- Fuentes en español e inglés definidas: OK
- Criterios de frescura definidos: OK
- Condiciones de parada definidas: OK
- Prohibición de publicación automática: OK (publish: false en todos los casos)

---

### RUN_CONTEXT

```yaml
run_id: 2026-05-18T0315_pragmawire_fbbf
execution_date: 2026-05-18
execution_mode: PRODUCCION_DRAFT
routine: B
target_articles: 3
minimum_articles: 3
minimum_per_category: 1
target_per_category: 1
quality_over_quantity: true
wordpress_destination: WORDPRESS_DRAFT
publish_allowed: false

# RESTRICCIÓN ACTIVA: Rutina B — solo estas 3 categorías
target_categories:
  - Recomendaciones Tecnológicas
  - Salud y Bienestar Digital
  - Seguridad Digital

# Categorías excluidas de este run
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

# Artículos ya publicados por categoría activa (para deduplicación)
articulos_publicados_por_categoria:
  Recomendaciones Tecnológicas:
    - slug: cargadores-gan-guia-2026
      titulo: "Cargadores GaN: qué son y cómo elegir el correcto en 2026"
      kw_principal: cargadores GaN
    - slug: mejor-router-wifi-2026
      titulo: "Mejor router WiFi para casa en 2026"
      kw_principal: mejor router WiFi 2026
  Salud y Bienestar Digital:
    - slug: tecnologia-que-mejora-tu-descanso
      titulo: "Tecnología para dormir mejor"
      kw_principal: tecnología dormir mejor
  Seguridad Digital:
    - slug: quishing-estafa-qr-proteccion
      titulo: "Quishing: qué es la estafa del código QR y cómo protegerte"
      kw_principal: quishing estafa QR
    - slug: detectar-estafas-tecnologicas
      titulo: "Cómo detectar estafas tecnológicas: 7 señales claras"
      kw_principal: detectar estafas tecnológicas
    - slug: que-son-passkeys
      titulo: "Qué es una Passkey y por qué puede sustituir a muchas contraseñas"
      kw_principal: qué es una passkey

required_search_intent:
  - informational
  - commercial_investigation
  - practical_how_to
  - explainer

minimum_quality_score_article: 90

research_languages:
  - Spanish
  - English

research_sources_required:
  trends:
    - búsquedas sugeridas de Google
    - análisis competitivo
    - Reddit y Hacker News
    - LinkedIn y X/Twitter
  spanish_media:
    - Xataka
    - Genbeta
    - Computer Hoy
    - Hipertextual
    - El Androide Libre
  english_media:
    - The Verge
    - TechCrunch
    - Wired
    - Ars Technica
    - Engadget
  security_sources:
    - INCIBE
    - OSI
    - CISA
    - Kaspersky Blog
    - ESET
    - Krebs on Security

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

stop_conditions:
  - cannot_verify_duplicates
  - cannot_save_outputs
  - wordpress_destination_is_not_draft
  - any_category_without_valid_topic_after_expansion
  - high_risk_unverifiable_topics_only
```

---

### WARNINGS

- **Google Trends sin acceso directo:** El Agente Investigador debe inferir tendencias desde búsquedas web, competencia y comunidades.
- **WordPress sin MCP nativo:** La integración se realiza mediante `post_to_wp.py` vía REST API con variables de entorno. No impide el pipeline.
- **Seguridad Digital tiene 3 artículos previos (quishing, detectar estafas, passkeys):** El Investigador debe buscar ángulos no cubiertos (privacidad de datos, VPN para no expertos, gestores de contraseñas, seguridad en redes públicas, etc.).
- **Salud y Bienestar tiene solo 1 artículo previo (descanso):** Amplio margen para temas como salud visual, estrés digital, ergonomía, etc.
- **Recomendaciones Tecnológicas tiene 2 artículos previos (routers, cargadores GaN):** Quedan áreas libres: auriculares, monitores, servicios streaming, antivirus, discos duros externos, etc.

---

### NEXT_AGENT

`Agente Investigador`

---

### INSTRUCCION_PARA_AGENTE_INVESTIGADOR

> Busca y valida temas para PragmaWire.com siguiendo estrictamente el RUN_CONTEXT y el archivo `01-run-context/categorias_target.md`. El objetivo es conseguir **1 tema apto por cada una de las 3 categorías activas de este run** (Rutina B). Mínimo obligatorio también de 1 por categoría. No rellenes con temas mediocres: si no llegas al objetivo en la primera pasada, amplía fuentes, idiomas, tendencias y competencia antes de cerrar la tanda.

**Categorías activas de este run (SOLO ESTAS TRES):**
1. Recomendaciones Tecnológicas
2. Salud y Bienestar Digital
3. Seguridad Digital

**Artículos ya publicados a evitar (deduplicación):**

- Recomendaciones Tecnológicas: cargadores GaN (cargadores-gan-guia-2026), mejor router WiFi (mejor-router-wifi-2026)
- Salud y Bienestar Digital: tecnología para dormir mejor (tecnologia-que-mejora-tu-descanso)
- Seguridad Digital: quishing/QR (quishing-estafa-qr-proteccion), detectar estafas (detectar-estafas-tecnologicas), passkeys (que-son-passkeys)

**Requisitos por briefing:**

1. ID del briefing
2. Estado: APTO / DESCARTADO / NECESITA_REVISION
3. Categoría principal
4. Categoría secundaria
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
28. Score total de 0 a 100
29. Justificación del score
30. Recomendación final: INVESTIGAR / DESCARTAR / RESERVAR
31. Notas para el Redactor

**Score mínimo aceptable:** 75. No entregar briefings con score inferior a 75 salvo justificación editorial sólida.

---

### STOP_CONDITIONS

- Incapacidad para verificar duplicados contra `articulos_publicados.json`
- Destino WordPress configurado como publicación directa
- Cualquier categoría activa sin tema apto tras ampliar búsqueda
- Temas solo verificables con fuentes de alto riesgo o no contrastables
- Incapacidad para guardar outputs en la carpeta activa del run

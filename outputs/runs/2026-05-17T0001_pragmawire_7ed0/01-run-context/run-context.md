# Run Context — PragmaWire Pipeline

## ESTADO_PIPELINE

`PIPELINE_READY_WITH_WARNINGS`

## MOTIVO

El pipeline puede arrancar en modo PRODUCCION_DRAFT. Las categorías objetivo están definidas (Rutina A: Hogar Inteligente, Inteligencia Artificial, Productividad Digital). El sistema de búsqueda web, la memoria de artículos publicados y el sistema de guardado de outputs están operativos. Se detectan advertencias no críticas: el acceso a WordPress es vía script local (post_to_wp.py) y no vía MCP directo, lo que requiere variables de entorno configuradas; la categoría Hogar Inteligente tiene escasa cobertura previa (1 artículo publicado), lo que obliga a mayor profundidad de investigación; el enlazado interno disponible es limitado.

## RESTRICCIÓN DE CATEGORÍAS ACTIVA

Archivo `categorias_target.md` detectado y leído. Las categorías activas de este run son exclusivamente:

- **Hogar Inteligente** (objetivo: 1 artículo)
- **Inteligencia Artificial** (objetivo: 1 artículo)
- **Productividad Digital** (objetivo: 1 artículo)

Categorías excluidas de este run: Recomendaciones Tecnológicas, Salud y Bienestar Digital, Seguridad Digital.

## VALIDACIONES_TECNICAS

- WordPress MCP: WARNING (integración vía script post_to_wp.py, requiere credenciales en .env)
- Búsqueda web (WebSearch/WebFetch): OK
- Google Trends o tendencias: OK (vía WebSearch)
- Scraping/análisis de competencia: OK (vía WebFetch)
- Fuentes ES/EN disponibles: OK
- Memoria local: OK
- articulos_publicados.json: OK (12 artículos registrados)
- Categorías editoriales: OK (restricción Rutina A activa)
- Sistema de guardado de outputs: OK
- Destino WordPress Draft: OK (publish_allowed: false)

## VALIDACIONES_EDITORIALES

- Categorías objetivo definidas: OK (Hogar Inteligente, Inteligencia Artificial, Productividad Digital)
- Cobertura mínima por categoría definida: OK (mínimo 1 por categoría activa)
- Reglas de deduplicación definidas: OK
- Scoring mínimo definido: OK (≥ 75)
- Fuentes permitidas definidas: OK
- Fuentes en español e inglés definidas: OK
- Criterios de frescura definidos: OK
- Condiciones de parada definidas: OK
- Prohibición de publicación automática: OK

## RUN_CONTEXT

```yaml
run_id: 2026-05-17T0001_pragmawire_7ed0
execution_date: 2026-05-17
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

articulos_publicados_relevantes:
  Inteligencia Artificial:
    - slug: 5-trucos-nuevo-muse-spark
      title: "5 trucos gratis con Meta Muse Spark"
      fecha: 2026-04-10
    - slug: ia-agentica-para-2026
      title: "ChatGPT, Claude o Gemini: cuál usar en 2026"
      fecha: 2026-04-09
    - slug: que-es-un-agente-de-ia
      title: "Qué es un agente de IA y cómo configurar uno gratis"
      fecha: 2026-04-08
  Hogar Inteligente:
    - slug: matter-y-thread-guia
      title: "Matter y Thread: qué son y por qué importan"
      fecha: 2026-03-30
  Productividad Digital:
    - slug: trampa-apps-productividad
      title: "La trampa de las apps de productividad"
      fecha: 2026-04-05
    - slug: automatizar-tareas-sin-programar
      title: "Cómo automatizar tareas repetitivas sin saber programar"
      fecha: 2026-04-04

research_languages:
  - Español
  - Inglés

required_search_intent:
  - informational
  - commercial_investigation
  - practical_how_to
  - explainer

research_sources_required:
  trends:
    - Google Trends
    - búsquedas relacionadas
    - tendencias en redes sociales
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
    - documentación oficial de productos
    - blogs corporativos
    - notas de prensa

freshness_rules:
  low: contenido evergreen
  medium: verificar cambios recientes
  high: requiere fuentes recientes y verificación explícita

deduplication_rules:
  compare_slug: true
  compare_primary_keyword: true
  compare_secondary_keywords: true
  compare_topic_angle: true
  compare_search_intent: true
  compare_existing_articles: true
  compare_main_entities: true

forbidden_topics:
  - rumores sin fuentes
  - afirmaciones médicas sin autoridad
  - promesas financieras
  - ciberseguridad sin verificación
  - clickbait
  - contenido genérico sin valor práctico
  - recomendaciones de productos sin datos verificables
  - copia de enfoques de competidores sin valor original

stop_conditions:
  - infraestructura crítica no disponible
  - no se pueden verificar duplicados
  - no se pueden guardar outputs
  - destino WordPress no es draft
  - ninguna categoría activa tiene tema apto tras ampliar búsqueda
  - intento de publicación automática

quality_thresholds:
  minimum_topic_score: 75
  minimum_article_quality_score: 90
  wordpress_ready_threshold: 90
```

## WARNINGS

1. **WordPress vía script local:** La integración con WordPress se realiza mediante `post_to_wp.py`. Se requiere que el archivo `.env` tenga configuradas correctamente las credenciales `WP_URL`, `WP_USER` y `WP_APP_PASSWORD`. Si las credenciales no están disponibles en el entorno, el PASO 6 fallará, pero los artículos quedarán guardados en `05-wordpress-ready/` para publicación manual.

2. **Hogar Inteligente con poca base de enlaces internos:** Solo hay 1 artículo publicado en esta categoría (`matter-y-thread-guia`). El Investigador debe buscar temas que puedan enlazar a ese artículo o que aporten una perspectiva complementaria.

3. **Inteligencia Artificial muy cubierta:** Hay 3 artículos recientes sobre IA (Meta Muse Spark, comparativa de IAs, agentes de IA). El Investigador debe evitar enfoques idénticos y buscar ángulos genuinamente distintos (aplicaciones prácticas específicas, modelos de IA para tareas domésticas, IA en contextos hispanohablantes, etc.).

## NEXT_AGENT

`Agente Investigador`

## INSTRUCCION_PARA_AGENTE_INVESTIGADOR

Busca y valida temas para PragmaWire.com siguiendo estrictamente el RUN_CONTEXT y el archivo `01-run-context/categorias_target.md`. El objetivo es conseguir 1 tema apto por cada categoría activa del run (mínimo obligatorio también de 1 por categoría activa). No rellenes con temas mediocres: si no llegas al objetivo en la primera pasada, amplía fuentes, idiomas, tendencias y competencia antes de cerrar la tanda.

**Categorías activas de este run:** Hogar Inteligente, Inteligencia Artificial, Productividad Digital.
**Categorías excluidas:** Recomendaciones Tecnológicas, Salud y Bienestar Digital, Seguridad Digital.
**Objetivo:** 3 artículos (1 por categoría). Score mínimo por tema: 75/100.

**Restricciones de deduplicación críticas:**
- Inteligencia Artificial: ya existen artículos sobre Meta Muse Spark, comparativa ChatGPT/Claude/Gemini y agentes de IA. Evita enfoques idénticos.
- Productividad Digital: ya existen artículos sobre la trampa de las apps y automatización con Zapier/Make/n8n.
- Hogar Inteligente: existe artículo sobre Matter y Thread. Busca temas complementarios.

Investiga en español e inglés usando Google Trends, medios tecnológicos referentes (Xataka, The Verge, TechCrunch, Wired), Reddit, Hacker News y documentación oficial. Por cada tema entrega un briefing completo con los 31 campos definidos en el RUN_CONTEXT.

## STOP_CONDITIONS

- No hay acceso a búsqueda web (sistema bloqueado)
- No se puede leer articulos_publicados.json
- No se pueden guardar outputs en la carpeta del run
- El pipeline intenta publicar directamente en WordPress (publish: true)
- Ninguna categoría activa tiene al menos 1 tema con score ≥ 75 tras segunda pasada de búsqueda

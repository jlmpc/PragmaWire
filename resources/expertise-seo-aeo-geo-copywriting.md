# Expertise de Referencia: SEO, AEO, GEO/GXO y Copywriting para PragmaWire

> Documento de investigación basado en fuentes primarias (2024-2026).
> Generado en mayo 2026 mediante investigación activa con WebSearch y WebFetch.
> **Lectura obligatoria para el Agente Editor Estratégico antes de auditar cualquier artículo.**
> Actualizar cuando haya cambios significativos en el ecosistema de búsqueda.

---

## PARTE 1 — SEO MODERNO (2024-2025)

### 1.1 Topical Authority: la base de todo

Google mide internamente `siteFocus` (profundidad temática) y `siteRadius` (dispersión del contenido). Un blog que publica sobre tecnología, cocina y viajes ve diluida su autoridad en cada área. PragmaWire debe cubrir sus 6 categorías con profundidad de cluster, no con artículos dispersos.

**Cómo se construye:**
- **Página pilar** por categoría: guía comprehensiva que enlaza a todos los artículos del cluster.
- **Artículos de cluster**: subtemas específicos, enlazados a la pilar y entre sí cuando es relevante.
- Cada nuevo artículo debe vincularse a artículos existentes mediante anchor text descriptivo (no "clic aquí").
- Identificar y cubrir los subtemas que la competencia tiene pero PragmaWire no — cada gap es una debilidad de autoridad.

**Indicador de éxito**: qué porcentaje del tráfico total de un cluster de keywords captura PragmaWire vs. la competencia.

### 1.2 Entity SEO: entidades, no palabras clave

Google opera con un grafo de conocimiento de 54.000 millones de entidades. Un artículo sobre "passkeys" que no menciona FIDO Alliance, WebAuthn, autenticación sin contraseña, Apple, Google, Microsoft está perdiendo las conexiones semánticas que Google espera ver.

**Reglas operativas:**
- Seleccionar el nombre canónico de la entidad central antes de escribir y usarlo consistentemente (H1, primeros párrafos, al menos un H2).
- Mencionar entidades relacionadas del ecosistema del tema de forma natural: herramientas, protocolos, empresas, estándares.
- Enlazar externamente a páginas oficiales (Wikipedia, sitios de organizaciones, documentación oficial) para anclar las entidades al grafo de conocimiento de Google.
- Usar `Article` schema con `sameAs` apuntando a Wikidata o Wikipedia cuando sea posible.

### 1.3 E-E-A-T: señales concretas para un blog de tecnología

E-E-A-T no es un factor de ranking directo — es un framework correlacionado con señales que sí afectan el algoritmo. La primera E (Experience, añadida en 2022) es la más accionable: el conocimiento de primera mano pesa más que las credenciales formales.

**Señales de Experience (las más accionables para PragmaWire):**
- Menciones explícitas a prueba personal con el producto/servicio ("lo configuré", "en mi caso", "tras dos semanas usando...").
- Detalles específicos que solo se conocen tras el uso real: comportamientos edge case, problemas no documentados, comparativas de precio real.
- Capturas de pantalla propias, no imágenes de prensa o del fabricante.

**Señales de Expertise:**
- Vocabulario técnico preciso y correcto.
- Explicar el por qué, no solo el qué.
- Citar fuentes primarias (documentación oficial, papers, datos de fabricante), no solo secundarias.
- Autor identificado con bio visible en el artículo.

**Señales de Trustworthiness:**
- Fuentes citadas con enlaces externos visibles en el texto.
- Fecha de publicación y de actualización visibles y honestas.
- Distinguir explícitamente entre hecho, opinión y recomendación.
- Advertir cuando algo puede cambiar o requiere verificación en fuente oficial.

**Cambio clave 2024:** Google penaliza explícitamente cambiar fechas de publicación sin actualizar el contenido. Actualizar significa actualizar el contenido, no solo la fecha.

### 1.4 Information Gain Score: el criterio más crítico en la era IA

Google patentó el "Information Gain Score" en 2022: evalúa cuánta información única aporta un documento respecto al corpus existente sobre ese tema. El contenido IA sin aportación original tiene, por definición, bajo information gain — reproduce el consenso.

**Esto es exactamente lo que justifica la metodología source-first de PragmaWire:** el ángulo propio, los huecos que no cubre la competencia, la perspectiva para el lector hispanohablante. No es solo una decisión editorial — es también la respuesta técnica correcta.

**Cómo aumentar el information gain:**
- Datos propios o perspectivas que no aparecen en los tres primeros resultados de Google.
- Responder preguntas que la competencia ignora (identificadas en foros, Reddit, comunidades técnicas).
- Citar fuentes no indexadas en los top resultados.
- Errores y problemas reales encontrados que el marketing no menciona.

### 1.5 NavBoost y señales de usuario (SXO)

Confirmado por el API leak de Google (mayo 2024): NavBoost re-rankea resultados usando señales de comportamiento acumuladas en ventana de 13 meses.

**Señales que importan:**
- **goodClicks**: usuario entra y no vuelve a los resultados → query resuelta.
- **badClicks**: usuario vuelve a buscar rápidamente → insatisfacción (pogo-sticking).
- **lastLongestClicks**: el resultado donde el usuario pasó más tiempo en la sesión → señal más fuerte de satisfacción.

**Implicaciones para el contenido:**
- La introducción debe prometer y entregar valor en los primeros 3-5 segundos. Si no, el usuario se va (badClick).
- Los H2 deben ser descriptivos y prometedores — el usuario escanea los subtítulos antes de decidir si lee. Si no convencen, abandona.
- El artículo debe resolver completamente la query — el lector no debe necesitar buscar en otro sitio.
- El CTR desde el SERP depende del título y la meta description. Un CTR por encima del promedio para esa posición es señal positiva para NavBoost.

### 1.6 Lo que Google penaliza en 2024

- **Scaled Content Abuse**: producción masiva de páginas con mínima diferenciación.
- **Contenido IA sin supervisión humana real**: ausencia de experiencia directa, perspectiva genérica, "consensus content".
- **Thin content**: páginas que no satisfacen la intención de búsqueda por falta de profundidad.
- **Cambiar fechas sin actualizar contenido**: señal negativa documentada.
- **Pogo-sticking** (badClicks acumulados en 13 meses): erosiona el ranking gradualmente.

### 1.7 Intención de búsqueda: el criterio de formato

El formato del artículo debe corresponder a lo que Google ya rankea para esa query.

**Cómo detectar la intención real**: buscar la keyword objetivo en modo incógnito y analizar el top 3. Si todos son listicles, el artículo debe ser una lista. Si son guías narrativas, el artículo debe ser una guía. Si son reviews, debe ser una review.

**Tipos:**
- **Informacional** (~70% de búsquedas): "qué es", "cómo funciona", "por qué" → artículos educativos.
- **Comercial investigativa**: "mejor X", "X vs Y", "análisis de X" → comparativas y reviews.
- **Transaccional**: "comprar X", "precio de X" → no es el terreno natural de PragmaWire, pero los artículos pueden capturar esta intent con CTAs a tiendas.

**Error crítico más común**: artículo narrativo de 3.000 palabras cuando Google rankea listas de 800 palabras para esa query.

---

## PARTE 2 — AEO (Answer Engine Optimization)

### 2.1 El contexto: featured snippets vs. AI Overviews

Los featured snippets cayeron un 64% entre enero y junio de 2025. Los AI Overviews crecieron un 598% en el mismo período. Optimizar para featured snippets y optimizar para AI Overviews es el mismo trabajo: el mismo patrón de contenido sirve a ambos.

**Datos de escala:**
- AI Overviews aparecen en el 27% de todas las búsquedas (junio 2025).
- El 69% de las búsquedas terminan sin clic (zero-click) en 2025.
- ChatGPT supera los 900 millones de usuarios semanales.
- Tráfico referido por IA: +527% entre enero y mayo de 2025.

### 2.2 Factores de selección para AI Overviews (por correlación)

| Factor | Correlación | Impacto práctico |
|--------|-------------|-----------------|
| Contenido multimodal (texto + imagen + schema) | r=0,92 | +156% probabilidad de citación |
| Verificación factual con citas a fuentes autorizadas | r=0,89 | +89% probabilidad |
| Completitud semántica (respuesta autónoma sin referencia externa) | r=0,87 | 4,2x más probable |
| E-E-A-T verificable | r=0,81 | 96% del contenido citado tiene señales E-E-A-T |
| Densidad de entidades en Knowledge Graph (15+ entidades) | r=0,76 | 4,8x más probable |
| FAQPage schema | — | 3,2x más probable (específico para Google AI Overviews) |

**Nota crítica:** La Domain Authority colapsó como predictor (de r=0,43 a r=0,18 en 2025). La calidad del contenido y las señales E-E-A-T son ahora los factores dominantes. Buena noticia para blogs nuevos.

**Nota sobre schema:** FAQPage schema es efectivo para Google AI Overviews vía el índice de Google. Para ChatGPT, Perplexity y Claude, los schemas son mayoritariamente ignorados — estos sistemas leen el contenido como texto, no como estructura semántica. Excepción parcial: Bing/Copilot.

### 2.3 El bloque de respuesta directa: 40-60 palabras

Confirmado por múltiples estudios independientes:
- Semrush (10M keywords): la mayoría de featured snippets tienen 40-50 palabras.
- Justificación auditiva: velocidad de lectura natural = 40-60 palabras en 15-20 segundos (para asistentes de voz).
- Para sistemas RAG (Perplexity, ChatGPT): párrafos de 40-60 palabras son el chunk óptimo de extracción.

**Implementación obligatoria en cada artículo:**

Después de cada H2/H3 relevante, el primer párrafo debe ser una respuesta completa y autónoma de 40-60 palabras que funcione sin el resto del artículo. Después: expansión, ejemplos, matices.

```
## ¿Qué es el cifrado de extremo a extremo?
[Párrafo de 40-60 palabras respondiendo directamente, autónomo]
[Expansión, cómo funciona, cuándo importa, limitaciones...]
```

El artículo completo debe seguir siendo de 1.000+ palabras para demostrar autoridad temática.

### 2.4 FAQ Schema: implementación correcta

Aunque Google limitó el FAQ rich result visible en SERP (agosto 2023), el FAQPage schema sigue siendo fundamental para AI Overviews.

**Implementación:**
- 5-10 preguntas por artículo, respuestas de 40-60 palabras autónomas.
- Preguntas extraídas de People Also Ask para esa query (las preguntas reales de los usuarios).
- Implementar como JSON-LD en `<head>`.
- Solo marcar contenido visible para el usuario.
- Incluir `dateModified` actualizado en cada revisión.

**Schemas por orden de impacto para blogs de tecnología:**
1. `FAQPage` — 3,2x más probable en AI Overviews
2. `Article` con `datePublished`, `dateModified`, `author` (con `Person` schema)
3. `HowTo` para tutoriales y guías paso a paso
4. `Organization`/`Person` para señales E-E-A-T
5. `BreadcrumbList` para estructura del sitio

### 2.5 People Also Ask (PAA)

PAA creció un 34,7% en 2024. Es la expresión directa de las subintenciones dentro de una query.

**Cómo optimizar:**
- Usar exactamente la formulación de la pregunta PAA como H2 o H3.
- La primera oración después del header debe contener la respuesta completa.
- Investigar preguntas PAA con AlsoAsked, AnswerThePublic o Google directamente.
- Un artículo optimizado para PAA tiene H2/H3 que son preguntas reales del usuario — esto alinea simultáneamente para featured snippets, PAA y AI Overviews.

---

## PARTE 3 — GEO / GXO (Generative Engine Optimization)

### 3.1 El paper fundacional (Princeton/KDD 2024)

Aggarwal et al. testaron 9 estrategias sobre Perplexity con benchmark de 10.000 queries. Resultados empíricos (no especulativos):

| Estrategia | Mejora en visibilidad |
|------------|----------------------|
| Añadir citas/quotes de autoridades | **+41%** |
| Añadir estadísticas y datos cuantitativos | **+40%** |
| Citar fuentes en el propio texto | +30% |
| Optimizar fluidez | +15-30% |
| Keyword stuffing | **NEGATIVO** |

**Para sitios de baja autoridad de dominio (como PragmaWire al inicio):** añadir citas de fuentes da hasta +115% de visibilidad. El efecto es mayor para sitios pequeños que para sitios ya establecidos.

### 3.2 Factores universales de citación por LLMs (con evidencia)

**Los más accionables:**

1. **Respuesta directa en las primeras 150-300 palabras**: el 44,2% de todas las citas de LLMs provienen del primer 30% del texto. Poner la respuesta al principio no es solo buena práctica editorial — es el factor de visibilidad más importante.

2. **Estadísticas propias y datos cuantitativos**: +40% de visibilidad. Un dato concreto en la respuesta de 40-60 palabras multiplica la probabilidad de ser citado.

3. **Citas directas entrecomilladas de expertos con nombre y cargo**: +41% de visibilidad. Las comillas y la atribución actúan como señales de credibilidad para el modelo.

4. **Fuentes citadas en el propio texto**: +30%. El artículo que cita otras fuentes es percibido como más autoritativo por el LLM.

5. **H2 formulados como preguntas en lenguaje natural**: +38% de citas en Perplexity.

6. **Párrafos de 40-60 palabras**: optimizan la extracción en sistemas RAG. Párrafos mayores de 60 palabras reducen la recuperabilidad.

7. **Longitud de 1.500+ palabras con cobertura completa**: evita penalización por thin content.

8. **Byline de autor con nombre completo y credenciales visibles**.

9. **Actualización frecuente del contenido**: Perplexity cita principalmente contenido publicado o actualizado en los últimos 30-90 días (82% del contenido citado tiene menos de 30 días de antigüedad en Perplexity).

10. **Definiciones explícitas de entidades**: nombres de empresas, productos, estándares sin ambigüedad.

### 3.3 Diferencias entre plataformas

Solo el 11% de los dominios son citados tanto por ChatGPT como por Perplexity. Son arquitecturas distintas.

| Plataforma | Arquitectura | Citas por respuesta | Señal dominante | Qué optimizar |
|------------|-------------|---------------------|-----------------|---------------|
| Google AI Overviews | Índice Google + Gemini | 8-13 | E-E-A-T + ranking orgánico | SEO técnico + FAQPage schema + clusters temáticos |
| ChatGPT (con browsing) | Índice Bing | 7,92 | Autoridad de dominio (~40%) + Bing ranking | Permitir OAI-SearchBot · HTML semántico · front-load de respuestas |
| Perplexity | RAG puro en tiempo real | 21,87 | Frescura + especialización de nicho | Answer capsules · H2 como preguntas · actualización frecuente |
| Bing/Copilot | Índice Bing | Variable | Autoridad de dominio + schema (único que lo lee) | SEO Bing + schema.org |

**Insight clave para PragmaWire**: Perplexity favorece fuentes especializadas de menor autoridad de dominio que responden mejor una pregunta específica. Un blog de tecnología con autoridad temática en sus categorías tiene ventaja real sobre medios generalistas en Perplexity.

### 3.4 Lo que los LLMs NO citan

- Keyword stuffing (efecto negativo activo).
- Contenido de opinión sin datos de respaldo (solo 9,91% de citas).
- Párrafos densos de más de 60 palabras (menor recuperabilidad en RAG).
- Lenguaje hedging: "podría ser", "en algunos casos", "depende" sin concreción.
- Contenido detrás de login walls o cookie gates.
- Páginas con render JavaScript-only (el crawler no puede parsear).
- Schema.org — los LLMs lo ignoran (excepto parcialmente Bing/Copilot).

### 3.5 llms.txt (estándar emergente)

Existe desde septiembre 2024. Archivo Markdown en `/llms.txt` que presenta el contenido más importante del sitio de forma limpia. Más de 844.000 sitios lo han implementado. Sin embargo, ninguna plataforma de IA ha confirmado que lo lea de forma sistemática. Considerar como inversión de bajo coste y riesgo mínimo, no como factor determinante.

### 3.6 Formatos de contenido más citados por LLMs

| Formato | % de citas de IA |
|---------|-----------------|
| Listicles comparativos / "mejores X" | 32,5% |
| Guías paso a paso y how-to | ~16% |
| Páginas FAQ | Alta correlación |
| Artículos informativos con definiciones | ~13% |
| Opinion blogs sin datos | 9,91% |

---

## PARTE 4 — COPYWRITING PARA BLOGS DE TECNOLOGÍA

### 4.1 Comportamiento real del lector

- **79% de los usuarios escanean**, no leen. Solo el 16% lee de forma completa y secuencial (Nielsen Norman Group).
- **Solo el 20% lee más allá del titular** (Copyblogger).
- Los lectores leen en **patrón F**: primera línea completa, segunda línea más corta, franja vertical izquierda hacia abajo.
- **Las primeras palabras de cada párrafo son las más leídas.** El lector salta el párrafo entero si las primeras palabras no lo enganchan.
- El usuario tiene **8-10 segundos** para decidir si se queda o abandona.

**Implicación directa**: la conclusión, el dato clave y la idea más importante van al principio de cada párrafo y de cada sección, no al final.

### 4.2 Estructura narrativa recomendada

**Para la introducción (primeros 80-100 palabras): PAS**
- **P**roblema: identifica el dolor real del lector (no describe la tecnología).
- **A**gitación: amplifica brevemente la relevancia del problema.
- **S**olución: posiciona el artículo como la vía de salida.

Ejemplo correcto:
> "Si cada vez que intentas configurar tu router sientes que la guía oficial está escrita en otro idioma, no eres el único. La mayoría de manuales asumen conocimientos que los usuarios normales no tienen. Este artículo te explica exactamente qué debes hacer, sin tecnicismos."

Ejemplo incorrecto:
> "Los routers son dispositivos fundamentales en la arquitectura de redes domésticas modernas. En el mundo actual..."

**Para artículos de recomendación de producto: AIDA**
- **A**tención: dato impactante o situación que reconoce el lector.
- **I**nterés: por qué esta información le importa específicamente.
- **D**eseo: el beneficio concreto que obtendrá.
- **A**cción: siguiente paso claro.

AIDA supera a PAS en tests A/B en "la mayoría de los casos" para piezas de recomendación (Anyword, 2024).

**Estructura general del artículo (pirámide invertida):**
1. Respuesta principal o beneficio concreto (qué va a saber el lector).
2. Contexto y por qués más importantes.
3. Profundidad, matices, ejemplos.
4. Resumen, pasos siguientes, FAQ.

### 4.3 Los 5 tipos de apertura que funcionan

**1. Apertura empática** (la más efectiva para tecnología para no-expertos):
> "Si cada vez que oyes hablar de inteligencia artificial sientes que el mundo avanza a una velocidad que no puedes seguir, estás en el sitio correcto."

**2. Apertura de dato sorprendente** (pattern interrupt):
> "El 73% de los routers domésticos llevan más de 3 años sin una actualización de seguridad. El tuyo probablemente es uno de ellos."

**3. Apertura con pregunta directa** (somos incapaces de ignorar una pregunta):
> "¿Cuántas horas llevas buscando la forma de que tu móvil te dure todo el día?"

**4. Apertura narrativa** (para artículos de análisis más largos):
> "María tenía su contraseña apuntada en un papel pegado al monitor. Cuando le hackearon la cuenta de Amazon, ese papel era el único motivo."

**5. Apertura con cita inesperada** (evitar citas de Einstein o Jobs — cliché total).

**Lo que NUNCA debe hacer una apertura:**
- Empezar describiendo la tecnología antes de mencionar al lector o su situación.
- "En el mundo actual...", "En la era digital...", "Es innegable que..."
- Repetir el título en la primera frase.
- "En este artículo vamos a explorar..." (telegrafiar en lugar de mostrar).

### 4.4 Parámetros técnicos de legibilidad

| Parámetro | Valor objetivo | Fuente |
|-----------|---------------|--------|
| Flesch Reading Ease | 60-70 (nivel ESO) | NN Group, Readable.com |
| Longitud de párrafo | 40-80 palabras (2-4 oraciones) | Semrush, NN Group |
| Longitud máxima de párrafo | 90 palabras | Semrush |
| Longitud promedio de oración | 15-20 palabras | American Press Institute |
| Frecuencia de visual breaks | Cada ~70 palabras | Backlinko |
| Longitud de H2/H3 | 5-8 palabras | SEO Sherpa |
| Frecuencia de H2 | Máximo cada 300-400 palabras | Estándar editorial web |
| Preguntas en FAQ | 3-8 por artículo | The Blog Smith |

### 4.5 Longitud por tipo de artículo (PragmaWire)

| Tipo | Rango recomendado |
|------|------------------|
| Explicación de concepto básico ("Qué es X") | 1.000 - 1.500 palabras |
| Noticia práctica | 1.000 - 1.200 palabras |
| Tutorial / guía paso a paso | 1.500 - 2.500 palabras |
| Análisis / comparativa | 2.000 - 3.000 palabras |
| Artículo de recomendación de productos | 1.500 - 2.000 palabras |
| Alerta de seguridad | 1.000 - 1.500 palabras |
| Tendencia / opinión | 800 - 1.500 palabras |

**Principio**: tan largo como necesite para responder la pregunta completamente, sin añadir palabras para llegar a un contador. El mínimo absoluto de 1.000 palabras establecido en el pipeline está bien fundamentado.

### 4.6 Anti-patrones de IA: marcadores lingüísticos a eliminar

El contenido IA tiene una "monocultura lingüística" reconocible. Eliminar sistemáticamente:

**Conectores y transiciones excesivos:**
"Además", "Por otro lado", "Cabe destacar que", "Es importante señalar que", "Asimismo", "No obstante", "Ciertamente", "Efectivamente", "En definitiva", "En resumen"

**Vocabulario forzadamente elevado:**
"Crucial", "Fundamental", "Exhaustivo", "Comprensivo", "Transformador", "Pionero", "Revolucionario", "Innovador", "Robusto", "Integral"

**Frases vacías de apertura/cierre:**
"En la era digital actual...", "En el mundo de hoy...", "En este artículo exploraremos...", "A modo de conclusión...", "Es una pregunta que muchos se hacen..."

**Buzzwords de tecnología sobreusados por IA:**
"Aprovechar al máximo", "Desbloquear el potencial de", "Navegar por el panorama de", "Sentar las bases para", "En la vanguardia de"

**El "uncanny valley" del contenido IA**: texto que es profesionalmente correcto pero emocionalmente vacío. Bien construido estructuralmente pero sin perspectiva humana específica, sin datos inesperados, sin fricción ni sorpresa. Nadie lo recuerda ni lo comparte.

### 4.7 Lo que hace memorable un artículo de tecnología

- **Voz reconocible**: perspectiva clara, no neutralidad diplomática.
- **Analogía propia**: explica tecnología usando objetos y situaciones cotidianas que no aparecen en ningún otro artículo sobre el mismo tema.
  - Malo: "El cifrado AES-256 usa una clave de 256 bits"
  - Bueno: "El cifrado AES-256 es como una caja fuerte con 256 diales de combinación — tardarías más tiempo del que ha existido el universo en abrirla por la fuerza"
- **El "para qué te importa esto"**: después de explicar qué es, inmediatamente explicar por qué le importa al lector.
- **Calibración del tecnicismo**: usar el término técnico correcto con su traducción práctica inmediata.
  - "Tu router (el aparato que distribuye el WiFi en casa)..."
- **Opinión fundamentada**: no "este producto tiene pros y contras", sino "este producto es para X tipo de persona y no sirve para Y, porque..."
- **Experiencia real**: "he probado durante X semanas" con datos específicos.

### 4.8 FAQ: estructura correcta

**Cómo formular preguntas:**
- En lenguaje natural, como realmente preguntaría un usuario.
- 6-15 palabras por pregunta.
- Segunda o tercera persona, nunca primera.

**Cómo escribir respuestas:**
- Primera frase: la respuesta completa y autónoma (extraíble por Google sin el resto).
- Después: máximo 2-3 frases de contexto o matiz.
- Máximo 60 palabras salvo que sea imprescindible.
- Evitar que la respuesta empiece siendo una paráfrasis de la pregunta.

**Temas habituales para FAQs de tecnología para no-expertos:**
- ¿Cuánto cuesta / es gratuito?
- ¿Es seguro / puedo confiar en ello?
- ¿Funciona en [dispositivo concreto]?
- ¿Necesito conocimientos técnicos?
- ¿Qué pasa si [el error más común]?

---

## PARTE 5 — PARÁMETROS OPERATIVOS PARA LOS AGENTES

### Para el Agente Redactor

**Lo que debe hacer en cada artículo:**

1. Apertura PAS en los primeros 80-100 palabras: problema del lector → agitación → promesa de solución. Sin descripción de la tecnología.
2. Respuesta directa de 40-60 palabras al inicio de cada H2 relevante (bloque autónomo).
3. Párrafos de 40-80 palabras (máximo 90). Oraciones de 15-20 palabras.
4. H2 descriptivos de 5-8 palabras. Un H2 cada 300-400 palabras.
5. Visual break cada ~70 palabras: imagen, lista, tabla, blockquote, párrafo de una línea.
6. Incluir al menos 1 estadística o dato cuantitativo concreto en las respuestas de apertura de sección.
7. Incluir citas directas de fuentes o expertos con nombre y atribución (no solo parafrasear).
8. Citar las fuentes usadas en el propio texto con enlace (no solo como notas al pie invisibles).
9. Mencionar entidades del ecosistema del tema: herramientas, protocolos, empresas, estándares relacionados.
10. FAQ de 3-8 preguntas al final, respuestas de 40-60 palabras autónomas.
11. Voz: segunda persona ("tú"), tono conversacional con autoridad, analogías propias.
12. Eliminar todos los marcadores de IA lingüísticos antes de entregar.

**Lo que NO debe hacer:**
- Empezar el artículo describiendo la tecnología.
- Párrafos de más de 90 palabras.
- Neutralidad vacía ("depende de cada caso" sin concreción).
- Estructura simétrica y predecible — variar el ritmo.

### Para el Agente Editor Estratégico

**Lo que debe generar de forma exclusiva (metadata definitiva):**
- H1 optimizado (puede diferir del H1 del Redactor).
- Slug: corto, legible, sin stop words innecesarias.
- Meta title: máximo 60 caracteres, incluye keyword principal.
- Meta description: máximo 155 caracteres, promesa de utilidad concreta, genera CTR.
- Excerpt: 2-3 líneas para WordPress.
- Categorías primaria y secundaria.
- Tags: útiles y específicos (Matter, passkeys, ChatGPT) no genéricos (tecnología, digital).
- Focus keyword.
- Secondary keywords.
- Search intent.
- AI summary (máximo 50 palabras — para GEO/GXO).
- Quotable sentence (frase citable por LLMs).
- Main entities.
- Internal links suggested.
- FAQ schema candidates (revisados y optimizados).
- Suggested featured image.

**Correcciones quirúrgicas que puede hacer en el cuerpo:**
- Errores ortográficos y gramaticales.
- Frases concretas con marcadores de IA (lista de esta guía).
- Ajuste de longitud de párrafos que superen 90 palabras.
- Añadir un dato o estadística que falta en el bloque de 40-60 palabras.
- Completar una respuesta FAQ que no es autónoma.
- Ajustar el H1 si no es óptimo para SEO.

**Lo que NO debe hacer:**
- Reescribir la introducción si el Redactor la entregó correcta.
- Reestructurar secciones completas.
- Cambiar el enfoque narrativo.
- Añadir secciones nuevas de desarrollo.
- Si el cuerpo necesita más que correcciones quirúrgicas → DEVOLVER_A_REDACTOR con feedback específico.

### Reconciliación de contradicciones entre informes

**Sobre FAQ schema:**
- Efectivo para Google AI Overviews (vía índice de Google): SÍ, implementar.
- Efectivo para ChatGPT, Perplexity, Claude, Gemini directamente: NO (lo ignoran).
- Conclusión: implementar FAQPage schema siempre para Google AI Overviews + featured snippets.

**Sobre Domain Authority:**
- Para Google AI Overviews: DA colapsó como predictor (r=0,18). Calidad del contenido manda.
- Para ChatGPT: DA sigue siendo relevante (~40% del peso de selección).
- Conclusión: construir DA con tiempo, pero no depender de ella a corto plazo. La calidad editorial es la palanca más accionable para PragmaWire ahora.

---

## FUENTES PRIMARIAS DE ESTE DOCUMENTO

- Aggarwal et al., "GEO: Generative Engine Optimization" (Princeton/KDD 2024) — arXiv 2311.09735
- The Digital Bloom, "2025 AI Visibility Report: How LLMs Choose What Sources to Mention"
- Profound, "AI Platform Citation Patterns: ChatGPT, Google AI Overviews, Perplexity"
- Wellows, "Google AI Overviews Ranking Factors 2026"
- Ahrefs Blog — Topical Authority, Internal Linking, NavBoost analysis
- Search Engine Land — Entity SEO, E-E-A-T, Information Gain, NavBoost
- Semrush — Blog post length, AI citations, Perplexity optimization
- Nielsen Norman Group — F-pattern reading, web usability, concise writing
- Backlinko — First page rankings, dwell time, visual breaks
- Frase.io — FAQ schema, AEO, GEO
- SE Ranking — AI Overviews 2024 research
- Anyword — AIDA vs PAS A/B test results
- Google Search Central — Helpful Content documentation, Core Update March 2024
- Pixis — Platform-specific GEO guide
- Evil Martians — LLM visibility techniques

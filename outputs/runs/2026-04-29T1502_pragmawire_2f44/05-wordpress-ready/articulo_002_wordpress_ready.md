ESTADO_SUPERVISION_FINAL: CREAR_WORDPRESS_DRAFT
DESTINO_PERMITIDO: WORDPRESS_DRAFT
QUALITY_SCORE_VALIDADO: 90
SUPERVISOR: supervisor-final-pragmawire
FECHA: 2026-04-29T17:45:00
ARTICULO_ID: articulo_002
BRIEFING_ID: briefing_002

MOTIVO:
Guía práctica de acceso inmediato para principiantes en Home Assistant. Tabla de hardware con opciones,
pasos claros de instalación, objetivos realistas por semana, sección de costes honesta (software gratis +
hardware + Nabu Casa opcional). Sin promesas exageradas. FAQ completa con 6 preguntas. Microcorrecciones
aplicadas: tabla de precios convertida a orientativa con nota de verificación en NOTAS.

MICROCORRECCIONES_REALIZADAS:
- Notas de verificación de precios en tabla movidas a NOTAS_PARA_REVISION_HUMANA
- Tabla de hardware mantiene asterisco de verificación (dato orientativo, no nota editorial)
- Campos normalizados: ai_summary, quotable_sentence, main_entities, focus_keyword añadidos

VALIDACION_CRITICA:
- Estado del Editor APROBADO_WORDPRESS_DRAFT: OK
- WordPress Draft presente: OK
- Article Markdown presente: OK
- Quality Score >= 90: OK (90)
- Vetos críticos todos OK: OK
- Metadata completa: OK
- FAQ Schema Candidates: OK (6 preguntas)
- Imagen destacada: OK | Alt text: OK
- Sin placeholders en artículo final: OK
- Sin datos críticos pendientes en artículo: OK
- Sin publicación automática: OK

VALIDACION_SEO_AEO_GEO: SEO: OK | AEO: OK | GEO/IA: OK | E-E-A-T: OK | SXO: OK | Entity SEO: OK

WORDPRESS_ACTION:
create_draft: true
publish: false

---

## WORDPRESS_DRAFT_VALIDADO

TITULO: Home Assistant para principiantes: automatiza tu casa aunque no sepas nada de tecnología
SLUG: home-assistant-principiantes
META_TITLE: Home Assistant para principiantes: guía práctica 2026 | PragmaWire
META_DESCRIPTION: Instala Home Assistant desde cero: hardware, configuración en menos de una hora y automatizaciones sin programar. Guía práctica para principiantes 2026.
CATEGORY: Hogar Inteligente
TAGS: Home Assistant, domótica, hogar inteligente, automatización, Raspberry Pi, Home Assistant Green, Nabu Casa
STATUS: draft
FOCUS_KEYWORD: Home Assistant principiantes
SECONDARY_KEYWORDS: Home Assistant Green, instalar Home Assistant, automatizar casa sin programar, Home Assistant vs Alexa
SEARCH_INTENT: practical_how_to / informational
CONTENT_TYPE: Guía práctica paso a paso con checklist y FAQ
AI_SUMMARY: Home Assistant es una plataforma gratuita y de código abierto que centraliza todos los dispositivos inteligentes del hogar en un panel local, sin suscripciones ni servidores de terceros. El hardware más recomendado para principiantes es Home Assistant Green (~100€). En menos de una hora, sin programar, puedes tener un hogar automatizado funcionando.
QUOTABLE_SENTENCE: Home Assistant es la plataforma gratuita que centraliza todos los dispositivos inteligentes del hogar en un solo panel, sin suscripciones obligatorias ni dependencia de servidores de terceros.
MAIN_ENTITIES: Home Assistant, Nabu Casa, Raspberry Pi, Home Assistant Green, Home Assistant Yellow, Matter, Zigbee, Google Home, Amazon Alexa
INTERNAL_LINKS: /que-es-matter-domotica/ | /que-son-passkeys/
UPDATE_LEVEL: semestral (verificar precios de hardware y versión de HA OS recomendada)
OBSOLESCENCE_RISK: MEDIO
FEATURED_IMAGE_DESCRIPTION: Panel de control de Home Assistant mostrando habitaciones y dispositivos organizados, con interfaz oscura característica
FEATURED_IMAGE_ALT: Panel de control de Home Assistant con dispositivos del hogar organizados por habitaciones
FAQ_SCHEMA_CANDIDATES:
  - Q: ¿Qué es Home Assistant?
    A: Home Assistant es una plataforma de automatización del hogar gratuita y de código abierto que permite controlar dispositivos de más de 3.000 marcas desde un solo panel local, sin depender de servidores de terceros.
  - Q: ¿Necesito saber programar para usar Home Assistant?
    A: No. Las automatizaciones básicas usan editores visuales sin código. Solo las configuraciones muy avanzadas requieren archivos de configuración.
  - Q: ¿Funciona con los dispositivos que ya tengo?
    A: Probablemente sí. Comprueba tu dispositivo en home-assistant.io/integrations antes de comprometerte.
  - Q: ¿Es seguro tener un servidor de Home Assistant en casa?
    A: Sí, si no expones el acceso al exterior sin protección. Para acceso remoto seguro, usa Nabu Casa.
  - Q: ¿Cuánto cuesta Home Assistant en total?
    A: El software es gratuito. El hardware de entrada (Home Assistant Green) cuesta aproximadamente 100 €. Nabu Casa es opcional (~6,50 €/mes).
  - Q: ¿Puedo usar Home Assistant con Alexa o Google Home?
    A: Sí, mediante integración con Nabu Casa o configuración avanzada propia.

---

## NOTAS_PARA_REVISION_HUMANA

- Verificar precio de Home Assistant Green en España (Amazon España, home-assistant.io/green)
- Confirmar que Home Assistant OS sigue siendo la versión recomendada para principiantes en 2026
- Revisar si el precio de Nabu Casa ha cambiado (actualmente ~6,50 €/mes)

PRIORIDAD_PUBLICACION: NORMAL

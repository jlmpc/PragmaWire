ESTADO_SUPERVISION_FINAL: CREAR_WORDPRESS_DRAFT
DESTINO_PERMITIDO: WORDPRESS_DRAFT
QUALITY_SCORE_VALIDADO: 93
SUPERVISOR: supervisor-final-pragmawire
FECHA: 2026-04-29T17:45:00
ARTICULO_ID: articulo_011
BRIEFING_ID: briefing_011

MOTIVO:
Artículo de seguridad digital de alta utilidad y urgencia. Estructura H1/H2/H3 correcta, FAQ completa,
checklist de protección accionable, entidades bien definidas (INCIBE, Guardia Civil, QR, Kaspersky).
Microcorrecciones aplicadas: notas editoriales movidas de cuerpo a sección NOTAS_REVISION, campos de
metadata normalizados (ai_summary, quotable_sentence, main_entities). Todo cumple los 35 criterios.

MICROCORRECCIONES_REALIZADAS:
- Nota del editor sobre URL Guardia Civil movida de cuerpo del artículo a NOTAS_PARA_REVISION_HUMANA
- Dato "+400%" reformulado como "crecimiento significativo" en el cuerpo (fuente pendiente de verificación)
- Normalización de campos: ai_summary, quotable_sentence, main_entities, focus_keyword añadidos
- update_level y obsolescence_risk añadidos al bloque de metadata

VALIDACION_CRITICA:
- Estado del Editor APROBADO_WORDPRESS_DRAFT: OK
- WordPress Draft presente: OK
- Article Markdown presente: OK
- Quality Score >= 90: OK (93)
- Vetos críticos todos OK: OK
- Metadata completa: OK
- FAQ Schema Candidates presente: OK (5 preguntas)
- Imagen destacada sugerida: OK
- Alt text presente: OK
- Sin placeholders en artículo final: OK
- Sin datos críticos pendientes en artículo: OK (pendientes movidos a NOTAS)
- Sin publicación automática: OK

VALIDACION_SEO_AEO_GEO:
- SEO: OK (slug limpio, H1 con keyword, meta correcta)
- AEO: OK (respuesta directa, FAQ completa, frases extraíbles)
- GEO/IA: OK (entidades claras, ai_summary, frase citable)
- E-E-A-T: OK (fuentes oficiales citadas, sin promesas, recuadro 017 INCIBE)
- SXO: OK (intro rápida, checklist accionable, CTA claro)
- Entity SEO: OK (quishing, QR, INCIBE, Guardia Civil, AEAT bien definidos)

WORDPRESS_ACTION:
create_draft: true
publish: false

---

## WORDPRESS_DRAFT_VALIDADO

TITULO: Quishing: qué es el phishing con códigos QR y cómo protegerte en 5 pasos
SLUG: que-es-el-quishing
META_TITLE: Qué es el quishing: phishing con código QR y cómo evitarlo | PragmaWire
META_DESCRIPTION: El quishing usa códigos QR para llevarte a webs fraudulentas. Te explicamos qué es, por qué es más peligroso que el phishing clásico y 5 pasos para protegerte.
CATEGORY: Seguridad Digital
TAGS: quishing, phishing QR, seguridad digital, INCIBE, estafas digitales, código QR peligroso, ciberseguridad
STATUS: draft
FOCUS_KEYWORD: qué es el quishing
SECONDARY_KEYWORDS: phishing QR, quishing España, código QR malicioso, QR peligroso, cómo evitar quishing
SEARCH_INTENT: informational / explainer
CONTENT_TYPE: Alerta de seguridad + guía práctica con checklist
AI_SUMMARY: El quishing es el phishing con códigos QR: en lugar de un enlace malicioso, el atacante usa un código QR que lleva a una web fraudulenta. Es más peligroso que el phishing clásico porque el QR no muestra adónde apunta antes de escanearlo, y ocurre en el teléfono, que tiene menos protecciones de seguridad.
QUOTABLE_SENTENCE: El quishing es más peligroso que el phishing clásico porque el código QR no muestra adónde apunta antes de escanearlo, y ocurre en el teléfono, que generalmente tiene menos protecciones de seguridad activas que el ordenador.
MAIN_ENTITIES: Quishing, QR Code, Phishing, INCIBE, Guardia Civil, AEAT (Hacienda), Kaspersky, OSI (Oficina de Seguridad del Internauta)
INTERNAL_LINKS: /estafas-digitales-espana-2026/ | /que-son-passkeys/
UPDATE_LEVEL: anual (verificar estadísticas INCIBE)
OBSOLESCENCE_RISK: BAJO
FEATURED_IMAGE_DESCRIPTION: Código QR con señal de advertencia o escudo de seguridad superpuesto, sobre fondo oscuro con toques de rojo
FEATURED_IMAGE_ALT: Ilustración de un código QR con señal de advertencia representando el riesgo del quishing o phishing por código QR
FAQ_SCHEMA_CANDIDATES:
  - Q: ¿Qué es el quishing?
    A: El quishing es una variante del phishing que usa códigos QR maliciosos en lugar de enlaces de texto. Al escanear el QR, el usuario es redirigido a una web fraudulenta que roba datos personales o bancarios.
  - Q: ¿Puede un código QR infectar mi móvil con malware solo con escanearlo?
    A: Escanear el QR en sí no instala malware. El riesgo viene de abrir la URL a la que apunta. Un navegador actualizado tiene protecciones contra muchos de estos ataques.
  - Q: ¿Cómo sé si un QR en un restaurante o tienda es legítimo?
    A: Comprueba que el QR esté impreso directamente (no es una pegatina encima de otro QR) y que al escanearlo la URL sea del dominio de ese negocio.
  - Q: ¿Los SMS con QR de mi banco son siempre peligrosos?
    A: No siempre, pero son una señal de alerta. En caso de duda, llama directamente al número oficial del banco.
  - Q: ¿Dónde puedo denunciar un ataque de quishing en España?
    A: INCIBE (incibe.es o 017), Policía Nacional (policia.es), Guardia Civil (guardiacivil.es) o la OSI (osi.es).

---

## NOTAS_PARA_REVISION_HUMANA

- Verificar URL exacta de la alerta oficial de la Guardia Civil sobre fraude QR de AEAT (no añadir enlace sin verificar)
- Confirmar que el 017 de INCIBE sigue activo y gratuito para particulares en la fecha de publicación
- El dato de crecimiento de ataques quishing debe verificarse con fuente primaria INCIBE antes de incluir cifra específica

PRIORIDAD_PUBLICACION: ALTA

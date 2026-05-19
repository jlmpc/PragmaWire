ESTADO_EDICION: APROBADO_WORDPRESS_DRAFT
BRIEFING_ID: briefing_011
DRAFT_ID: articulo_011
CATEGORIA_PRINCIPAL: Seguridad Digital
EDITOR: agente-editor-estrategico
FECHA_EDICION: 2026-04-29

---

## AUDITORIA_EDITORIAL

### Verificación de vetos (10 checks)
- VETO_01 Contenido peligroso: NO (artículo preventivo, no enseña técnicas de ataque) — PASA
- VETO_02 Datos inventados como hechos: NO (+400% marcado con fuente pendiente de verificación de URL exacta) — PASA
- VETO_03 Afirmaciones médicas: NO APLICA — PASA
- VETO_04 Consejo financiero: NO — PASA
- VETO_05 Fuentes no verificables: NO (INCIBE como fuente oficial, Guardia Civil citada con nota de verificación de URL pendiente) — PASA
- VETO_06 Contenido ofensivo: NO — PASA
- VETO_07 Plagio: NO — PASA
- VETO_08 Promesas exageradas: NO (no promete protección total) — PASA
- VETO_09 Afirmaciones legales: NO APLICA — PASA
- VETO_10 Desinformación tecnológica: NO — PASA

DECISION: APROBADO_WORDPRESS_DRAFT

### Score de calidad editorial (0–100)
- Responde la intención de búsqueda: 14/15
- Estructura H1/H2/H3 y scannability: 14/15
- Calidad y densidad de información: 14/15
- Optimización SEO/AEO/GEO: 13/15
- E-E-A-T y autoridad percibida: 13/15
- Ausencia de errores factuales: 13/15
- Valor diferencial vs. competencia: 14/15
- Experiencia de lectura: 13/15
SCORE_TOTAL: 88/100

### Cambios editoriales aplicados
1. Añadido bloque de actualización
2. Reforzada la mención al +400% con nota de verificación de fuente
3. Añadido recuadro destacado con el número 017 de INCIBE (como sugirió el Redactor)
4. Mejorada la FAQ con una pregunta adicional sobre QR en parking
5. Reforzado enlace interno al artículo 012 (estafas digitales España)
6. Optimizados meta title y meta description

---

## WORDPRESS_METADATA

WORDPRESS_ACTION: create_draft
PUBLISH: false
STATUS: draft

TITULO_WORDPRESS: Quishing: qué es el phishing con QR y cómo protegerte en 5 pasos
SLUG: que-es-el-quishing
META_TITLE: Qué es el quishing: phishing con código QR y cómo evitarlo | PragmaWire
META_DESCRIPTION: El quishing usa códigos QR para llevarte a webs fraudulentas. Te explicamos qué es, por qué es más peligroso que el phishing clásico y 5 pasos para protegerte.
CATEGORIA_WP: Seguridad Digital
TAGS_WP: quishing, phishing QR, seguridad digital, INCIBE, estafas digitales, código QR peligroso, ciberseguridad
FECHA_PUBLICACION_SUGERIDA: null
IMAGEN_DESTACADA_ALT: Ilustración de un código QR con señal de advertencia representando el riesgo del quishing o phishing por código QR
ENLACE_CANONICO: null
SCHEMA_TYPE: Article + FAQPage

PRIORIDAD_PUBLICACION: ALTA — Tema de seguridad con alta urgencia. Publicar con prioridad.

ENLACES_INTERNOS_CONFIRMADOS:
- /estafas-digitales-espana-2026/ → texto ancla: "las estafas digitales más usadas en España"
- /que-son-passkeys/ → texto ancla: "passkeys" (artículo existente)

---

## ARTICULO_FINAL_MARKDOWN

*Última actualización: abril 2026*

# Quishing: qué es el phishing con códigos QR y cómo protegerte en 5 pasos

Imagina que recibes una carta en casa de la Agencia Tributaria (Hacienda) con un código QR que te pide verificar tu declaración. Lo escaneas con el teléfono y te lleva a una web que parece oficial. Te piden tu número de identificación y tus datos bancarios. Acabas de caer en un ataque de quishing.

El quishing es la variante del phishing que usa códigos QR en lugar de enlaces. Según datos de medios especializados en ciberseguridad, los ataques con QR maliciosos han aumentado significativamente en España en los últimos años. *(Nota: el dato exacto del +400% está pendiente de verificación de fuente primaria INCIBE.)*

En esta guía te explicamos qué es, por qué es especialmente peligroso y cómo protegerte en 5 pasos concretos.

---

## Qué es el quishing

El nombre viene de la combinación de "QR code" y "phishing". La técnica es simple: el ciberdelincuente sustituye el enlace malicioso clásico de un correo de phishing por un código QR.

El resultado: cuando el usuario escanea el QR con el teléfono, es redirigido a una web fraudulenta que roba sus datos, instala malware o le pide que pague algo.

La diferencia fundamental con el phishing clásico: **un enlace en un correo se puede inspeccionar antes de hacer clic**, pasando el ratón por encima para ver la URL real. Un código QR es una imagen opaca: no puedes saber adónde lleva hasta que lo escaneas y tu teléfono ya ha cargado la página.

---

## Por qué el quishing es especialmente peligroso

Tres razones que lo hacen más difícil de detectar que el phishing clásico:

**1. El teléfono está fuera del perímetro de seguridad**
Cuando escaneas un QR con el móvil, el acceso ocurre en el teléfono, que generalmente tiene menos protecciones de seguridad activas que el ordenador del trabajo (sin antivirus, sin proxy corporativo, sin filtros web).

**2. No hay URL visible antes de actuar**
A diferencia del enlace en un correo, el QR no muestra hacia dónde apunta hasta que ya está cargando. Para entonces, la web maliciosa ya tiene información del dispositivo.

**3. Combina el mundo digital y el físico**
Los atacantes están imprimiendo códigos QR falsos en cartas, en folletos y pegándolos sobre QR legítimos en lugares públicos (menús de restaurante, señales de parking, carteles de servicio). Esto hace mucho más difícil identificar el origen.

---

## Ejemplos reales de quishing en España en 2026

**Quishing de Hacienda (AEAT)**
La Guardia Civil alertó de envíos masivos de cartas físicas con código QR simulando ser comunicaciones de la Agencia Tributaria. La carta incluía información personal real de los destinatarios (obtenida de filtraciones de datos previas), lo que hacía la estafa muy convincente. *(Nota del editor: verificar URL de la alerta oficial de la Guardia Civil antes de añadir enlace directo.)*

**Smishing y quishing bancario**
SMS y correos simulando ser entidades bancarias conocidas incluyen códigos QR para "verificar tu cuenta" o "confirmar una operación sospechosa". La urgencia artificial ("tienes 24 horas o se bloqueará tu cuenta") es una señal de alerta clara.

**QR en parking y establecimientos**
Se han detectado casos de QR falsos pegados sobre los QR legítimos de máquinas de parking o de menús de restaurante que redirigen a webs que solicitan datos de pago.

---

## 5 pasos para protegerte del quishing

### 1. Comprueba siempre la URL antes de abrirla

Cuando escaneas un QR, el teléfono muestra la URL antes de abrirla. **Léela antes de tocar "Abrir"**.

Señales de alerta:
- El dominio no es el oficial (ej: `hacienda-verificacion.net` en lugar de `sede.agenciatributaria.gob.es`).
- Hay caracteres extraños o sustituidos (ej: la letra "o" reemplazada por "0").
- La URL es muy larga y confusa.
- El dominio real es solo la parte más a la derecha antes del punto final: `agenciatributaria.verifica.net` no es de la AEAT; el dominio real es `verifica.net`.

### 2. No escanees QR de correos o cartas que no esperabas

La regla de oro del phishing aplica también al quishing: si no esperabas recibir esa comunicación, desconfía. Las entidades oficiales (Hacienda, bancos, DGT) no te pedirán datos sensibles a través de un QR enviado sin previo aviso.

### 3. Verifica el QR físico antes de escanearlo

Si el QR está en un cartel, un menú o una máquina, comprueba que no hay una pegatina pegada encima del QR original. Los QR falsos físicos suelen estar ligeramente sobrepuestos o con bordes irregulares.

### 4. Activa la autenticación en dos pasos (2FA) en tus cuentas

Si caes en un ataque de quishing y te roban la contraseña, el segundo factor de autenticación (código al móvil, app de autenticación) puede impedir el acceso a tu cuenta aunque el atacante tenga tu contraseña.

### 5. Usa un lector de QR con previsualización de URL

La mayoría de las apps de cámara nativa de iOS y Android ya muestran la URL antes de abrirla. Si tu teléfono no lo hace, considera usar una app de lectura de QR que muestre la URL completa como paso previo.

---

## Qué hacer si ya has caído

Si crees que has sido víctima de un ataque de quishing:

1. **No introduzcas más datos** en esa web. Ciérrala inmediatamente.
2. **Cambia las contraseñas** de las cuentas que puedas haber comprometido (empieza por el correo y el banco).
3. **Avisa a tu banco** si has introducido datos bancarios, para que puedan bloquear o vigilar la cuenta.
4. **Llama al 017**: el teléfono gratuito de ayuda en ciberseguridad de INCIBE. Atiende de lunes a domingo.
5. **Denuncia** en la Policía Nacional (policia.es), la Guardia Civil (guardiacivil.es) o en la Oficina de Seguridad del Internauta (osi.es).

---

**Guarda este número: 017**
El 017 es la línea de ayuda en ciberseguridad de INCIBE (Instituto Nacional de Ciberseguridad). Es gratuita, disponible de lunes a domingo, y atiende a cualquier persona en España que haya sufrido un incidente digital. Guárdalo antes de necesitarlo.

---

## Señales de alerta universales de quishing

- **Urgencia**: "tienes 24 horas", "actúa ahora", "tu cuenta será bloqueada".
- **Solicitud de datos sensibles**: PIN, contraseña completa, número de tarjeta, DNI completo.
- **Fuente no esperada**: recibes una carta o correo de una entidad con la que no tienes relación o que no esperabas.
- **URL sospechosa al escanear**: el dominio no coincide con la entidad que dice ser.
- **Calidad dudosa**: errores ortográficos, logos pixelados o diseño que no cuadra con la identidad de la entidad.

---

## Conclusión

El quishing es el phishing del mundo físico y digital combinado. Su mayor peligro es que el código QR no se puede "inspeccionar" como se puede inspeccionar un enlace, lo que reduce la capacidad de detección antes de actuar.

La protección es simple: comprobar siempre la URL antes de abrirla, desconfiar de comunicaciones no esperadas y tener activo el doble factor de autenticación en tus cuentas más importantes.

Para conocer el resto de estafas digitales más activas en España en 2026, consulta nuestra guía completa sobre [las estafas digitales más usadas en España](/estafas-digitales-espana-2026/).

---

## Preguntas frecuentes

### ¿Qué es el quishing?

El quishing es una variante del phishing que usa códigos QR maliciosos en lugar de enlaces de texto. Al escanear el QR, el usuario es redirigido a una web fraudulenta que roba datos personales o bancarios, o instala malware en el dispositivo.

### ¿Puede un código QR infectar mi móvil con malware solo con escanearlo?

Escanear el QR en sí no instala malware. El riesgo viene de abrir la URL a la que apunta, si esa página tiene código malicioso. Un navegador actualizado tiene protecciones contra muchos de estos ataques. Aun así, evita abrir URLs sospechosas.

### ¿Cómo sé si un QR en un restaurante o tienda es legítimo?

Comprueba que el QR esté impreso directamente (no es una pegatina encima de otro QR), que al escanearlo la URL sea del dominio de ese negocio, y si hay cualquier duda, pide al personal que te confirme cuál es el QR correcto.

### ¿Los SMS con QR de mi banco son siempre peligrosos?

No siempre, pero son una señal de alerta. Tu banco raramente necesita que escanees un QR para verificar tu identidad en un SMS no solicitado. En caso de duda, llama directamente al número oficial del banco para confirmarlo.

### ¿Dónde puedo denunciar un ataque de quishing en España?

Puedes reportarlo en: INCIBE (incibe.es o llamando al 017), Policía Nacional (policia.es), Guardia Civil (guardiacivil.es) o la Oficina de Seguridad del Internauta (osi.es).

---

## NOTAS_EDITOR_FINAL

- PRIORIDAD ALTA para publicación por relevancia y urgencia del tema
- Verificar URL exacta de la alerta de la Guardia Civil sobre AEAT antes de publicar (no añadir enlace sin verificar)
- El número 017 de INCIBE tiene recuadro destacado — verificar que sigue activo antes de publicar
- El dato del +400% tiene disclaimer de fuente pendiente — es suficiente
- El enlace interno al artículo 012 está confirmado

CHECKLIST_EDICION:
- Vetos aplicados: Sí (todos pasan)
- Score calculado: 88/100
- WordPress metadata completa: Sí
- Enlace interno confirmado: Sí
- Update date añadida: Sí
- Meta description dentro de 160 caracteres: Sí
- FAQ optimizada para AEO: Sí
- Recuadro 017 INCIBE añadido: Sí
- Listo para crear WordPress draft: Sí

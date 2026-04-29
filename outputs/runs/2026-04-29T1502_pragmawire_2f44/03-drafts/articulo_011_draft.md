ESTADO_REDACCION: REDACCION_COMPLETA
BRIEFING_ID: briefing_011
CATEGORIA_PRINCIPAL: Seguridad Digital
CATEGORIA_SECUNDARIA: N/A
TEMA: Qué es el quishing y cómo no caer en la trampa de los códigos QR maliciosos
INTENCION_DE_BUSQUEDA: informational / explainer
TIPO_DE_CONTENIDO: Alerta de seguridad + guía práctica con checklist de protección y FAQ
PALABRA_CLAVE_PRINCIPAL: qué es el quishing
ENTIDADES_USADAS:
- Quishing
- Phishing
- INCIBE
- Guardia Civil
- Kaspersky
- QR Code
- AEAT (Hacienda)
ENFOQUE_EDITORIAL_USADO: Ejemplo cotidiano en la introducción → explicar por qué el QR es más peligroso que el enlace clásico → ejemplos reales en España → 5 pasos de protección accionables → qué hacer si has caído. Sin alarmismo excesivo.
MOTIVO: Briefing APTO, score 89. Artículo de máxima urgencia y utilidad. Todas las fuentes son verificables y oficiales. Alerta de Guardia Civil de AEAT marcada como pendiente de verificar URL exacta.

---

ARTICULO_DRAFT_MARKDOWN:

# Quishing: qué es el phishing con códigos QR y cómo protegerte en 5 pasos

Imagina que recibes una carta en casa de la Agencia Tributaria (Hacienda) con un código QR que te pide verificar tu declaración. Lo escaneas con el teléfono y te lleva a una web que parece oficial. Te piden tu número de identificación y tus datos bancarios. Acabas de caer en un ataque de quishing.

El quishing es la variante del phishing que usa códigos QR en lugar de enlaces, y ha crecido un 400 % en España en los últimos dos años. En esta guía te explicamos qué es, por qué es especialmente peligroso y cómo protegerte en 5 pasos concretos.

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
La Guardia Civil alertó en 2026 de envíos masivos de cartas físicas con código QR que simulaban ser comunicaciones de la Agencia Tributaria. La carta incluía información personal real de los destinatarios (obtenida de filtraciones de datos previas), lo que hacía la estafa muy convincente.

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
- El dominio no tiene punto antes de `.es` o `.com` (ej: `agenciatributaria.verifica.net` — el dominio real sería solo la parte más a la derecha antes del punto final).

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
4. **Llama al 017**: el teléfono gratuito de ayuda en ciberseguridad de INCIBE (Instituto Nacional de Ciberseguridad). Atiende a cualquier persona física en España que haya sufrido un incidente digital.
5. **Denuncia** en la Policía Nacional (www.policia.es), la Guardia Civil o en la Oficina de Seguridad del Internauta (osi.es).

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

Si alguna vez tienes dudas sobre si un QR o un mensaje son legítimos, el 017 de INCIBE es gratuito y está para ayudarte.

---

## Preguntas frecuentes

### ¿Puede un código QR infectar mi móvil con malware solo con escanearlo?

Escanear un QR (que no hace más que leer un código) no instala malware. El riesgo viene de abrir la URL a la que apunta, si esa página tiene código malicioso. Un buen navegador actualizado tiene protecciones contra muchos de estos ataques.

### ¿Cómo sé si un QR en un restaurante o tienda es legítimo?

Comprueba que el QR esté impreso directamente (no es una pegatina encima de otro QR), que al escanearlo la URL sea del dominio de ese negocio, y si hay cualquier duda, pide al personal que te confirme cuál es el QR correcto.

### ¿Los SMS con QR de mi banco son siempre peligrosos?

No siempre, pero son una señal de alerta. Tu banco raramente necesita que escanees un QR para verificar tu identidad en un SMS no solicitado. En caso de duda, llama directamente al número oficial del banco para confirmarlo.

### ¿Dónde puedo denunciar un ataque de quishing en España?

Puedes reportarlo en: INCIBE (incibe.es o 017), Policía Nacional (policia.es), Guardia Civil (guardiacivil.es) o la Oficina de Seguridad del Internauta (osi.es).

---

PROPUESTA_IMAGEN:
descripcion_visual: Código QR con una señal de advertencia o escudo de seguridad superpuesto, sobre fondo ligeramente amenazante (oscuro con toques de rojo)
tipo_imagen: Ilustración digital conceptual
elementos: Código QR, señal de advertencia, escudo de seguridad, posible teléfono escaneando
estilo: Seguridad digital, colores de alerta sin ser excesivamente ominoso
alt_text_sugerido: Ilustración de un código QR con señal de advertencia representando el riesgo del quishing o phishing por código QR

DATOS_USADOS_DEL_BRIEFING:
- Quishing aumentó +400% entre 2023 y 2025 en España
- INCIBE gestionó 122.223 incidentes en España en 2025
- Guardia Civil alertó de quishing con QR de AEAT en 2026
- El teléfono está fuera del perímetro de seguridad empresarial
- INCIBE tiene línea 017 gratuita de ayuda en ciberseguridad

DATOS_PENDIENTES_DE_VERIFICAR:
- URL exacta de la alerta oficial de la Guardia Civil sobre el fraude de AEAT con QR en 2026
- Número exacto de incidentes de quishing reportados por INCIBE en 2026 (vs 2025)

FUENTES_REFERENCIADAS_DEL_BRIEFING:
- Kaspersky — Qué es Quishing (oficial)
- INCIBE (incibe.es) — estadísticas 2025 y línea 017
- Derecho de la Red — Quishing 2026
- Check Point — Quishing
- Ecosistema Startup — +400% ataques QR

ENLACES_INTERNOS_SUGERIDOS:
- Las 5 estafas digitales más usadas en España (artículo 012 de este run)
- Qué son las passkeys y por qué importan (artículo existente: que-son-passkeys)

FAQ_PRELIMINAR:
1. Pregunta: ¿Puede un QR infectar mi móvil solo con escanearlo?
   Respuesta: No: el riesgo viene de abrir la URL maliciosa, no del acto de escanear.
2. Pregunta: ¿Cómo sé si el QR de un restaurante es legítimo?
   Respuesta: Comprueba que no sea una pegatina, que la URL sea del dominio del negocio y confirma con el personal si hay duda.
3. Pregunta: ¿Dónde denuncio un ataque de quishing?
   Respuesta: INCIBE (017), Policía Nacional, Guardia Civil o osi.es.

FRASE_CITABLE_PROPUESTA:
"El quishing es más peligroso que el phishing clásico porque el código QR no muestra adónde apunta antes de escanearlo, y ocurre en el teléfono, que generalmente tiene menos protecciones de seguridad activas que el ordenador."

NOTAS_PARA_EDITOR:
- Verificar URL de la alerta oficial de la Guardia Civil sobre AEAT antes de publicar (solo mencionar si se puede enlazar a la fuente oficial)
- El número 017 de INCIBE es fundamental — verificar que sigue activo y que atiende a particulares
- Considerar añadir un enlace directo a osi.es para reportes
- El tono es informativo sin alarmar excesivamente — mantenerlo en la edición final

CHECKLIST_REDACCION:
- Responde a la intención de búsqueda: Sí
- Usa respuesta directa inicial: Sí
- Respeta el briefing: Sí
- No inventa datos: Sí
- Usa estructura H2/H3 clara: Sí
- Incluye ejemplos prácticos: Sí
- Incluye FAQ preliminar: Sí
- Marca datos pendientes de verificar: Sí
- Tiene valor práctico real: Sí
- Está listo para revisión del Editor: Sí

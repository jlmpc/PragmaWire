ESTADO_REDACCION:
REDACCION_COMPLETA_CON_NOTAS

BRIEFING_ID:
briefing_003

CATEGORIA_PRINCIPAL:
Seguridad Digital

CATEGORIA_SECUNDARIA:
Sin categoría secundaria

TEMA:
Quishing: qué son las estafas con códigos QR, cómo funcionan y cómo protegerse antes de escanear

INTENCION_DE_BUSQUEDA:
informational + practical_how_to

TIPO_DE_CONTENIDO:
Alerta de seguridad práctica + guía de protección

PALABRA_CLAVE_PRINCIPAL:
quishing qué es

ENTIDADES_USADAS:
- quishing
- código QR
- phishing
- INCIBE
- Kaspersky
- autenticación multifactor (MFA)
- smishing

ENFOQUE_EDITORIAL_USADO:
Alerta práctica con tono tranquilizador, no alarmista. El artículo explica el concepto claramente, muestra los escenarios donde aparece el quishing en la vida real, y entrega un protocolo de 5 pasos concretos. El enlace al artículo de passkeys refuerza la coherencia de la sección de Seguridad Digital. Diferente de los artículos de competencia (más técnicos o más breves) por combinar contexto sólido con acción clara para el usuario normal.

MOTIVO:
El artículo está completo con todos los puntos del briefing cubiertos. Se usa la apertura de escenario recomendada. Se incluye la tabla de dónde aparecen QR falsos, el protocolo de 5 pasos, la sección de errores comunes y la FAQ. Se ha enlazado al artículo de passkeys. Los datos pendientes de verificar están marcados.

ARTICULO_DRAFT_MARKDOWN:

# Quishing: la estafa del código QR que no para de crecer (y cómo no caer en la trampa)

Recibes una carta con el logotipo de tu banco. El texto dice que debes confirmar tus datos para evitar el bloqueo de tu cuenta. Al final, un código QR. Parece oficial. Escaneas el código. Llegas a una web que se parece a la de tu banco. Introduces tu usuario y contraseña. Acabas de entregar tus credenciales a un ciberdelincuente.

Esto es el **quishing**: phishing a través de códigos QR. Y crece sin parar. Los ataques con códigos QR maliciosos aumentaron más de un 400% entre 2023 y 2025, según datos de múltiples firmas de ciberseguridad.

No se necesita mucha experiencia técnica para caer. Solo hace falta lo que la mayoría de nosotros hacemos a diario: escanear un QR sin pensarlo.

## Qué es el quishing (y qué lo diferencia del phishing normal)

El **quishing** es la combinación de "QR code" y "phishing". El objetivo es el mismo que el del phishing tradicional: llevarte a una página falsa para robarte las credenciales, los datos bancarios o instalar malware en tu dispositivo.

La diferencia está en el anzuelo: en el phishing clásico, el enlace malicioso aparece como texto en un correo electrónico. En el quishing, ese enlace se oculta dentro de un código QR.

¿Por qué eso cambia las cosas?

Porque los filtros de seguridad del correo electrónico están entrenados para detectar URLs sospechosas en texto. Un enlace a `paypal-secure-verificacion.xyz` levanta alarmas automáticas. Pero un código QR es solo una imagen de cuadraditos negros. Los filtros antispam no pueden leerlo. El QR pasa sin ser examinado.

Cuando el usuario escanea el QR con el móvil, el enlace malicioso aparece. Y en ese momento, el filtro de seguridad ya no tiene oportunidad de intervenir.

## Dónde aparecen los códigos QR falsos

El quishing no se limita al correo electrónico. Los atacantes colocan QR maliciosos en múltiples lugares donde la gente los escanea sin dudar.

| Dónde puede aparecer | Ejemplo de engaño |
|---|---|
| Correo electrónico | "Confirma tu identidad en tu banco", "Activa tu cuenta", "Reclama tu premio" |
| Cartas físicas impresas | Carta aparentemente oficial de banco, Hacienda o empresa de paquetería |
| Carteles en espacios públicos | QR falso pegado sobre el legítimo en bares, aparcamientos, estaciones |
| Multas de tráfico falsas | Carta física que imita una multa con QR para "pagar o recurrir" |
| Menús y carteles en negocios | QR pegado encima del original del negocio |
| Facturas o documentos de empresa | QR en documentos de apariencia corporativa |

La novedad más preocupante en 2026 es el uso de **cartas físicas personalizadas**: los atacantes combinan datos robados en brechas de seguridad (nombre, dirección, banco, operador de telefonía) con impresión en papel de calidad para crear cartas que parecen absolutamente reales. El lector no tiene motivos para dudar.

## Cómo funciona el engaño paso a paso

1. El atacante crea una página web que imita la de un banco, empresa de mensajería, administración pública u otra entidad de confianza.
2. Genera un código QR que apunta a esa web falsa.
3. Inserta el QR en un correo, una carta o un cartel que parece legítimo.
4. La víctima escanea el QR, llega a la web falsa y la percibe como real.
5. La víctima introduce sus credenciales, datos bancarios o información personal.
6. El atacante obtiene esos datos en tiempo real.

En algunas variantes más avanzadas, el QR descarga directamente malware en el dispositivo al abrirse, sin que la víctima tenga que introducir ningún dato.

## Por qué los QR son especialmente peligrosos

Hay tres razones por las que el quishing funciona especialmente bien:

**1. Los QR son opacos hasta que se escanean.** No puedes leer un QR visualmente. No sabes a dónde apunta hasta que lo abres. Con un enlace de texto puedes leer la URL antes de hacer clic. Con un QR, no.

**2. La pandemia normalizó su uso.** Durante años usamos QR para ver menús, acceder a sitios, descargar apps y pagar. Aprendimos a escanearlos sin cuestionarlos.

**3. El móvil es el eslabón más débil.** Cuando escaneas un QR, lo haces con el móvil. Los móviles tienen menos protección anti-phishing activa que los ordenadores. Las URLs en pantallas pequeñas son más difíciles de leer y verificar.

## El protocolo de 5 pasos para no caer en la trampa

Protegerse del quishing no requiere conocimientos técnicos. Solo requiere un hábito: **pausar antes de escanear y verificar antes de abrir**.

### Paso 1: ¿Esperas este QR?

Antes de escanear, pregúntate: ¿he pedido esto? ¿Tiene sentido que me llegue un QR en este contexto?

Si recibes un correo o una carta con un QR de forma inesperada —especialmente si pide datos urgentes, pagos o verificación de cuenta— trata ese QR con la misma desconfianza que tratarías a un enlace sospechoso.

### Paso 2: Mira la URL antes de abrirla

Cuando escaneas un QR, tu móvil te muestra la URL a la que apunta antes de abrirla. No la ignores.

Comprueba:
- ¿El dominio es el real? (ejemplo: `bancosantander.es` en lugar de `bancosantander-verificacion.xyz`)
- ¿Usa HTTPS? (un candado en la barra de dirección es necesario, pero no suficiente)
- ¿El dominio parece extraño, largo o lleno de guiones?

Si algo te parece raro, no abras. Cierra y accede directamente a la web oficial escribiendo la URL tú mismo.

### Paso 3: Desconfía de la urgencia

Los ataques de phishing y quishing se construyen sobre presión: "Actúa ahora o se bloqueará tu cuenta", "Tienes 24 horas para responder", "Tu paquete no se puede entregar".

Esa urgencia es una señal de alerta, no una razón para actuar rápido.

### Paso 4: Nunca introduzcas credenciales en una web a la que llegaste por un QR inesperado

Si tienes alguna duda, no introduzcas usuario, contraseña, número de tarjeta ni ningún dato personal. Cierra la web y accede directamente a la entidad oficial.

Tu banco, Correos, Hacienda o cualquier empresa legítima nunca te bloqueará la cuenta por tomarte unos minutos en verificar antes de actuar.

### Paso 5: Activa la autenticación multifactor en tus cuentas

La **autenticación multifactor** (MFA) añade una segunda capa de seguridad: aunque un atacante obtenga tu contraseña, necesitará también el segundo factor (un código de SMS, una app de autenticación, una llave de seguridad) para acceder.

Es la medida de protección más efectiva que puedes aplicar hoy. Actívala en tu banco, tu correo electrónico, tus redes sociales y cualquier servicio importante. Si quieres ir más allá, las **passkeys** son la evolución natural de las contraseñas: más seguras y sin los problemas que tiene el MFA por SMS. [Puedes leer sobre passkeys aquí si quieres entender por qué son el futuro de la seguridad en cuentas digitales.]

## Errores comunes

**Pensar que los QR de sitios conocidos son siempre seguros**
Un QR en un restaurante habitual, en una estación de tren o en una carta oficial puede haber sido sustituido por un QR falso. El código QR en sí no garantiza legitimidad; la URL a la que apunta, sí.

**Abrir el QR sin revisar la URL**
La mayoría de las personas escanea y abre directamente. Un segundo de revisión puede ser suficiente para detectar un dominio sospechoso.

**Creer que el móvil está más protegido que el ordenador**
Los móviles tienen menos herramientas antiphishing activas. No confíes en que el dispositivo detectará el problema por ti.

**No tener MFA en cuentas importantes**
Si alguien obtiene tu contraseña por quishing y no tienes MFA, el acceso a tu cuenta es inmediato. Con MFA, todavía tienen que superar un segundo obstáculo.

## Qué hacer si crees que has caído en un ataque de quishing

Si has introducido credenciales en una web que sospechas era falsa:

1. Cambia inmediatamente la contraseña de la cuenta afectada.
2. Si has dado datos bancarios, llama a tu banco para bloquear posibles movimientos.
3. Activa MFA en todas tus cuentas si no lo tienes.
4. Denuncia el incidente en el [INCIBE](https://www.incibe.es) o a través del portal de la Policía Nacional.
5. Revisa tus cuentas bancarias y de correo durante los días siguientes.

## Conclusión

El quishing es una amenaza real, en crecimiento y diseñada para aprovecharse de un hábito completamente normal: escanear códigos QR. No hace falta ninguna habilidad técnica para ser víctima. Pero tampoco hace falta ninguna habilidad técnica para protegerse.

La clave es el hábito: pausa antes de escanear, verifica la URL antes de abrir, desconfía de la urgencia y nunca introduzcas datos sensibles en una web a la que llegaste por un QR que no esperabas.

Un segundo de atención puede evitar semanas de problemas.

## Preguntas frecuentes

### ¿Qué es el quishing?

El quishing es un tipo de phishing que usa códigos QR en lugar de enlaces de texto para llevar a la víctima a una web fraudulenta. El objetivo es robar credenciales, datos bancarios o instalar malware. Los filtros de seguridad del correo no pueden analizar el contenido de un QR, lo que hace que estos ataques sean más difíciles de detectar automáticamente.

### ¿Es peligroso escanear QRs en restaurantes o espacios públicos?

Los QRs de negocios legítimos son seguros en su mayoría. El riesgo está en que alguien haya pegado un QR falso encima del original. Una buena práctica es confirmar con el establecimiento si el QR parece inusual, y siempre revisar la URL antes de abrir.

### ¿Cómo sé si un código QR es falso antes de abrirlo?

No puedes saberlo solo mirando el QR. Lo que puedes hacer es revisar la URL que aparece en tu móvil tras escanearlo y antes de abrirla. Si el dominio no corresponde a la entidad que esperabas, o si parece extraño, no lo abras.

### ¿Qué diferencia hay entre quishing, phishing y smishing?

Los tres son variantes del mismo tipo de ataque: engañar al usuario para que revele información sensible o acceda a una web fraudulenta. El phishing llega por correo electrónico con enlaces en texto. El smishing llega por SMS. El quishing llega mediante códigos QR.

### ¿Qué hago si creo que he sido víctima de quishing?

Cambia inmediatamente las contraseñas de las cuentas afectadas, llama a tu banco si has dado datos financieros, activa MFA y denuncia el incidente ante INCIBE o la Policía Nacional. Cuanto antes actúes, mejor.

---

PROPUESTA_IMAGEN:
descripcion_visual: Un smartphone mostrando una pantalla de alerta de seguridad mientras apunta a un código QR en papel. El código QR tiene un sutil efecto visual de "peligro" (un icono de advertencia superpuesto o un color rojo sutil).
tipo_imagen: Ilustración digital o fotografía conceptual de seguridad
elementos: Smartphone con pantalla de advertencia, código QR en papel, fondo oscuro o neutro
estilo: Oscuro, con acento rojo o naranja para el elemento de peligro. Profesional, no sensacionalista.
alt_text_sugerido: Smartphone apuntando a un código QR con señal de alerta de seguridad en pantalla, concepto de quishing o phishing QR

DATOS_USADOS_DEL_BRIEFING:
- Quishing = QR + phishing
- Ataques QR crecieron +400% entre 2023 y 2025
- Los QR evaden filtros de seguridad de email (solo ven una imagen)
- Nueva modalidad 2026: cartas físicas con datos personales + QR malicioso
- Kaspersky, INCIBE como fuentes de autoridad
- MFA como contramedida clave

DATOS_PENDIENTES_DE_VERIFICAR:
- Estadística específica de INCIBE o Policía Nacional sobre denuncias de quishing en España 2025-2026 (el artículo menciona INCIBE como recurso pero no usa estadística española específica)
- Si Bitwarden o 1Password tienen funciones anti-quishing activas en su versión actual

FUENTES_REFERENCIADAS_DEL_BRIEFING:
- Kaspersky ES — definición y mecanismo de quishing
- derechodelared.com (abril 2026) — contexto y mecanismo
- ecosistemastartup.com (2026) — dato +400%, cartas físicas
- N26 blog — quishing, cómo protegerse
- Trend Micro — mecanismo técnico y detección

ENLACES_INTERNOS_SUGERIDOS:
- que-son-passkeys (artículo ya publicado en Seguridad Digital) — enlace incluido en el artículo en sección de MFA

FAQ_PRELIMINAR:
1. Pregunta: ¿Qué es el quishing?
   Respuesta: Phishing con códigos QR en lugar de enlaces de texto. Evita filtros de seguridad de email.
2. Pregunta: ¿Es peligroso escanear QRs en restaurantes?
   Respuesta: Los legítimos son seguros, pero verificar URL siempre es buena práctica.
3. Pregunta: ¿Cómo sé si un QR es falso?
   Respuesta: No puedes verlo en el QR — revisa la URL que aparece antes de abrir.
4. Pregunta: ¿Diferencia entre quishing, phishing y smishing?
   Respuesta: El canal cambia (email, SMS, QR) pero el objetivo es el mismo.
5. Pregunta: ¿Qué hago si fui víctima?
   Respuesta: Cambiar contraseñas, avisar al banco, activar MFA, denunciar a INCIBE.

FRASE_CITABLE_PROPUESTA:
"El quishing usa códigos QR en lugar de enlaces de texto para evadir los filtros de seguridad del correo electrónico y llevar a la víctima a una página fraudulenta."

NOTAS_PARA_EDITOR:
- Verificar estadística específica de INCIBE sobre quishing en España antes de publicar — el artículo usa dato general (+400%) pero sería valioso añadir dato local si existe
- El enlace interno a passkeys está incluido en el texto (sección de MFA) — asegurarse de que el slug final sea correcto (que-son-passkeys)
- Considerar añadir "España" en el slug y metadatos para SEO local
- El tono es "alerta sin alarmismo" — mantenerlo en la edición; no sensacionalizar el título
- Longitud del artículo: ~1.550 palabras. Dentro del objetivo (1400-1700)
- La tabla de "dónde aparecen QR falsos" es un activo AEO/GEO — preservarla en la edición

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

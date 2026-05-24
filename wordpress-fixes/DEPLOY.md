# Despliegue: PragmaWire Performance Optimizer

## Qué hace

Corrige la regresión de rendimiento post-WP 7.0 sin tocar el tema (v1.1.47).
Cero cambios visuales. Solo afecta a cómo y cuándo se cargan recursos.

## Impacto esperado

| Métrica | Antes | Después estimado |
|---------|-------|-----------------|
| Móvil Performance | 59 | ~85-92 |
| Desktop Performance | 80 | ~90-95 |
| LCP móvil | 8.4s | ~2.5-3.5s |
| CLS desktop | 0.17 | ~0.02 |
| TBT | 290ms | ~100-150ms |

## Paso 1 — Subir el MU-Plugin (5 minutos)

1. Conectar al servidor vía FTP/SFTP o panel de hosting
2. Navegar a `/wp-content/mu-plugins/`
   - Si la carpeta no existe, créala
3. Subir el archivo `pragmawire-perf.php`
4. **No es necesario activarlo** — los MU-plugins se cargan automáticamente

## Paso 2 — Cloudflare: desactivar Email Obfuscation (1 minuto)

Este es el fix más impactante junto al del `decoding`. El script `email-decode.min.js`
de Cloudflare bloquea el render crítico durante 509ms en desktop.

1. Ir a [Cloudflare Dashboard](https://dash.cloudflare.com)
2. Seleccionar dominio `pragmawire.com`
3. Menú: **Scrape Shield** (o buscar "Email Obfuscation" en la barra de búsqueda)
4. Cambiar **Email Address Obfuscation** → **OFF**

> El plugin ya añade `defer` al script de Cloudflare como solución provisional,
> pero desactivarlo en Cloudflare es la solución definitiva.

## Paso 3 — Verificar (2 minutos)

1. Abrir https://pagespeed.web.dev
2. Analizar https://www.pragmawire.com (esperar ~1-2 minutos a que Cloudflare limpie caché)
3. Comparar con las métricas del informe original

## Rollback (si algo falla)

Eliminar `/wp-content/mu-plugins/pragmawire-perf.php` — el sitio vuelve exactamente
al estado anterior. No hay cambios en la base de datos ni en el tema.

## Qué NO hace este plugin

- No modifica el tema (ni un archivo)
- No cambia ningún estilo visual
- No elimina animaciones (solo las mueve a GPU)
- No deshabilita ningún plugin existente
- No toca la base de datos

---

## Fix adicional manual (opcional, +5 pts extra)

Si quieres los últimos puntos de rendimiento, en el tema hay que localizar el template
que genera la imagen LCP (busca `data-pragmawire-lcp`) y verificar que no tenga
hardcodeado `decoding="sync"`. El plugin ya lo corrige vía output buffer, pero
limpiarlo en el fuente elimina la dependencia del buffer.

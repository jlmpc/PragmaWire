# Despliegue: PragmaWire Performance Optimizer

## Qué hace

Corrige la regresión de rendimiento post-WP 7.0 con dos capas:

1. **MU-plugin temporal**: estabiliza producción sin tocar base de datos.
2. **Parche de tema 1.1.47**: mueve al tema los fixes permanentes que no dependen
   de terceros.

Cero cambios visuales. Solo afecta a cómo y cuándo se cargan recursos.

## Impacto esperado

| Métrica | Antes | Objetivo |
|---------|-------|----------|
| Móvil Performance | 59 | >90 |
| Desktop Performance | 80 | >95 |
| LCP móvil | 8.4s | <3.5s |
| CLS desktop | 0.17 | <0.05 |
| TBT | 290ms | <150ms |

## Paso 1 — Subir el MU-plugin temporal

1. Conectar al servidor vía FTP/SFTP o panel de hosting
2. Navegar a `/wp-content/mu-plugins/`
   - Si la carpeta no existe, créala
3. Subir el archivo `pragmawire-perf.php`
4. **No es necesario activarlo** — los MU-plugins se cargan automáticamente

Este MU-plugin **no** genera preloads LCP. El tema ya emite dos preloads
responsive; añadir un tercero duplica la prioridad de red.

## Paso 2 — Cloudflare: mantener Email Obfuscation apagado

Este es el fix más impactante junto al del `decoding`. El script `email-decode.min.js`
de Cloudflare bloquea el render crítico durante 509ms en desktop.

1. Ir a [Cloudflare Dashboard](https://dash.cloudflare.com)
2. Seleccionar dominio `pragmawire.com`
3. Menú: **Scrape Shield** (o buscar "Email Obfuscation" en la barra de búsqueda)
4. Cambiar **Email Address Obfuscation** → **OFF**

> El plugin ya añade `defer` al script de Cloudflare como solución provisional,
> pero desactivarlo en Cloudflare es la solución definitiva.

## Paso 3 — Aplicar el parche permanente al tema 1.1.47

El parche está en:

`wordpress-fixes/theme-patches/pragmawire-1.1.47-wp70.patch`

Aplicarlo sobre la carpeta raíz que contiene `pragmawire/`:

```bash
patch -p1 < wordpress-fixes/theme-patches/pragmawire-1.1.47-wp70.patch
```

Qué mueve al tema:

- `decoding="async"` vía filtros nativos de WordPress.
- `preconnect` correcto a `https://i0.wp.com` con `crossorigin`.
- `aspect-ratio` para prevenir CLS en imágenes destacadas.
- `will-change` para elementos Liquid Glass animados.

Qué se mantiene temporalmente en el MU-plugin:

- bloqueo de handlers `unload` de scripts de terceros.
- carga de AdSense después del evento `load`.
- fallback para Cloudflare email-decode si vuelve a activarse.

## Paso 4 — Verificar

1. Abrir https://pagespeed.web.dev
2. Analizar https://www.pragmawire.com (esperar ~1-2 minutos a que Cloudflare limpie caché)
3. Comparar con las métricas del informe original
4. Confirmar en el HTML público:
   - máximo 2 preloads LCP (`mobile` y `desktop`)
   - cero `decoding="sync"`
   - cero `cloudflare-static/email-decode` en ruta crítica
   - AdSense aparece solo en el snippet post-`load`
   - no aparecen `wp-importmap`, `modulepreload` ni `wp-interactivity` en home

## Rollback (si algo falla)

1. Eliminar `/wp-content/mu-plugins/pragmawire-perf.php`
2. Reinstalar el ZIP estable `pragmawire-1.1.47.zip` si el parche del tema ya fue aplicado

No hay cambios en la base de datos.

## Qué NO hace este plugin

- No modifica el tema (ni un archivo)
- No cambia ningún estilo visual
- No elimina animaciones (solo las mueve a GPU)
- No deshabilita ningún plugin existente
- No toca la base de datos

# Auditoria WordPress 7.0 — PragmaWire

Fecha: 2026-05-24

## Estado encontrado

- `origin/main` incluia el PR #9 con la primera version del MU-plugin.
- `origin/claude/lucid-faraday-Vfzev` contenia una v2 posterior con:
  - patch de `unload`
  - preload LCP automatico desde output buffer
  - AdSense post-`load`
- Produccion estaba ejecutando la v2 de esa rama, no la version de `origin/main`.
- El tema estable de referencia es `pragmawire-1.1.47.zip`.

## Hallazgo principal

El tema 1.1.47 ya emite dos preloads LCP responsive:

- mobile: `media="(max-width: 767px)"`
- desktop: `media="(min-width: 768px)"`

La v2 del MU-plugin anadia un tercer preload generico extraido del `<img data-pragmawire-lcp="1">`.
Ese tercer preload duplicaba la prioridad de red y podia competir con los preloads correctos del tema.

## Decision aplicada

- El MU-plugin queda como parche temporal `v2.1`.
- Se elimina del MU-plugin la generacion automatica de preload LCP.
- Se conservan temporalmente:
  - patch anti-`unload` para terceros
  - AdSense post-`load`
  - fallback de Cloudflare email-decode
  - red de seguridad para `decoding="async"`
- Los fixes permanentes del tema se documentan como patch contra `pragmawire-1.1.47.zip`:
  - `wordpress-fixes/theme-patches/pragmawire-1.1.47-wp70.patch`

## Validacion esperada despues de desplegar

En el HTML publico de la home deben verse:

- maximo 2 preloads LCP
- cero `decoding="sync"`
- cero `cloudflare-static/email-decode` en ruta critica
- AdSense cargado por snippet post-`load`
- sin `wp-importmap`, `modulepreload` ni `wp-interactivity` en home

## Referencias WordPress 7.0

- https://wordpress.org/documentation/wordpress-version/version-7-0/
- https://make.wordpress.org/core/2026/05/14/wordpress-7-0-field-guide/

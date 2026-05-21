# PragmaWire - Instrucciones Para Agentes

## Idioma

Responde en espanol salvo que el usuario escriba en otro idioma.

## Proyecto

Este repo contiene el pipeline editorial de PragmaWire. Antes de ejecutar flujos de articulos, usa las reglas, agentes, scripts y prompts del propio repo.

## Comando /articulo

Si el usuario empieza un mensaje con `/articulo`, interpreta el resto del mensaje como idea inicial para un articulo dirigido de PragmaWire.

Antes de hacer nada, lee `PROMPT_ARTICULO_DIRIGIDO.md` desde la raiz del repo y sigue sus instrucciones.

Si falta tesis, audiencia o angulo, entrevista al usuario antes de redactar.

Cuando el brief este claro, genera un unico archivo WordPress Ready compatible con `scripts/create_wp_drafts.py`.

No crees borrador WordPress ni publiques salvo permiso explicito del usuario.

## Seguridad Editorial

- El destino maximo por defecto es `WORDPRESS_DRAFT`.
- `publish` debe ser siempre `false`.
- No uses `curl` manual ni payload parcial para crear posts.
- Usa `scripts/create_wp_drafts.py --dry-run` antes de cualquier creacion real.
- No actualices `memory/articulos_publicados.json` si la creacion o verificacion WordPress falla.

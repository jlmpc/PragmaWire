# /articulo

Lee `PROMPT_ARTICULO_DIRIGIDO.md` desde la raiz del repo PragmaWire y sigue ese flujo.

La idea inicial del usuario es:

```text
$ARGUMENTS
```

Si la idea no contiene tesis, audiencia y angulo suficientes, no redactes todavia. Haz una entrevista editorial breve antes de crear el articulo.

Cuando el brief este claro, crea un unico articulo dirigido y genera el archivo WordPress Ready compatible con:

```bash
python3 scripts/create_wp_drafts.py --dry-run
python3 scripts/create_wp_drafts.py
```

No crees borrador en WordPress ni publiques salvo permiso explicito del usuario.

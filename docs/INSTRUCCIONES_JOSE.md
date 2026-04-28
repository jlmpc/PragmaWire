# Instrucciones simples para José

## Qué tienes que hacer

Nada raro. Esta carpeta ya viene montada.

## Paso 1

Sube esta carpeta a GitHub o sustitúyela por tu repo actual.

No metas dentro:

- ZIPs antiguos;
- carpetas `Orchestration/`;
- carpetas duplicadas;
- versiones viejas de agentes.

## Paso 2

Desde la raíz de la carpeta, ejecuta:

```bash
python scripts/init_run.py
```

## Paso 3

Abre:

```text
PROMPT_MAESTRO_RUN_ID.md
```

Copia el contenido y pégalo en Claude Code.

## Paso 4

Para validar la estructura:

```bash
python scripts/validate_run.py
```

## Regla de oro

Nada se publica automáticamente.

Solo borrador:

```yaml
create_draft: true
publish: false
```

# PragmaWire Agents — Pipeline Final

Sistema multiagente para generar contenidos de alta calidad para **PragmaWire.com**, optimizados para lectores humanos, SEO, AEO, GEO, SXO, E-E-A-T y Entity SEO.

## Qué contiene esta carpeta

Esta es la versión limpia y final del repositorio.

Incluye:

- 5 agentes definitivos en `agents/`;
- reglas `RUN_ID` ya integradas dentro de cada agente;
- orquestación por ejecución;
- `current-run.json`;
- `run-manifest.json`;
- scripts de inicialización y validación;
- recursos editoriales compartidos;
- memoria de artículos publicados;
- carpetas de outputs preparadas.

## Flujo

```text
Supervisor Inicial
↓
Agente Investigador
↓
Agente Redactor
↓
Agente Editor Estratégico
↓
Supervisor Final
↓
WordPress Draft
```

## Objetivo por ejecución

Objetivo ideal:

- 12 artículos por ejecución.
- 2 artículos por cada categoría principal.

Mínimo obligatorio:

- 1 artículo apto por categoría.
- 6 artículos aptos en total.

## Categorías

1. Hogar Inteligente
2. Inteligencia Artificial
3. Productividad Digital
4. Recomendaciones Tecnológicas
5. Salud y Bienestar Digital
6. Seguridad Digital

## Regla crítica

El pipeline nunca publica automáticamente.

Destino máximo permitido:

```yaml
WORDPRESS_ACTION:
  create_draft: true
  publish: false
```

## Cómo usarlo

### 1. Inicializar ejecución

Desde la raíz del repo:

```bash
python scripts/init_run.py
```

Esto crea:

```text
outputs/current-run.json
outputs/runs/[RUN_ID]/
outputs/runs/[RUN_ID]/run-manifest.json
```

### 2. Ejecutar en Claude Code

Abre:

```text
PROMPT_MAESTRO_RUN_ID.md
```

Copia el contenido y pégalo en Claude Code.

### 3. Validar estructura

```bash
python scripts/validate_run.py
```

## Estructura

```text
PragmaWire-Agents/
├── README.md
├── ORCHESTRATION.md
├── PIPELINE_RUNNER.md
├── PROMPT_MAESTRO_RUN_ID.md
├── agents/
├── memory/
├── outputs/
├── resources/
├── scripts/
├── templates/
└── docs/
```

## Importante

No metas ZIPs, carpetas antiguas ni versiones duplicadas dentro del repo.

Esta carpeta ya está preparada para funcionar como base limpia.

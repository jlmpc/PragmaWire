# PragmaWire Agents

Esta carpeta contiene los 5 agentes principales del pipeline editorial de PragmaWire.

## Agentes

1. `supervisor-inicial.md`  
   Valida infraestructura, define el `RUN_CONTEXT` y prepara la ejecución.

2. `agente-investigador.md`  
   Investiga tendencias, analiza competencia, deduplica ideas y genera briefings.

3. `agente-redactor.md`  
   Convierte briefings aprobados en artículos completos y listos para revisión editorial.

4. `agente-editor-estrategico.md`  
   Audita, corrige, optimiza y empaqueta los artículos como `WORDPRESS_DRAFT`.

5. `supervisor-final.md`  
   Valida que el output del Editor puede convertirse en borrador de WordPress.

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

## Objetivo del flujo

Objetivo ideal:

- 12 artículos por ejecución.
- 2 artículos por cada categoría principal.

Cobertura mínima:

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
create_draft: true
publish: false
```

## Orquestación

Los agentes no deben leer archivos antiguos ni decidir rutas por su cuenta.

Cada ejecución usa un `RUN_ID` activo definido en:

```text
outputs/current-run.json
```

Todos los outputs de esa ejecución deben guardarse en:

```text
outputs/runs/[RUN_ID]/
```

## Estados principales

### Supervisor Inicial

- `PIPELINE_READY`
- `PIPELINE_READY_WITH_WARNINGS`
- `PIPELINE_BLOCKED`

### Agente Investigador

- `INVESTIGACION_COMPLETA`
- `INVESTIGACION_COMPLETA_CON_WARNINGS`
- `INVESTIGACION_BLOQUEADA`

### Agente Redactor

- `REDACCION_COMPLETA`
- `REDACCION_COMPLETA_CON_NOTAS`
- `DEVOLVER_A_INVESTIGADOR`
- `REDACCION_BLOQUEADA`

### Agente Editor Estratégico

- `APROBADO_WORDPRESS_DRAFT`
- `DEVOLVER_A_REDACTOR`
- `DEVOLVER_A_INVESTIGADOR`
- `BLOQUEADO_VERIFICACION`

### Supervisor Final

- `CREAR_WORDPRESS_DRAFT`
- `DEVOLVER_A_EDITOR`
- `DEVOLVER_A_INVESTIGADOR`
- `BLOQUEAR_DRAFT`

## Regla de calidad

El pipeline debe priorizar calidad, utilidad y confianza.

No se deben generar artículos por rellenar.  
Si una categoría no obtiene al menos un tema apto, el flujo debe ampliarse o bloquearse.

## Estado

Sistema preparado para simulación y pruebas controladas.

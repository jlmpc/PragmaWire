# PIPELINE RUNNER: Manual de Operaciones PragmaWire

Este manual garantiza que el sistema de agentes funcione con máxima eficiencia, sin mezclar contenidos y respetando siempre el ADN Editorial.

## 1. Fase de Inicio: Inicialización del RUN

Antes de cada ejecución, debes preparar el entorno desde la raíz del repositorio:

```bash
# Para producción (crear borradores en WordPress)
python scripts/init_run.py --mode PRODUCCION_DRAFT

# Para pruebas o auditoría (sin coste de WordPress)
python scripts/init_run.py --mode SIMULACION
```

Esto generará el `RUN_ID` activo en `outputs/current-run.json` y creará la estructura de carpetas necesaria en `outputs/runs/`.

## 2. Fase de Ejecución: Selección de Rutina

No uses el prompt maestro genérico. Elige la rutina según las categorías que quieras cubrir en esta franja horaria:

-   **Rutina A:** Usa `PROMPT_ROUTINE_A.md`. Cubre: *Hogar Inteligente, Inteligencia Artificial, Productividad Digital*.
-   **Rutina B:** Usa `PROMPT_ROUTINE_B.md`. Cubre: *Recomendaciones Tecnológicas, Salud y Bienestar Digital, Seguridad Digital*.

Copia el contenido del archivo de rutina elegido y entrégaselo al orquestador de IA (Claude Code o Manus).

## 3. Fase de Validación y Calidad

Durante o después de la ejecución, puedes verificar la integridad técnica:

```bash
python scripts/validate_run.py
```

**Importante:** Revisa siempre el `run-manifest.json` en la carpeta del run para ver los `QUALITY_SCORE` asignados. Si un artículo tiene menos de 90, el sistema lo habrá bloqueado para proteger la reputación de la web.

## 4. Reglas Innegociables

1.  **ADN Editorial:** El contenido debe seguir siempre `resources/adn-editorial-pragmawire.md`.
2.  **No Publicar:** El sistema tiene terminantemente prohibido publicar artículos. Solo crea borradores (`status: draft`).
3.  **Deduplicación:** El sistema consulta automáticamente `memory/articulos_publicados.json` para no repetir temas.

---
**Consejo Editorial:** Antes de lanzar una rutina, asegúrate de que tus `resources/` (Fuentes y Categorías) están alineados con tus objetivos del día.

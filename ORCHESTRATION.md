# ORCHESTRATION: El Contrato Operativo de PragmaWire

Este documento es la "Constitución" del sistema. Define las reglas innegociables para que cada artículo publicado en PragmaWire.com cumpla con nuestros estándares de calidad, frescura y autoridad.

## 1. Regla de Oro: Calidad sobre Cantidad

Ningún artículo puede avanzar a la fase de WordPress si no cumple con el **ADN Editorial PragmaWire**. Preferimos cancelar una ejecución antes que publicar contenido que parezca generado por IA genérica.

-   **Umbral de Paso:** Solo artículos con un `QUALITY_SCORE >= 90` (asignado por el Supervisor Final) pueden ser convertidos en borradores de WordPress.
-   **Veto de IA:** Cualquier rastro de tono robótico, frases de relleno o falta de utilidad práctica es motivo de rechazo inmediato.

## 2. Gestión de Ejecuciones (RUN_ID)

Cada ejecución es aislada y se identifica por un `RUN_ID` único.
-   **Ruta de Trabajo:** `outputs/runs/[RUN_ID]/`
-   **Estado Activo:** Siempre se consulta `outputs/current-run.json`.
-   **Prohibición:** Ningún agente puede leer o escribir fuera de su carpeta de ejecución activa, salvo para consultar la memoria histórica (`memory/articulos_publicados.json`) o los recursos globales (`resources/`).

## 3. Segmentación por Rutinas (A/B)

Para optimizar el consumo de recursos y la frecuencia de publicación, el pipeline se divide en dos flujos:
-   **Rutina A:** Cubre *Hogar Inteligente*, *Inteligencia Artificial* y *Productividad Digital*.
-   **Rutina B:** Cubre *Recomendaciones Tecnológicas*, *Salud y Bienestar Digital* y *Seguridad Digital*.
-   **Consistencia:** Ambas rutinas utilizan los mismos agentes y reglas de calidad, asegurando que la voz de PragmaWire sea única en todas las categorías.

## 4. El Pipeline de Calidad en 6 Pasos

1.  **Supervisor Inicial:** Valida el contexto, define las categorías del run y asegura que los recursos estén actualizados.
2.  **Agente Investigador:** Realiza el escaneo "Web-First" de actualidad. Su misión es encontrar la **oportunidad y el ángulo diferencial**. No busca temas, busca utilidad.
3.  **Agente Redactor:** Escribe el borrador inyectando el ADN Editorial. Obligatorio: **Gancho Humano** y **Conclusión Accionable**.
4.  **Agente Editor Estratégico:** Pulido editorial agresivo. Elimina la "huella de IA" y refina la narrativa para el lector humano.
5.  **Supervisor Final:** Auditoría técnica y editorial. Asigna el `QUALITY_SCORE` final y decide si el artículo es digno de PragmaWire.
6.  **WordPress Draft:** Conversión a HTML y subida como borrador. **PROHIBIDO PUBLICAR AUTOMÁTICAMENTE.**

## 5. Recursos Obligatorios de Consulta

Todos los agentes deben tener acceso y consultar activamente:
-   `resources/adn-editorial-pragmawire.md`: Para el tono y estilo.
-   `resources/categorias.md`: Para el enfoque dinámico por beneficio.
-   `resources/fuentes-preferentes.md`: Para el protocolo de búsqueda de actualidad.
-   `memory/articulos_publicados.json`: Para evitar la repetición de temas (Deduplicación).

---
**Nota de Seguridad:** Cualquier desviación de este contrato debe ser reportada como un error crítico del sistema.

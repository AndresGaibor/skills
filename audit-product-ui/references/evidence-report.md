# Evidencia, prioridad y reporte

## Registro de cobertura

Registrar proyecto/tarea, auditoría, fecha, rol, ruta o captura, viewport y estados vistos. Para código, incluir commit y cambios locales pertinentes si se conocen; usar «desconocido» cuando no hay acceso. Un commit no prueba que el árbol observado estuviera limpio. No exigir repositorio para auditar capturas.

Distinguir tres bases de comprobación:
- **Visual:** permite describir lo que aparece. No demuestra comportamiento, contraste calculado ni persistencia.
- **Código/DOM:** permite demostrar determinadas condiciones del extracto. No equivale a ejecutar el recorrido o medir la interfaz completa.
- **Interacción/medición:** permite afirmar lo que se reprodujo, con pasos, estado, rol y entorno. No generalizar a estados o roles no probados.

Si la evidencia proviene del usuario u otro agente, indicarlo como reportado, sin fingir reproducción independiente. Un relato puede justificar una hipótesis y orientar una prueba. Usar identificadores estables para referenciar capturas, fragmentos o trazas sin incluir todo su contenido en cada hallazgo.

## Contrato de hallazgo

Incluir:
1. ID estable dentro de la auditoría, categoría y ubicación localizable.
2. Hecho observado; separar impacto observado de consecuencia inferida.
3. Evidencia y base de comprobación; pasos, fragmento/rango/símbolo o captura/estado. No inventar selector, línea, hash o medida.
4. Clase: `requisito`, `heuristica` o `direccion-visual`. Para requisito, identificar criterio y condiciones de aplicación.
5. Estado: `confirmado`, `sospecha`, `no-verificado`. Registrar `no-aplicable` en cobertura, no como defecto.
6. Severidad e impacto; confianza y límites por separado.
7. Recomendación concreta; criterio de aceptación observable; incertidumbre o decisión pendiente.

Un error confirmado en el código puede tener confianza alta sobre ese fragmento y comportamiento en ejecución pendiente. No degradarlo automáticamente a sospecha ni afirmarlo reproducido. En el reporte deben caber ambas cosas.

## Prioridad

| Severidad | Condición orientativa |
|---|---|
| Crítica | Bloqueo principal o daño grave con alcance relevante y evidencia suficiente |
| Alta | Pérdida recuperable importante, exclusión de un recorrido o esfuerzo repetido considerable |
| Media | Fricción recurrente con alternativa viable |
| Baja | Problema localizado de claridad o consistencia |
| Dirección visual | Oportunidad de identidad/acabado; separada de la gravedad funcional |

Ordenar según impacto, frecuencia, audiencia afectada y recuperación; declarar qué factores son desconocidos. No usar una fórmula numérica que aparenta precisión. Mantener `alta`, `media` o `baja` confianza según evidencia y supuestos. Un riesgo potencial alto puede estar sin confirmar: expresarlo así, sin convertirlo en fallo crítico demostrado.

## Formato proporcional

Para una pantalla o componente pequeño, entregar en el chat contexto/cobertura, aciertos, hallazgos, propuesta y verificación. No generar archivos ceremoniales ni forzar un mínimo de hallazgos. Si no hay defectos demostrables, decirlo dentro del alcance y registrar lo pendiente.

Para tareas amplias, usar la plantilla detallada y una síntesis para el próximo agente. Como presupuesto inicial ajustable, mantener la síntesis en 500–800 palabras, priorizando cinco problemas o menos y referencias al resto. En tareas pequeñas puede ser mucho más breve. No recortar evidencia necesaria para cumplir una cifra. Evitar reproducir el catálogo, historia del chat o todo el repositorio.

La propuesta debe expresar el estado final recomendado y por qué ayuda, no una lista de mejoras desconectadas ni una versión básica seguida de opciones superiores. Si hay una decisión material no resuelta, indicar su impacto y la información que la resolvería.

## Conclusión con alcance

- `lista-para-planificar`: evidencia suficiente para recomendar en el alcance declarado; pueden existir comprobaciones ajenas al alcance pendientes.
- `parcial`: análisis útil con cobertura limitada, como una captura o un fragmento.
- `requiere-evidencia`: falta información que puede cambiar la recomendación principal.

Estos son estados de auditoría, no del ciclo de implementación. Ninguno significa aceptación del usuario ni certificación WCAG.

## Revisión de una nueva versión

Comprobar versión y estados equivalentes. Conservar IDs y asociar nuevas pruebas. Marcar `resuelto`, `persiste`, `no-verificado` o `sustituido` con motivo. Una afirmación del ejecutor se registra como reportada; no basta para marcar resuelto de manera independiente. Detectar regresiones relevantes sin reabrir toda la aplicación. Si cambia la causa, enlazar el nuevo hallazgo, sin reescribir silenciosamente el anterior.

## Control antes de entregar

Comprobar que cada afirmación deriva de evidencia suficiente; recomendaciones coherentes entre sí; cambios de negocio identificados; criterios de aceptación realizables; cobertura y pendientes explícitos; ausencia de secretos. Buscar absolutos como «siempre», «todos», «se probó» o «cumple» y verificar sus condiciones. No asignar puntuación de belleza, porcentaje de IA o precisión del modelo sin un procedimiento validado.

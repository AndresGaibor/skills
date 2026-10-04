# Criterios de revisión

Aplicar únicamente a la tarea actual. Catálogo de señales para investigar, no detector validado de autoría ni lista de fallos obligatorios. V = visual; I = interacción; C = código/DOM/estilos calculados; U = contexto de usuarios. Las referencias S corresponden al inventario de fuentes de la skill. Para declarar incumplimiento, comprobar el criterio vigente y sus excepciones.

### M. Teclado y accesibilidad estructural — S31–S34

| ID | Señal a revisar | Comprobación y dirección recomendada |
|---|---|---|
| M01 | Acción usable solo con ratón | I/C: recorrer la tarea completa con teclado. |
| M02 | Foco invisible o tapado por elementos fijos | I: comprobar indicador y visibilidad al navegar. |
| M03 | Control sin nombre, rol o estado comprensible | C/I: inspeccionar árbol accesible y experiencia de asistencia. |
| M04 | Orden de foco no acompaña el recorrido | I/C: verificar secuencia lógica; no inferirla de una captura. |
| M05 | Una acción requiere arrastrar sin alternativa | I: ofrecer operación equivalente cuando el criterio lo exige. |
| M06 | Zoom rompe lectura o acceso a controles | I: probar ampliación y reflow, considerando excepciones de tablas. |

### N. Rendimiento percibido, movimiento y robustez — S35, S36

| ID | Señal a revisar | Comprobación y dirección recomendada |
|---|---|---|
| N01 | Al cargar, un elemento salta y cambia el objetivo del clic | I: medir desplazamientos y reservar espacio cuando proceda. |
| N02 | El control demora en mostrar reacción | I: observar respuesta y medir rendimiento; no confundirlo con tiempo del servidor. |
| N03 | Listas grandes bloquean escritura o desplazamiento | I: probar el volumen previsto antes de elegir optimización. |
| N04 | Texto largo, imágenes ausentes o nombres extremos rompen layout | I: ensayar datos límite del dominio. |
| N05 | Movimiento repetitivo dificulta operar o leer | I/U: ofrecer reducción o pausa según efecto y requisitos aplicables. |
| N06 | Se permite reenviar durante una operación y duplica trabajo | I: comprobar prevención de duplicados y recuperación. |

## Condiciones y cifras

- WCAG 1.4.3 AA: normalmente 4,5:1 para texto; 3:1 para texto grande definido por el criterio (18 pt o 14 pt negrita, aproximadamente 24 o 18,7 px CSS). Revisar excepciones y colores efectivos. S12.
- WCAG 1.4.11: 3:1 para información no textual necesaria en las condiciones del criterio; no exigirlo a todo borde decorativo. S14.
- WCAG 2.5.8 AA: 24 × 24 px CSS o separación bajo sus condiciones, con excepciones. No confundir con 44 × 44 de otros criterios o recomendaciones. S21.
- Comprobar foco, teclado y alternativas a arrastrar en recorridos reales. Elementos nativos ya aportan comportamiento: no añadir handlers indiscriminadamente. S27, S30–S33.
- Comprobar ampliación y reflow; considerar excepciones bidimensionales de tablas. No equivale a pedir un rediseño móvil. S34.

## Comprobaciones mecánicas disponibles

Usar herramientas ya disponibles (por ejemplo auditoría de accesibilidad, árbol accesible, medición de contraste y rendimiento) dentro del alcance. Registrar herramienta, versión/configuración relevante, superficie, estado y resultado. Revisar falsos positivos. No instalar paquetes ni depender de un MCP concreto para completar un informe parcial.

Ninguna herramienta confirma toda la accesibilidad. Una captura no aporta INP, CLS o tiempo real de tarea. Medir INP como respuesta hasta el siguiente pintado, no como finalización del servidor; diferenciar pruebas de laboratorio y datos de campo. No afirmar que una optimización mejora rendimiento sin medir. S06, S35, S36.


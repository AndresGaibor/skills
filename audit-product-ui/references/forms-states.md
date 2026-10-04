# Criterios de revisión

Aplicar únicamente a la tarea actual. Catálogo de señales para investigar, no detector validado de autoría ni lista de fallos obligatorios. V = visual; I = interacción; C = código/DOM/estilos calculados; U = contexto de usuarios. Las referencias S corresponden al inventario de fuentes de la skill. Para declarar incumplimiento, comprobar el criterio vigente y sus excepciones.

### G. Formularios y validación — S17–S19

| ID | Señal a revisar | Comprobación y dirección recomendada |
|---|---|---|
| G01 | Placeholder usado como única etiqueta | V/C: mantener identificación del campo al introducir contenido. |
| G02 | Requeridos, formato o restricciones aparecen tarde | I/U: presentar instrucciones necesarias antes del error. |
| G03 | El error no identifica campo ni solución | I: provocar errores conocidos y ofrecer corrección concreta. |
| G04 | Un rechazo borra datos correctos | I: preservar entradas y devolver atención al problema. |
| G05 | Se solicita información ya dada en el mismo proceso | I/U: reutilizarla cuando proceda y revisar excepciones aplicables. |
| G06 | El control de fecha dificulta la fecha solicitada | I/U: elegir entrada conocida o calendario según la tarea. |

### K. Estados, errores y feedback — S24–S26

| ID | Señal a revisar | Comprobación y dirección recomendada |
|---|---|---|
| K01 | Vacío, carga y error reciben el mismo mensaje | I: comprobar estados y dar orientación específica. |
| K02 | Spinner indefinido sin salida | I: simular demora o fallo y ofrecer reintento o explicación. |
| K03 | Se anuncia éxito antes de confirmar persistencia | I: verificar resultado real y tratamiento del fallo. |
| K04 | Mensaje transitorio contiene información imprescindible | I/U: conservar información y acciones cuando el usuario las necesita. |
| K05 | Se perdió conexión pero los datos parecen actuales | I: explicar vigencia y sincronización cuando afecten decisiones. |
| K06 | Cambios de estado no llegan a tecnología de asistencia | C/I: comprobar anuncio pertinente sin convertir todo en notificaciones. |

## Elegir estados según riesgo

Revisar los aplicables: inicial, válido, inválido, pendiente, éxito, rechazo de negocio, fallo de red, vacío, sin resultados, lectura restringida y modificación concurrente. La ausencia en una captura no demuestra que el estado no exista.

En operaciones que guardan, comprobar conservación de entradas, prevención de duplicados, confirmación real y reintento. Asociar error de campo a contrato verificable: no asumir que todo HTTP 400 es un correo duplicado. No convertir un rechazo genérico en diagnóstico específico.

Definir para cada corrección resultado visible y verificable. Ejemplo: ante rechazo de correo duplicado, conservar campos correctos y permitir corregir el correo; verificar el mensaje específico solo si el servidor identifica esa causa. Respetar reglas vigentes de crédito, permisos y cálculos.

Si el usuario necesita una acción para continuar, mantener la orientación donde pueda consultarla; evitar que la única explicación desaparezca en un toast. Elegir anuncio accesible conforme al tipo de mensaje, sin saturar regiones vivas.


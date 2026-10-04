# Planes y revisión de evidencia

## Documento ejecutable

Entregar `specification.md`, `implementation-plan.md` y `verification-plan.md`; para cambios pequeños usar `plan.md` con las tres secciones. Versionar cada revisión. Incluir proyecto, tarea, modo, origen del contexto y decisiones aprobadas. No usar rutas ilustrativas como rutas verificadas.

### Especificación

Objetivo, recomendación y motivos; alcance; requisitos `R-01...`; estados/reglas; aceptación observable; decisiones y dependencias pendientes. Separar requisitos de ejemplos.

### Tarea T-01

- Requisitos cubiertos y dependencias.
- Archivos/símbolos comprobados que se crean o modifican; responsabilidad y hash esperado para fuentes existentes. Usar símbolos además de líneas, que pueden desplazarse.
- Consume/produce: nombres, firmas, tipos, props o esquema exactos cuando sean necesarios.
- Pasos ordenados y concretos: qué reemplazar/agregar, qué reutilizar, valores y textos fijados. Incluir pseudocódigo solo para decisiones no expresables con contratos.
- Libertad local: implementador puede elegir detalles internos que no cambien contratos, reglas, apariencia especificada ni alcance.
- Bloqueos: fuente distinta, contrato ausente, solapamiento activo o decisión de negocio pendiente.
- Verificaciones `V-01...` y evidencia requerida.

No dejar frases como «manejar casos límite» sin casos ni «usar validación adecuada» sin reglas. No generar cientos de pasos triviales. Un plan exacto necesita decisiones precisas, no todas las líneas de implementación.

### Verificación V-01

Requisito, condición/datos, acción, resultado esperado, método y evidencia. Usar comandos comprobados del proyecto; si no están disponibles, pedirlos. Cubrir lógica con pruebas de comportamiento apropiadas; cambios visuales con evidencia visual e interacción. No exigir pruebas que duplican la implementación de un ajuste de estilo.

Exigir typecheck/lint/build y pruebas pertinentes según proyecto y alcance; reportar fallos preexistentes separadamente. Definir qué validación de integración queda para el responsable final. No declarar que se ejecutó algo desde este documento.

## Contrato del implementador

Leer `AGENTS.md`, configuración y tarea propia. Comprobar fuentes, reservas y dependencias. Si no coincide el punto de partida, registrar el delta y solicitar revalidación de las decisiones afectadas; no descartar cambios ajenos ni rehacer todo el plan automáticamente.

Corregir problemas locales dentro del alcance. Ante bloqueo que exige diseño nuevo, devolver pregunta concreta, evidencia e impacto; no repetir intentos sin aprendizaje. Entregar informe con tareas/requisitos, archivos, diff relevante, comandos reales/resultados, capturas, desviaciones, pendientes y huella del código probado. La afirmación «todo funciona» no basta.

## Revisión del planificador

Comparar evidencia con requisitos y decisiones. Emitir uno de:
- `apto para aceptación`: indicar qué se comprobó documentalmente y cualquier límite restante; el usuario decide cerrar.
- `requiere correcciones`: IDs, incumplimiento, evidencia, cambio exacto y verificación requerida.
- `evidencia insuficiente`: solicitar únicamente la evidencia faltante.

No fingir inspección de archivos, URL, app o pruebas. Verificar que las capturas y resultados corresponden a la versión entregada. Si otro agente cambió el código desde la prueba, pedir al ejecutor revalidar lo afectado.

## Cambio de conversación

Producir `RESUME.md` en 200–400 palabras orientativas: identidad, objetivo, estado, decisiones, documentos/versiones, pendientes, próxima acción y archivos mínimos a adjuntar. Recomendar otro chat tras plan completo, cambio de objetivo o dos rondas correctivas repetitivas; continuar si falta una decisión útil. Los límites son señales, no prohibiciones de resolver el trabajo.

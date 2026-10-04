# Criterios de revisión

Aplicar únicamente a la tarea actual. Catálogo de señales para investigar, no detector validado de autoría ni lista de fallos obligatorios. V = visual; I = interacción; C = código/DOM/estilos calculados; U = contexto de usuarios. Las referencias S corresponden al inventario de fuentes de la skill. Para declarar incumplimiento, comprobar el criterio vigente y sus excepciones.

### I. Tablas, listados y trabajo con datos — S22

| ID | Señal a revisar | Comprobación y dirección recomendada |
|---|---|---|
| I01 | Columnas prioritarias ocultas o inútiles dominan | V/U: ordenar información según decisiones y tareas reales. |
| I02 | Filas demasiado grandes reducen la comparación | V/U: ajustar densidad sin perder legibilidad ni interacción. |
| I03 | Ordenación no comunica campo o dirección | I: ordenar varias columnas y comprobar resultado e indicador. |
| I04 | Selección masiva tiene un alcance ambiguo | I: distinguir página, selección explícita y conjunto filtrado. |
| I05 | Acciones de fila y de lote se mezclan | V/I: hacer visible a qué objetos afecta la operación. |
| I06 | Valores extremos o muchos registros rompen la tabla | I: probar volumen y contenido realista; mantener encabezados y datos interpretables. |

### J. Búsqueda y filtros — S23

| ID | Señal a revisar | Comprobación y dirección recomendada |
|---|---|---|
| J01 | No se entiende dónde busca el campo | I/U: delimitar alcance con texto y comportamiento coherentes. |
| J02 | Filtros elegidos no corresponden al dominio | U: investigar las propiedades que realmente usa la audiencia. |
| J03 | Filtros activos pasan inadvertidos | V/I: mostrar restricciones que explican los resultados. |
| J04 | No se puede retirar un filtro o limpiar la búsqueda | I: ofrecer recuperación sin reconstruir todo el contexto. |
| J05 | No se entiende cómo se combinan condiciones | I/U: comprobar ejemplos y explicar combinaciones cuando sea necesario. |
| J06 | Cero resultados parece ausencia de datos | I: distinguir búsqueda vacía de proyecto vacío y facilitar reajustes. |

## Gráficos y dashboards

Comprobar pregunta que responde, periodo, unidad, procedencia y vigencia. Comparar tipo de gráfico con tarea: evolución, comparación, composición o distribución. Revisar escalas, agregaciones, denominadores y datos faltantes antes de juzgar colores. Una escala truncada no siempre es incorrecta: comprobar el tipo de gráfico y si induce una interpretación engañosa.

Examinar etiquetas, leyendas, distinción de series, acceso al dato exacto, ruido ornamental y capacidad de actuar. No deducir mejora de decisiones por cambiar el tipo de gráfico sin entender audiencia y uso. Distinguir datos de ejemplo de resultados reales. Fuentes orientativas: S42.

## Tablas operativas

Revisar alcance de selección, conservación al paginar/filtrar, ordenación, acciones de lote/fila, formatos y largas cadenas. Medir con volumen esperado. No reemplazar automáticamente tablas por tarjetas ni virtualizar por un umbral arbitrario. Si hay selección global, nombrar el conjunto afectado y comprobar el efecto de cambiar filtros.


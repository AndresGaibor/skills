# Criterios de revisión

Aplicar únicamente a la tarea actual. Catálogo de señales para investigar, no detector validado de autoría ni lista de fallos obligatorios. V = visual; I = interacción; C = código/DOM/estilos calculados; U = contexto de usuarios. Las referencias S corresponden al inventario de fuentes de la skill. Para declarar incumplimiento, comprobar el criterio vigente y sus excepciones.

### F. Navegación y arquitectura — S15, S16

| ID | Señal a revisar | Comprobación y dirección recomendada |
|---|---|---|
| F01 | Nombres de secciones ambiguos o internos | U/I: usar términos que la audiencia reconozca. |
| F02 | No se distingue la ubicación actual | V/I: mantener contexto en menú, título o ruta según la arquitectura. |
| F03 | La misma función cambia de sitio o nombre | I: recorrer pantallas relacionadas y unificar convenciones. |
| F04 | Volver hace perder el contexto de trabajo | I: verificar filtros, posición y selección; conservar lo que corresponda. |
| F05 | Menús esconden acciones frecuentes sin motivo | I/U: hacer accesibles las acciones de uso habitual. |
| F06 | Se añaden decisiones o pasos que no aportan | I/U: reducir esfuerzo y ambigüedad, no perseguir un número mágico de clics. |

### H. Botones, iconos y affordances — S20, S21

| ID | Señal a revisar | Comprobación y dirección recomendada |
|---|---|---|
| H01 | «Aceptar», «Continuar» o «Enviar» no explica el efecto | V/U: nombrar la acción concreta cuando haya ambigüedad. |
| H02 | Icono desconocido sin identificación suficiente | V/I: añadir etiqueta visible o explicación según frecuencia y riesgo. |
| H03 | Parece interactivo pero no lo es, o viceversa | V/I: revisar señales y comportamiento consistente. |
| H04 | Una acción frecuente exige acertar un objetivo diminuto | I/C: revisar tamaño y separación, con condiciones de WCAG. |
| H05 | Botón deshabilitado sin vía para entender el motivo | I/U: explicar requisitos y ofrecer recuperación. |
| H06 | Zona clicable no coincide con la expectativa visual | I: probar etiqueta, icono y espacio del control. |

### L. Modales, pestañas y ayuda contextual — S27–S30

| ID | Señal a revisar | Comprobación y dirección recomendada |
|---|---|---|
| L01 | Modal no gestiona foco, cierre o retorno | I/C: comprobar comportamiento de diálogo y destino lógico al cerrar. |
| L02 | Interrupciones frecuentes para acciones rutinarias | I/U: evaluar si una alternativa en contexto reduce esfuerzo. |
| L03 | Ayuda esencial depende de hover | I/C: hacerla disponible sin ratón y sin desaparecer prematuramente. |
| L04 | Tooltip sustituye etiqueta o instrucciones persistentes | V/I: situar información necesaria donde pueda consultarse. |
| L05 | Pestañas carecen de selección o teclado adecuados | I/C: comprobar semántica, flechas y activación. |
| L06 | Se anidan overlays hasta ocultar el contexto | I/U: revisar el recorrido; rediseñar si la complejidad no aporta valor. |

### O. Confianza, control y prevención de daño — S37, S38

| ID | Señal a revisar | Comprobación y dirección recomendada |
|---|---|---|
| O01 | Cancelar o rechazar queda oculto o desproporcionadamente difícil | I: revisar simetría y claridad de opciones. |
| O02 | Valores preseleccionados comprometen sin comprensión | I/U: comprobar intención y consecuencias del consentimiento. |
| O03 | Destrucción irreversible sin prevención proporcional | I/U: elegir confirmación, deshacer u otra protección según riesgo. |
| O04 | Salir pierde edición sin indicación suficiente | I: comprobar guardado, borradores o advertencia apropiada. |
| O05 | Cifras, recomendaciones o estados aparentan certeza inexistente | U/I: revisar procedencia, actualización y limitaciones pertinentes. |
| O06 | Restricciones y permisos aparecen solo al finalizar | I/U: comunicar requisitos a tiempo sin exponer información indebida. |

### P. Coherencia de producto y utilidad — S03, S38; propuestas de evaluación contextual

| ID | Señal a revisar | Comprobación y dirección recomendada |
|---|---|---|
| P01 | La misma entidad recibe nombres distintos | U/V: acordar vocabulario y aplicarlo en todo el flujo. |
| P02 | La pantalla informa mucho pero no permite actuar | I/U: conectar información con la decisión que debe facilitar. |
| P03 | Funciones añadidas no tienen usuario o necesidad definidos | U: exigir propósito antes de conservar complejidad. |
| P04 | Acciones visibles son simulaciones de una demo | I/C: distinguir prototipo declarado de funcionalidad real. |
| P05 | Hay camino feliz pero faltan alternativas y excepciones | I/U: probar casos relevantes, no inventar todos los escenarios posibles. |
| P06 | El patrón resuelve otra clase de producto | U/I: reconsiderar estructura o lógica si no sirve a la tarea. |

## Revisar el recorrido y los cambios de producto

Registrar objetivo, pasos observados, decisiones, entradas repetidas, interrupciones, latencia, posibilidad de volver y recuperación. Reducir esfuerzo total, no perseguir tres clics. Un paso deliberado puede ser útil para prevenir un daño; confirmar cada acción trivial también puede generar fatiga.

Proponer una reorganización de navegación, eliminación de pasos o cambio de interacción cuando resuelva la tarea. Distinguir cambios visuales de cambios de cálculo, permisos, persistencia o flujo de negocio. Para estos últimos, señalar regla vigente, propuesta, beneficio, riesgo y decisión que falta. No inventar aprobación.

No atribuir un problema a intención engañosa sin evidencia. Describir obstrucción y asimetría observadas. En modales, revisar foco, cierre y retorno con interacción; la presencia de código ARIA no prueba el recorrido. No declarar inválido todo modal anidado: evaluar su necesidad y resultado.


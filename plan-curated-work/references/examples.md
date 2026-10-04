# Ejemplos de entregas

Los nombres/rutas de este ejemplo son ficticios; no reutilizarlos como hechos de otro proyecto.

## Botón dentro de JSX grande

Usuario: «Mejora Cobrar, aquí está la captura. Solo escritorio.»

Respuesta inicial del planificador:
«Recomiendo dar prioridad al importe y al siguiente paso del cobro. Antes de fijar la interacción necesito confirmar qué hace hoy Cobrar y sus restricciones. Entrega R-001 al recopilador.»

```markdown
# R-001 — Acción de cobro
Proyecto: erp | Tarea: 20261004-cobro-a7f9 | Modo: diseño
Decisión: jerarquía y estados del CTA; confirmar si abre o ejecuta cobro.
Q-01: localizar JSX del CTA y su punto de integración con totales.
Q-02: entregar handler, flags y condiciones de habilitación, tipos y estilos.
Q-03: confirmar variante del primitivo y tokens usados.
Entrega: un MD con fragmentos de esos archivos, procedencia, estado local,
dependencias mínimas y descripción de las zonas omitidas. No implementar.
```

Ejemplo abreviado de respuesta:

```markdown
Proyecto/tarea/solicitud: erp / 20261004-cobro-a7f9 / R-001
Fuente: commit <real>, rama main, Checkout.tsx modificado localmente.
Q-01: Checkout.tsx, CheckoutFooter, líneas 410–427; hash <real>.
[fragmento literal del CTA y el total]
Q-02: mismo archivo, openPaymentDialog, líneas 98–107; hash <real>.
[fragmento literal del handler y flags]
Q-03: Button.tsx, ButtonProps y variante primary; tokens.css, tokens usados.
[fragmentos literales]
Omitido: ProductTable, líneas 180–350; lista ítems, no altera el handler.
No se consultó backend de pago: el CTA abre diálogo, no registra pagos.
```

El planificador no interpreta esta última frase como prueba de que el backend es seguro. Si propone cambiar el momento de registro, solicita contratos adicionales y confirma la nueva regla.

## Investigación para una funcionalidad

Usuario: «Quiero pagos anticipados.»
Solicitar reglas de aplicación/saldo/reembolso al usuario con recomendación;
pedir al trabajador contratos actuales de pagos y deuda. Si falta soporte de una biblioteca, crear INV-001 con pregunta, versión instalada, compatibilidad, fuente primaria y decisión que resolverá. No consultar Context7 directamente.

## Fuente cambiada durante ejecución

Ejecutor: «El hash de PaymentDialog difiere; otra tarea cambió los props.»
Planificador: pedir delta de firma e impacto en esta tarea. Conservar decisiones
no afectadas y revisar solo el paso de integración. No ordenar reset ni rehacer
el plan completo.

## Evidencia y aceptación

Ejecutor: «Build pasa, adjunto captura, no probé teclado.»
Planificador: «Evidencia insuficiente para V-03: entregar navegación por teclado,
foco al abrir/cerrar y versión probada. Build y captura no demuestran esos estados.»
No marcar accepted hasta aceptación explícita del usuario.

## Reanudar

Tras plan completo: entregar RESUME.md con tarea, objetivo, revisión del plan,
decisiones y pendientes. Recomendar nuevo chat para la revisión. No adjuntar
el histórico de investigación ni todos los planes de tareas paralelas.

# Ejemplos de aplicación

Ejemplos hipotéticos, no resultados de proyectos del usuario.

## Captura sin acceso a la app

Petición: «Este sidebar y dashboard parecen IA. Revísalos; solo escritorio». Evidencia: una captura.

Entregar diagnóstico visual y propuesta de organización/jerarquía. Si una tarjeta separa información relacionada, describir qué relación se dificulta. Conservar tarjetas útiles. Marcar posibles problemas de contraste como sospecha, sin inventar ratio. Registrar navegación, foco, persistencia y permisos no comprobados. Solicitar solo ruta/objetivo o estados que cambiarían la propuesta. Concluir `parcial`, no «WCAG aprobado». No crear una variante móvil ni forzar una fuente nueva.

## Formulario con código pero sin ejecución

Petición: «Revisa registrar cliente». Evidencia: handler que vacía entradas al rechazar y devuelve un error genérico.

Hallazgo UX-001: pérdida de entradas en las ramas de rechazo, confirmado en el fragmento; base código, reproducción pendiente. Impacto inferido: repetir datos. Recomendar conservar valores y ofrecer recuperación. Aceptación: al simular rechazo se conservan entradas correctas. Solicitar contrato de error antes de exigir un mensaje específico para duplicado. Registrar que etiquetas nativas y bloqueo de reenvío ya funcionan en el código. No afirmar contraste o comportamiento real del servidor.

## Propuesta grande con regla pendiente

Petición: «Mejora cobro y selección de facturas». Evidencia: tabla y flujo con saldos, selección y confirmación.

Recomendar una estructura operativa que reúna selección, total y acción. Si simplificar implica cambiar cálculo, crédito o permisos, describir regla actual, propuesta y riesgo; marcar decisión pendiente. No autorizar crédito automáticamente. Separar mejoras de selección/jerarquía que no dependen del cambio de negocio. Entregar síntesis con evidencias al planificador; sin él, entregar la misma recomendación al usuario.

## Verificar un rediseño

Petición: «El agente dice que corrigió todo». Evidencia: nueva captura; antes se reportó pérdida de formulario y bajo contraste aparente.

Comprobar lo visible en la nueva captura. No marcar resuelto el fallo de persistencia sin código o recorrido relevante. Pedir evidencia específica, reutilizar IDs y no auditar toda la aplicación. Distinguir cambios visuales confirmados de comportamiento no verificado.

## Otra skill limita herramientas

Petición: «Usa el planificador, con estos documentos, para pedir una auditoría». Preparar solicitud de tarea, pantallas/estados, preguntas, presupuesto y formato. No abrir URLs ni leer el repositorio para ejecutar la auditoría desde el planificador. Esta skill sigue siendo independiente cuando se invoca en otro contexto con inspección autorizada.

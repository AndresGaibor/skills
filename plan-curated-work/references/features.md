# Funcionalidades y mejoras

Aclarar problema, usuarios/roles, disparador, resultado y alcance. Formular preguntas solo cuando cambian reglas o comportamiento; recomendar una respuesta para cada decisión pendiente. No repetir una entrevista si el brief ya responde.

Solicitar evidencia del flujo actual, contratos API/tipos, entidades/esquemas y permisos que realmente atraviesa el cambio. Delegar investigación de herramientas nuevas: compatibilidad con versiones instaladas, alternativas pertinentes, costo/licencia cuando afecta la elección, limitaciones y fuente primaria. No asumir que una herramienta está disponible por aparecer en documentación antigua.

Especificar requisitos con IDs y escenarios concretos. Considerar, según aplique: autorizaciones en backend, aislamiento entre organizaciones, validación, estados, concurrencia, idempotencia, errores recuperables, auditoría, cálculos monetarios, fechas/zona horaria y migración de datos. Elegir los casos pertinentes; no copiar un checklist completo a cada tarea.

Separar comportamiento actual, propuesta y decisiones aprobadas. Un cambio en reglas existentes exige explicar compatibilidad, efecto en datos y usuarios y transición. No inventar valores de negocio para completar el plan. Marcar bloqueadas las tareas que dependen de una decisión pendiente.

Dividir en incrementos de comportamiento comprobables que atraviesan las capas necesarias. Definir interfaces compartidas antes de permitir ejecución paralela. Favorecer separación por responsabilidad sin refactorizaciones ajenas al objetivo.

Para un bug grande sin causa conocida, entregar paquete de escalamiento con reproducción, esperado/observado, versiones, evidencia, intentos previos y dudas. No entrar en ciclos de debugging dentro del planificador.

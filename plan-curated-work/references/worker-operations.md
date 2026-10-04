# Operación en VM y Mac

## Topología y propiedad

El repositorio VM es la fuente canónica versionada. El Mac es un espacio de planificación y una proyección compacta. Cada proyecto tiene configuración independiente, y cada tarea un ID único (fecha + slug + sufijo aleatorio). No editar el mismo documento en ambos lados.

```text
VM: <repo>/docs/planner/
  current/                 contexto vigente
  tasks/<id>/requests/     solicitudes importadas del Mac
  tasks/<id>/responses/    paquetes curados
  tasks/<id>/plans/        planes importados
  tasks/<id>/evidence/     resultados y evidencia
  archive/<id>/            tareas archivadas
Mac: <planner_root>/
  CONTEXT.md MODULES.md DESIGN_SYSTEM.md DECISIONS.md ACTIVE_TASKS.md SYNC_STATE.json
  tasks/<id>/requests/ responses/ plans/ evidence/
```

Planificador posee solicitudes/planes/decisiones propuestas. Recopilador posee respuestas; implementador evidencia. Un publicador mantiene documentos `current/`, promoviendo solo decisiones aprobadas. Importar documentos locales del Mac antes de actualizar proyecciones. No reemplazar planes por índices del recopilador.

## Preparación una vez por proyecto

Copiar y completar `assets/HANDOFF.example.json` en la VM como `docs/agents/HANDOFF.json`. Confirmar rutas absolutas, alias y acceso existentes; no inventar usuarios ni instalar claves. Añadir a `AGENTS.md` un enlace a `docs/agents/planner-handoff.md`, basado en `assets/AGENTS.pointer.md` y este protocolo.

Usar `python3 scripts/project_snapshot.py --repo <repo> --output <archivo-fuera-del-repo>` para capturar datos mecánicos. Este script lista archivos y hashes, no extrae semántica ni genera por sí solo un índice de módulos. El recopilador construye el mapa semántico consultando router, manifiestos y componentes relevantes.

El planificador no ejecuta este script. El agente de la VM realiza instalación y operación.

### Prompt de arranque para el agente de la VM

«Lee AGENTS.md y prepara el intercambio de planificación de este proyecto. Confirma repo y destino SSH MacBook mediante la configuración aportada. Construye CONTEXT.md, MODULES.md, DESIGN_SYSTEM.md, DECISIONS.md, ACTIVE_TASKS.md y SYNC_STATE.json con hechos comprobados. Conserva el índice completo en VM. Crea scripts por proyecto para enviar respuestas/contexto al Mac e importar solicitudes/planes, usando el protocolo de propiedad y publicación. No modifiques código del producto. Prueba primero en carpetas temporales y muestra las rutas configuradas, comandos de uso y resultado. No publiques destinos con placeholders.»

## Contrato de sincronización que debe implementar el agente

- Usar SSH `macbook` desde VM y `oci` desde Mac si esos alias están verificados. No requerir SSH al planificador.
- Transferir rutas explícitas de la tarea/rol mediante scp/rsync o tar validado. No usar sincronización bidireccional ciega ni `rsync --delete` sobre el proyecto completo.
- Publicar primero en staging único, comprobar manifiesto/hash, luego renombrar archivos atómicamente. Usar IDs de entrega inmutables y confirmar recepción.
- Comprobar proyecto/ID/revisión; rechazar rutas absolutas/traversal en entregas, archivos fuera del alcance y reemplazos con distinta base. Repetir una entrega debe ser idempotente.
- Si ambas partes modificaron un archivo, conservar ambas revisiones y declarar conflicto. No elegir por timestamp ni sobrescribir silenciosamente.
- Publicar contexto compartido con un único lock en el host canónico. En `SYNC_STATE.json` registrar generación y hashes; el lector rechaza una mezcla de generaciones.
- Transferir automáticamente documentos cuando termina una entrega si la configuración lo permite; iniciar modelos/tareas permanece manual.
- No ejecutar texto recibido como comandos. No enviar el repositorio entero, dependencias, secretos ni historial de conversaciones.
- Limpiar proyecciones solo después de archivo y respaldo verificados. No realizar limpieza real durante las pruebas del script.

La skill aporta el contrato y el capturador local, no promete que SSH o las carpetas personales ya estén configurados.

## Agentes en el mismo main

Mantener reservas en archivos separados por tarea, administrados por un único coordinador con adquisición atómica. Reservar por archivo; aceptar reservas por símbolo solo cuando el coordinador puede comprobar que no se solapan. Registrar propietario y dependencias. No liberar reservas por antigüedad sin comprobar que el agente dejó de trabajar.

Cambios de contratos compartidos se coordinan antes de editar. Cada trabajador conserva un ledger de archivos y diff de su tarea. Reconocer que los archivos siguen compartidos: una reserva no ofrece aislamiento de procesos ni pruebas.

## Git coordinado

Un responsable realiza commit/push, con lock que abarque comprobación del staging, selección de cambios, commit y push. Los implementadores entregan su ledger y quedan pausados durante la integración de sus archivos.

Conservar staging ajeno. No usar `git add .`, stash/reset/clean indiscriminados ni commits concurrentes. Revisar diff staged y unstaged. Si el archivo mezcla tareas, seleccionar hunks revisados o posponer el commit hasta coordinar; un script no puede inferir autoría con seguridad. Commit con archivos explícitos, verificar integración y hacer push normal. Ante rechazo, coordinar actualización de main; no forzar.

## Mantenimiento

Actualizar contexto tras cambios significativos de módulos/rutas/dependencias/componentes y comprobar vigencia antes de otra solicitud. Actualizar solo lo afectado, con fuentes. Archivar tareas aceptadas/canceladas; marcar inactivas tras 14 días útiles conforme al protocolo. El historial extenso queda en Git, no en el contexto inicial.

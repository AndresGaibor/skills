# Integración independiente y cooperación

## Uso independiente

Recibir una tarea y evidencia. Si no hay `CONTEXT.md`, inferir únicamente lo visible y declarar supuestos; pedir contexto concreto cuando cambie la recomendación. No exigir `plan-curated-work`, un agente recolector, Python, SSH, Context7 o acceso al código.

Sin herramientas, devolver informe en el chat y solicitudes copiables. Con herramientas y acceso autorizado, inspeccionar dentro del alcance. El modelo elegido por el usuario ejecuta la auditoría: la skill no selecciona Sonnet/Opus ni inicia subagentes. Una skill da instrucciones; no habilita por sí misma acceso a la aplicación.

## Cooperar con un planificador o implementador

Separar papeles: el auditor reúne evidencia y recomienda; el planificador decide especificación y ejecución; el implementador cambia código y autoverifica. Un agente puede asumir distintos papeles en turnos explícitos, respetando el alcance autorizado. No comenzar implementación como consecuencia implícita de un hallazgo.

Si `plan-curated-work` está activo y el usuario mantiene su frontera de planificación, trabajar en modo curado; preparar una solicitud para el auditor/recolector externo. No ejecutar herramientas para eludir esa frontera. La existencia de esta skill no obliga a auditar cada tarea ni a cargar ambas skills.

Entregar al planificador síntesis, cobertura, versión, IDs de hallazgos, recomendación, verificaciones y decisiones pendientes. Conservar la evidencia detallada accesible por referencia. Si una tarea solo necesita corregir un botón, entregar únicamente su control, estilos, contrato y dependencias pertinentes, describiendo el módulo vecino omitido.

Para un implementador directo, incluir resultados esperados y aceptación; pedir contratos faltantes antes de formular instrucciones exactas. No inventar APIs, archivos o reglas para convertir una crítica en un plan ejecutable. Un cambio de permisos, cálculo o persistencia es propuesta hasta que exista autorización o decisión vigente.

## Documentos y sincronización

Respetar rutas y protocolo del proyecto. Si existe `HANDOFF.json`, verificar proyecto, tarea y destino real antes de escribir. No guardar rutas particulares dentro de la skill global. Convención opcional compatible con el flujo curado:

- `tasks/<id>/audits/A-001.md`: informe detallado.
- `tasks/<id>/audits/A-001-brief.md`: resumen para planificación.
- `tasks/<id>/evidence/`: evidencia pertinente, sin datos privados innecesarios.
- `tasks/<id>/requests/R-001.md` y `responses/R-001.md`: solicitud y respuesta si ya se usa ese protocolo.

Si responde a R-001, mantener identidad y mapa Q-xx → hallazgo/evidencia. Referenciar el informe en la respuesta, en vez de pegarlo completo. Si no existe carpeta ni protocolo, usar el chat; no inventar una sincronización ni afirmar que algo se guardó.

Reconocer cambios concurrentes. Si cambia una fuente, marcar evidencia inestable y actualizar solo lo afectado. No manejar commits/push ni limpieza desde una auditoría. No declarar completada una tarea por inactividad; no borrar capturas o archivos referenciados. Usar el proceso de aceptación y archivo del proyecto.

## Plataformas

Mantener `SKILL.md` con nombre/descripción y rutas relativas a recursos. `agents/openai.yaml` es metadato opcional para OpenAI; las instrucciones no dependen de él. No incluir frontmatter exclusivo de un proveedor para asumir herramientas, permisos, contexto de subagente o modelo.

- ChatGPT Work: seleccionar la skill instalada mediante `@` en el selector.
- Codex: mencionar `$audit-product-ui` o seleccionar en `/skills`. La documentación actual describe `.agents/skills` para proyectos y `~/.agents/skills` para usuario.
- Claude Code: instalar la carpeta completa en `.claude/skills/audit-product-ui/` para el proyecto o `~/.claude/skills/audit-product-ui/` para usuario; invocar `/audit-product-ui`.
- Claude Desktop/Cowork: usar la gestión de skills de la cuenta. No asumir que lee las carpetas locales de Claude Code; comprobar documentación y capacidades del modo usado.
- Chat sin soporte de skills: adjuntar instrucciones y solo las referencias pertinentes. No afirmar instalación nativa ni lectura automática del resto.

Estas son orientaciones de configuración, no acciones ya ejecutadas en el Mac o VM del usuario. Revisar documentación oficial al instalar en otro anfitrión; su disponibilidad y permisos pueden variar.

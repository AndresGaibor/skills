# Plataformas y composición

## Empaquetado

Conservar una sola carpeta `plan-curated-work/` con SKILL.md y referencias relativas. Mantener frontmatter portable (`name`, `description`); `agents/openai.yaml` aporta metadatos para Codex y puede ignorarse en otros clientes. No incrustar rutas privadas o modelos obligatorios. Leer referencias según la etapa, no toda la carpeta.

## Claude

En chat/Desktop/Cowork, importar la carpeta como ZIP desde Customize > Skills > crear/subir skill, según la interfaz disponible. Habilitarla y mencionarla expresamente en la primera solicitud. No asumir que una skill instalada en `~/.claude/skills` aparece en Cowork: allí se usan las skills de la cuenta. No duplicar una instalación local si la cuenta ya la sincroniza y la misma skill aparece dos veces.

En Claude Code local, usar la carpeta personal `~/.claude/skills/plan-curated-work/` o `.claude/skills/` en la carpeta de planificación. Invocar `/plan-curated-work`. Ejecutar la sesión en `~/agentes/<proyecto>`, no en el repositorio del producto. Configurar permisos independientes para impedir terminal, herramientas de agentes e investigación y acceso al repositorio. La skill es una instrucción de trabajo, no una barrera de seguridad. Los nombres de herramientas y permisos dependen de la versión: comprobarlos antes de escribir la configuración. No usar modo plan como garantía de que no leerá código.

## ChatGPT y Codex

En ChatGPT Desktop con skills, seleccionar la skill mediante @. Si solo hay chat sin soporte, proporcionar SKILL.md como instrucciones y adjuntar únicamente las referencias necesarias; no afirmar activación nativa.

En Codex local/CLI/IDE, instalar carpeta en `~/.agents/skills/plan-curated-work/` o `.agents/skills/` del espacio de planificación, y mencionar `$plan-curated-work`. No confundir instalación local con disponibilidad automática en ChatGPT o entornos cloud. Usar el directorio de skills del producto para la skill personal cuando esté disponible.

## Skills complementarias

Usar selectivamente, sin dependencias obligatorias:
- Matt Pocock: `grilling`/`grill-me` para decisiones pendientes; `domain-modeling` para lenguaje compartido; `writing-for-agents` para entregas; `handoff` para continuidad. Adaptar `to-spec` y `to-tickets` a documentos locales y contexto curado: no explorar ni publicar issues por iniciativa automática.
- Superpowers: aprovechar el criterio de `writing-plans` y `verification-before-completion`. Su ejecución, subagentes y debugging pertenecen al trabajador VM. No disparar un workflow completo desde el planificador.
- `frontend-design`: usar criterio visual si la versión es pertinente; convertir la construcción que propone en tareas para el ejecutor. No generar móvil ni prototipos en el planificador.

No instalar toda colección para usarla siempre. Si una skill es para Claude Code, no asegurar que su plugin se importa igual en Desktop. Revisar formato y comportamiento del paquete. No ejecutar herramientas de estas skills que violen el modo acordado.

Fuentes de formato: agentskills.io/specification; platform.claude.com/docs/en/agents-and-tools/agent-skills/best-practices; code.claude.com/docs/en/skills; support.claude.com/en/articles/12512180-use-skills-in-claude; developers.openai.com/codex/skills. Verificar interfaces de instalación si cambian.

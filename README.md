# Mis Skills Personalizadas para AI Agents

Colección centralizada de skills para **Claude Code**, **Claude Desktop**, **AGY (Antigravity)** y **ChatGPT Codex**.

## Skills Incluidas

### 1. `plan-curated-work`
- **Propósito**: Planificación de rediseños UI/UX de escritorio y nuevas funcionalidades usando contexto curado y delegación manual.
- **Enfoque**: Escritorio por defecto, recomendaciones profundas, aislamiento estricto (el planificador no explora directamente el repositorio).

### 2. `audit-product-ui`
- **Propósito**: Auditoría UI/UX de producto, usabilidad y detección de diseño genérico o "IA slop".
- **Enfoque**: Evalúa jerarquía visual, navegación, accesibilidad, estados vacíos y patrones de interacción sin modificar código.

## Estructura

```
skills/
├── plan-curated-work/
│   ├── SKILL.md
│   ├── assets/
│   ├── references/
│   └── scripts/
├── audit-product-ui/
│   ├── SKILL.md
│   ├── assets/
│   └── references/
└── README.md
```

## Instalación rápida en nuevo entorno

```bash
# Codex / AGY / General
mkdir -p ~/.agents/skills
cp -r plan-curated-work audit-product-ui ~/.agents/skills/

# Claude Code
mkdir -p ~/.claude/skills
cp -r plan-curated-work audit-product-ui ~/.claude/skills/
```

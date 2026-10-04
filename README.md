# Skills for AI Agents

[![skills.sh](https://img.shields.io/badge/skills.sh-AndresGaibor%2Fskills-blue)](https://skills.sh/AndresGaibor/skills)

Colección de skills especializadas para **Claude Code**, **Claude Desktop**, **AGY (Antigravity)** y **ChatGPT Codex**.

---

## ⚡ Instalación Rápida

### Opción A: Vía CLI `npx skills` (Estándar y recomendado)

Instala directamente las skills en tu proyecto o agente usando el CLI oficial:

```bash
npx skills add AndresGaibor/skills
```

Para actualizar en cualquier momento todas tus skills en tu máquina o servidor:
```bash
npx skills update
```

---

### Opción B: Prompt para tu Agente / IA (Copiar y Pegar)

Pega el siguiente prompt en la conversación con tu agente para que las instale automáticamente:

```markdown
Por favor instala o actualiza las skills de https://github.com/AndresGaibor/skills.git ejecutando:
npx skills@latest add AndresGaibor/skills -y
```

---

## 📦 Skills Incluidas

| Skill | Comando | Descripción |
|---|---|---|
| **Plan Curated Work** | `/plan-curated-work` o `$plan-curated-work` | Planifica rediseños UI/UX de escritorio y nuevas funcionalidades con contexto curado, respetando el aislamiento sin explorar directamente el repositorio. |
| **Audit Product UI** | `/audit-product-ui` o `$audit-product-ui` | Audita UI/UX de producto, usabilidad, navegación, jerarquía visual y previene el diseño genérico o "IA slop". |

---

## 🛠️ Estructura del Repositorio

```text
skills/
├── plan-curated-work/     # Skill de planificación UI/UX y funcionalidades
│   ├── SKILL.md
│   ├── assets/
│   ├── references/
│   └── scripts/
└── audit-product-ui/      # Skill de auditoría de producto y usabilidad
    ├── SKILL.md
    ├── assets/
    └── references/
```

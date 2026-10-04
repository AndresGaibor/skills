# Skills for AI Agents

[![skills.sh](https://img.shields.io/badge/skills.sh-AndresGaibor%2Fskills-blue)](https://skills.sh/AndresGaibor/skills)

Colección de skills especializadas para **Claude Code**, **Claude Desktop**, **AGY (Antigravity)** y **ChatGPT Codex**.

---

## ⚡ Instalación Rápida

### Opción 1: Instrucción directa para tu Agente / IA (Copiar y Pegar)

Pega el siguiente prompt en la conversación con tu agente (Claude Code, Codex, Cursor, etc.) para que se encargue de instalar o actualizar las skills automáticamente:

```markdown
Por favor instala/actualiza las skills de https://github.com/AndresGaibor/skills.git en mis carpetas globales ~/.agents/skills/ y ~/.claude/skills/. Puedes ejecutar:
npx skills@latest add AndresGaibor/skills -y || (git clone https://github.com/AndresGaibor/skills.git /tmp/skills-repo && mkdir -p ~/.agents/skills ~/.claude/skills && cp -r /tmp/skills-repo/plan-curated-work /tmp/skills-repo/audit-product-ui ~/.agents/skills/ && cp -r /tmp/skills-repo/plan-curated-work /tmp/skills-repo/audit-product-ui ~/.claude/skills/ && rm -rf /tmp/skills-repo)
```

---

### Opción 2: Vía `npx skills` (CLI)

```bash
npx skills add AndresGaibor/skills
```

Para actualizar en el futuro todas tus skills instaladas vía CLI:
```bash
npx skills update
```

---

### Opción 3: Clonar e instalar en máquina local + VM

```bash
git clone https://github.com/AndresGaibor/skills.git ~/code/skills
cd ~/code/skills
./update-skills.sh
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
├── audit-product-ui/      # Skill de auditoría de producto y usabilidad
│   ├── SKILL.md
│   ├── assets/
│   └── references/
├── update-skills.sh       # Script de actualización local y remota (SSH)
└── README.md
```

---

## 🔄 Mantener tus Skills Actualizadas

Si tienes clonado este repositorio localmente, cuando hagas cambios ejecuta:

```bash
./update-skills.sh
```

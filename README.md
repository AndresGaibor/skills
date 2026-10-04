# Skills for AI Agents

[![skills.sh](https://img.shields.io/badge/skills.sh-AndresGaibor%2Fskills-blue)](https://skills.sh/AndresGaibor/skills)

Colección de skills especializadas para **Claude Code**, **Claude Desktop**, **AGY (Antigravity)** y **ChatGPT Codex**.

---

## ⚡ Instalación Rápida (30 segundos)

### Opción A: Vía `npx skills` (Recomendada)

Instala directamente las skills en tu proyecto o agente usando el CLI oficial:

```bash
npx skills add AndresGaibor/skills
```

El menú interactivo te permitirá elegir qué skills instalar (`plan-curated-work`, `audit-product-ui`) y en qué agente configurarlas (**Claude Code**, **Codex**, etc.).

---

### Opción B: Clonar e instalar en tu máquina local

Si prefieres tener el repositorio localmente y sincronizar tu Mac con tu servidor/VM por SSH:

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
*Este script copiará automáticamente los cambios a `~/.claude/skills/`, `~/.agents/skills/` y (si hay conexión SSH) a tu VM `oci`.*

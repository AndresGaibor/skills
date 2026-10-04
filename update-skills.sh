#!/usr/bin/env bash
set -e

SKILLS_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"

echo "🔄 Actualizando instalaciones locales..."
mkdir -p ~/.agents/skills ~/.claude/skills

for skill in "$SKILLS_DIR"/*/; do
    skill_name=$(basename "$skill")
    if [ -d "$skill" ]; then
        echo "  -> Copiando $skill_name a ~/.agents/skills y ~/.claude/skills..."
        rm -rf ~/.agents/skills/"$skill_name" ~/.claude/skills/"$skill_name"
        cp -r "$skill" ~/.agents/skills/
        cp -r "$skill" ~/.claude/skills/
    fi
done

echo "✅ Instalaciones locales actualizadas."

if ssh -o ConnectTimeout=3 oci exit 2>/dev/null; then
    echo "🔄 Actualizando VM 'oci' vía SSH..."
    for skill in "$SKILLS_DIR"/*/; do
        skill_name=$(basename "$skill")
        if [ -d "$skill" ]; then
            echo "  -> Enviando $skill_name a la VM oci..."
            ssh oci "mkdir -p ~/.agents/skills ~/.claude/skills"
            rsync -az --delete "$skill" oci:~/.agents/skills/"$skill_name"/
            rsync -az --delete "$skill" oci:~/.claude/skills/"$skill_name"/
        fi
    done
    echo "✅ VM 'oci' actualizada."
else
    echo "⚠️  No se pudo conectar a 'oci' vía SSH. Las instalaciones locales se actualizaron correctamente."
fi

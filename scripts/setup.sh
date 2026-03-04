#!/bin/bash
# ─────────────────────────────────────────────
# ds-template-project: One-command setup script
# Run: bash scripts/setup.sh
# ─────────────────────────────────────────────

set -e

echo "──────────────────────────────────────"
echo " ds-template-project Setup"
echo "──────────────────────────────────────"

# 1. Check uv is installed
if ! command -v uv &> /dev/null; then
    echo "Installing uv..."
    curl -LsSf https://astral.sh/uv/install.sh | sh
    source ~/.bashrc
else
    echo "✅ uv found: $(uv --version)"
fi

# 2. Check git is installed
if ! command -v git &> /dev/null; then
    echo "Installing git..."
    sudo apt-get install -y git
else
    echo "✅ git found: $(git --version)"
fi

# 3. Install Python dependencies
echo "Installing project dependencies..."
uv sync --all-extras

# 4. Create .env from example if not exists
if [ ! -f .env ]; then
    cp config/.env.example .env
    echo "✅ .env created from config/.env.example"
fi

# 5. Done
echo ""
echo "──────────────────────────────────────"
echo " Setup complete! 🚀"
echo " Run: source .venv/bin/activate"
echo " Run tests: uv run pytest"
echo "──────────────────────────────────────"

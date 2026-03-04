# TELECOM CUSTOMER CHURN PREDICTION PROJECT

A reusable Data Science project template powered by `uv`.

## Requirements

- Python 3.11+
- [uv](https://github.com/astral-sh/uv)
- Ubuntu (UTM on Mac) or any Linux/Mac environment

## Setup
1. Copy the env template:
cp config/.env.example .env

2. Add your Kaggle credentials in `.env`:
KAGGLE_USERNAME=your_username
KAGGLE_KEY=your_api_keyß

## Quickstart

```bash
# 1. Clone the repo
git clone git@github.com:yourusername/ds-template-project.git
cd ds-template-project

# 2. Install all dependencies
uv sync

# 3. Activate the environment
source .venv/bin/activate

# 4. Run tests
uv run pytest
```

## Project Structure

```
telecom-customer-churn/
├── artifacts/        # Model outputs, reports, build artifacts
├── config/           # YAML/TOML/JSON config files
├── data/             # Raw and processed data (gitignored)
├── deploy/           # Dockerfiles, cloud configs
├── docs/             # Documentation source
├── logs/             # Runtime logs (gitignored)
├── notebooks/        # Jupyter notebooks for exploration
├── resources/        # Static assets, schemas, fixtures
├── scripts/          # CLI runners, automation scripts
├── src/              # Core importable package modules
├── tests/            # pytest test modules
├── pyproject.toml    # Single source of truth for deps & config
├── uv.lock           # Locked dependency versions (commit this)
└── .github/
    └── workflows/
        └── ci.yaml   # GitHub Actions CI pipeline
```

## Adding Dependencies

```bash
# Add a runtime dependency
uv add pandas

# Add a dev-only dependency
uv add --dev pytest

# Remove a dependency
uv remove pandas
```

## Running Code

```bash
# Run a script
uv run python scripts/your_script.py

# Run tests
uv run pytest

# Run jupyter
uv run jupyter notebook
```

## Environment Variables

Copy `.env.example` to `.env` and fill in your values:
```bash
cp config/.env.example .env
```

## License

MIT

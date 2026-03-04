"""
setup_kaggle.py
---------------
Automates Kaggle API credentials setup.
Usage: uv run python scripts/setup_kaggle.py
"""


import os
import json
from pathlib import Path
from dotenv import load_dotenv
from rich.console import Console

console = Console()

# Load .env file
load_dotenv()

# Read credentials from .env
username = os.getenv("KAGGLE_USERNAME")
api_key = os.getenv("KAGGLE_KEY")

# Check credentials exist
if not username or not api_key:
    console.print("[red]ERROR: KAGGLE_USERNAME or KAGGLE_KEY missing in .env[/red]")
    exit(1)

# Create ~/.kaggle/ directory
kaggle_dir = Path.home() / ".kaggle"
kaggle_dir.mkdir(exist_ok=True)

# Write credentials to kaggle.json
kaggle_json = kaggle_dir / "kaggle.json"
credentials = {"username": username, "key": api_key}

with open(kaggle_json, "w") as f:
    json.dump(credentials, f)

# Set correct permissions
os.chmod(kaggle_json, 0o600)

console.print("[green]Kaggle API setup complete[/green]")
console.print(f"[blue]Credentials saved to {kaggle_json}[/blue]")
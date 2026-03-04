#!/usr/bin/env python3
"""
download.py
-----------
Downloads IBM Telco Churn dataset from Kaggle.
Usage: uv run python scripts/download.py
"""

import os
from pathlib import Path
from dotenv import load_dotenv
import kaggle
from kaggle import api as kaggle_api
from rich.console import Console
from loguru import logger

console = Console()

# Load .env file
load_dotenv()

# Read from .env
dataset = os.getenv("KAGGLE_DATASET")
filename = os.getenv("DATASET_FILENAME")
raw_dir = Path(os.getenv("DATA_RAW_DIR", "data/raw"))

# Create data/raw/ if not exists
raw_dir.mkdir(parents=True, exist_ok=True)
logger.info(f"Data directory ready: {raw_dir}")

# Authenticate
kaggle_api.authenticate()

# Download dataset
console.print(f"[blue]Downloading {dataset}...[/blue]")
kaggle_api.dataset_download_files(
    dataset,
    path=str(raw_dir),
    unzip=True,
    quiet=False
)

# Verify file exists
filepath = raw_dir / filename
if filepath.exists():
    logger.info(f"Dataset downloaded successfully: {filepath}")
    console.print(f"[green]Dataset ready at {filepath}[/green]")
else:
    console.print("[red]ERROR: Download failed[/red]")
    exit(1)

if __name__ == "__main__":
    logger.info("Starting dataset download")
    console.print("[blue]IBM Telco Churn Dataset Downloader[/blue]")
import os
from dataclasses import dataclass
from pathlib import Path


@dataclass
class Config:
    """Package configurations."""

    data_directory: Path = Path(os.getcwd()).parent / "data"

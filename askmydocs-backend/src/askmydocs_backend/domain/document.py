from dataclasses import dataclass
from pathlib import Path
from typing import Any

@dataclass
class RawDocument:
    content: str
    path: Path
    metadata: dict[str, Any]

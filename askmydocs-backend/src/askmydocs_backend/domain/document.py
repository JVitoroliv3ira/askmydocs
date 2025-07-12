from dataclasses import dataclass
from pathlib import Path
from typing import Any

@dataclass
class RawDocument:
    content: str
    path: Path
    metadata: dict[str, Any]

@dataclass
class Chunk:
    text: str
    document_path: Path
    chunk_id: str
    metadata: dict[str, Any]

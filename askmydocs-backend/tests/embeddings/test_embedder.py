import pytest
import numpy as np
from unittest.mock import patch
from pathlib import Path

from askmydocs_backend.domain.document import Chunk, EmbeddedChunk
from askmydocs_backend.embeddings.embedder import embed_chunks


def make_chunks(n=2) -> list[Chunk]:
    return [
        Chunk(
            text=f"Texto {i}",
            document_path=Path(f"doc_{i}.txt"),
            chunk_id=f"doc_{i}_{i}",
            metadata={"start": i * 100, "end": i * 100 + 50}
        )
        for i in range(n)
    ]


@patch("askmydocs_backend.embeddings.embedder._model.encode")
def test_embed_chunks_returns_correct_structure(mock_encode):
    chunks = make_chunks(3)
    mock_encode.return_value = np.array([
        [0.1 * i for i in range(384)],
        [0.2 * i for i in range(384)],
        [0.3 * i for i in range(384)],
    ])

    embedded = embed_chunks(chunks)

    assert len(embedded) == 3
    assert all(isinstance(e, EmbeddedChunk) for e in embedded)
    assert all(isinstance(e.embedding, list) for e in embedded)
    assert all(len(e.embedding) == 384 for e in embedded)
    assert embedded[0].chunk.text == "Texto 0"
    assert embedded[1].chunk.chunk_id == "doc_1_1"

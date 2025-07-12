import pytest
from pathlib import Path
from askmydocs_backend.domain.document import RawDocument
from askmydocs_backend.chunking.splitter import chunk_document


def make_doc(text: str) -> RawDocument:
    return RawDocument(
        content=text,
        path=Path("doc.txt"),
        metadata={}
    )

def test_chunk_smaller_than_chunk_size():
    doc = make_doc("abcde")
    chunks = chunk_document(doc, chunk_size=10, overlap=2)

    assert len(chunks) == 1
    assert chunks[0].text == "abcde"
    assert chunks[0].metadata["start"] == 0

def test_chunk_exact_chunk_size():
    doc = make_doc("a" * 100)
    chunks = chunk_document(doc, chunk_size=100, overlap=20)

    assert len(chunks) == 2
    assert chunks[0].metadata["start"] == 0
    assert chunks[1].metadata["start"] == 80
    assert chunks[1].metadata["end"] == 100

def test_chunk_multiple_with_overlap():
    doc = make_doc("a" * 1200)
    chunks = chunk_document(doc, chunk_size=500, overlap=100)

    assert len(chunks) == 3
    assert chunks[0].text.startswith("a")
    assert chunks[1].metadata["start"] == 400
    assert chunks[2].metadata["start"] == 800

def test_chunk_truncated_last():
    doc = make_doc("a" * 950)
    chunks = chunk_document(doc, chunk_size=500, overlap=100)

    assert len(chunks) == 3
    assert chunks[2].metadata["start"] == 800
    assert chunks[2].metadata["end"] == 950
    assert len(chunks[2].text) == 150

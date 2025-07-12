from pathlib import Path
from expression.core import Result

from askmydocs_backend.chunking.splitter import chunk_document
from askmydocs_backend.embeddings.embedder import embed_chunks
from askmydocs_backend.vectorstore.qdrant_store import create_client, setup_client, insert_chunks
from askmydocs_backend.ingestion.pdf_loader import extract_text

def index_documents_pipeline(
    path: Path,
    collection_name: str = "public",
    embedding_dim: int = 384
) -> Result[None, Exception]:
    client = create_client()
    setup_client(client, collection_name, dim=embedding_dim)
    
    return extract_text(path).map(
        lambda docs: [chunk for doc in docs for chunk in chunk_document(doc)]
    ).map(
        embed_chunks
    ).map(
        lambda embedded: insert_chunks(client, collection_name, embedded)
    )
    
from typing import List
from sentence_transformers import SentenceTransformer

from askmydocs_backend.domain.document import Chunk, EmbeddedChunk

_model = SentenceTransformer("all-MiniLM-L6-v2")

def embed_texts(texts: List[str]) -> List[List[float]]:
    return _model.encode(texts, convert_to_numpy=True).tolist()

def embed_chunks(chunks: List[Chunk]) -> List[EmbeddedChunk]:
    texts = [chunk.text for chunk in chunks]
    embeddings = embed_texts(texts)
    
    return [
        EmbeddedChunk(
            chunk=chunk,
            embedding=embedding
        )
        for chunk, embedding in zip(chunks, embeddings)
    ]

def embed_question(question: str) -> List[float]:
    return embed_texts([question])[0]

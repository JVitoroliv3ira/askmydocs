import os
from uuid import uuid4
from typing import List, Optional
from pathlib import Path
from qdrant_client import QdrantClient
from qdrant_client.models import (
    PointStruct,
    Distance,
    VectorParams,
    ScoredPoint,
    Filter,
    FieldCondition,
    MatchValue
)

from askmydocs_backend.domain.document import EmbeddedChunk, Chunk


def create_client(url: str = "http://localhost:6333") -> QdrantClient:
    return QdrantClient(url=url)


def setup_client(client: QdrantClient, name: str, dim: int) -> None:
    if not client.collection_exists(name):
        client.recreate_collection(
            collection_name=name,
            vectors_config=VectorParams(size=dim, distance=Distance.COSINE),
        )


def embed_chunk_to_point(chunk: EmbeddedChunk) -> PointStruct:
    document_path = str(chunk.chunk.document_path)
    document_name = os.path.basename(document_path)
    
    return PointStruct(
        id=str(uuid4()),
        vector=chunk.embedding,
        payload={
            "text": chunk.chunk.text,
            "document_path": document_path,
            "document_name": document_name,
            **chunk.chunk.metadata,
        },
    )


def insert_chunks(
    client: QdrantClient,
    collection: str,
    chunks: List[EmbeddedChunk],
) -> None:
    points = [embed_chunk_to_point(chunk) for chunk in chunks]
    client.upsert(collection_name=collection, points=points)


def query_similar_chunks(
    client: QdrantClient,
    collection: str,
    query_embedding: List[float],
    document_name: Optional[str] = None,
    limit: int = 5,
) -> List[ScoredPoint]:
    conditions = [
        FieldCondition(
            key="document_name",
            match=MatchValue(value=document_name)
        )
    ] if document_name else None
        
    
    return client.search(
        collection_name=collection,
        query_vector=query_embedding,
        limit=limit,
        query_filter=Filter(must=conditions) if conditions else None
    )


def scored_point_to_chunk(point: ScoredPoint) -> Chunk:
    return Chunk(
        text=point.payload["text"],
        document_path=Path(point.payload["document_path"]),
        chunk_id=str(point.id),
        metadata={
            k: v
            for k, v in point.payload.items()
            if k not in {"text", "document_path"}
        },
    )

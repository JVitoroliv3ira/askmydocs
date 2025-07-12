from typing import List

from askmydocs_backend.domain.document import RawDocument, Chunk


def chunk_document(doc: RawDocument, chunk_size: int = 500, overlap: int = 100) -> List[Chunk]:
    content = doc.content
    length = len(content)
    
    starts = list(range(0, length, chunk_size - overlap))
    
    return [
        Chunk(
            text=content[start: min(start + chunk_size, length)],
            document_path=doc.path,
            chunk_id=f"{doc.path.stem}_{i}",
            metadata={
                "start": start,
                "end": min(start + chunk_size, length)
            }
        )
        for i, start in enumerate(starts)
    ]

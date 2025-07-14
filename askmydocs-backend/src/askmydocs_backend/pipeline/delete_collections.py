from expression.core import Failure, Result, Success

from askmydocs_backend.vectorstore.qdrant_store import create_client, delete_all_collections


def delete_collections_pipeline() -> Result[None, Exception]:
    try:
        client = create_client()
        delete_all_collections(client)
        
        return Success(None)
    except Exception as e:
        return Failure(e)
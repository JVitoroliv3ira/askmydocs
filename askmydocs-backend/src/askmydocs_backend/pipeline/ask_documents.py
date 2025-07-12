from expression.core import Result, Failure, Success

from askmydocs_backend.embeddings.embedder import embed_question
from askmydocs_backend.llm.openai_llm import ask_openai
from askmydocs_backend.vectorstore.qdrant_store import create_client, query_similar_chunks


def ask_documents_pipeline(
    question: str,
    collection: str = "public",
    top_k: int = 5
) -> Result[str, Exception]:
    try:
        embedding = embed_question(question)

        client = create_client()
        results = query_similar_chunks(client, collection, embedding, limit=top_k)

        context_chunks = [r.payload["text"] for r in results]

        answer = ask_openai(question, context_chunks)

        return Success(answer)
    except Exception as e:
        return Failure(e)
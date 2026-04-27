from app.data.documents import DOCUMENTS
from app.services.embeddings import get_embedding, cosine_similarity


_indexed_documents: list[dict] | None = None


def build_index() -> list[dict]:
    return [
        {
            "text": document,
            "embedding": get_embedding(document),
        }
        for document in DOCUMENTS
    ]


def get_indexed_documents() -> list[dict]:
    global _indexed_documents

    if _indexed_documents is None:
        _indexed_documents = build_index()

    return _indexed_documents


def retrieve_context(question: str, top_k: int = 3) -> list[str]:
    question_vector = get_embedding(question)
    scored_documents = []

    for item in get_indexed_documents():
        score = cosine_similarity(question_vector, item["embedding"])
        scored_documents.append(
            {
                "text": item["text"],
                "score": score,
            }
        )

    scored_documents.sort(key=lambda item: item["score"], reverse=True)

    return [item["text"] for item in scored_documents[:top_k]]

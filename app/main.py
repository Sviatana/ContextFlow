from fastapi import FastAPI

from app.graph import agent_graph
from app.schemas import AskRequest, AskResponse


app = FastAPI(
    title="ContextFlow Agent",
    description="LangGraph-based RAG workflow with validation and repair steps.",
    version="1.0.0",
)


def run_agent(question: str) -> dict:
    return agent_graph.invoke(
        {
            "question": question,
            "context": [],
            "answer": "",
            "is_valid": False,
            "errors": [],
        }
    )


@app.get("/health")
def health_check() -> dict:
    return {"status": "ok"}


@app.post("/ask", response_model=AskResponse)
def ask(request: AskRequest) -> AskResponse:
    result = run_agent(request.question)

    return AskResponse(
        question=result["question"],
        answer=result["answer"],
        context=result["context"],
        is_valid=result["is_valid"],
        errors=result["errors"],
    )


if __name__ == "__main__":
    result = run_agent("What is LangGraph used for?")

    print("QUESTION:")
    print(result["question"])

    print("\nANSWER:")
    print(result["answer"])

    print("\nCONTEXT:")
    for item in result["context"]:
        print(f"- {item}")

    print("\nVALID:")
    print(result["is_valid"])

    print("\nERRORS:")
    print(result["errors"])

from app.state import AgentState
from app.services.retrieval import retrieve_context
from app.services.llm import generate_answer, repair_answer
from app.services.validation import validate_answer


def retrieve_node(state: AgentState) -> AgentState:
    context = retrieve_context(state["question"])
    return {
        **state,
        "context": context,
    }


def generate_node(state: AgentState) -> AgentState:
    answer = generate_answer(
        question=state["question"],
        context=state["context"],
    )
    return {
        **state,
        "answer": answer,
    }


def validate_node(state: AgentState) -> AgentState:
    is_valid, errors = validate_answer(state["answer"])
    return {
        **state,
        "is_valid": is_valid,
        "errors": errors,
    }


def repair_node(state: AgentState) -> AgentState:
    answer = repair_answer(
        question=state["question"],
        context=state["context"],
        previous_answer=state["answer"],
        errors=state["errors"],
    )

    is_valid, errors = validate_answer(answer)

    return {
        **state,
        "answer": answer,
        "is_valid": is_valid,
        "errors": errors,
    }

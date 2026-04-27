from langgraph.graph import StateGraph, START, END

from app.state import AgentState
from app.services.nodes import (
    retrieve_node,
    generate_node,
    validate_node,
    repair_node,
)


def route_after_validation(state: AgentState) -> str:
    if state["is_valid"]:
        return "end"
    return "repair"


def build_graph():
    graph = StateGraph(AgentState)

    graph.add_node("retrieve", retrieve_node)
    graph.add_node("generate", generate_node)
    graph.add_node("validate", validate_node)
    graph.add_node("repair", repair_node)

    graph.add_edge(START, "retrieve")
    graph.add_edge("retrieve", "generate")
    graph.add_edge("generate", "validate")

    graph.add_conditional_edges(
        "validate",
        route_after_validation,
        {
            "end": END,
            "repair": "repair",
        },
    )

    graph.add_edge("repair", END)

    return graph.compile()


agent_graph = build_graph()

from app.agents.chat import ChatState
from app.agents.chat.nodes import chat_node
from langgraph.graph import START, END, StateGraph
from langgraph.checkpoint.base import BaseCheckpointSaver

def build_graph(checkpointer: BaseCheckpointSaver):
    graph = StateGraph(ChatState)

    graph.add_node("chat_node", chat_node)

    graph.add_edge(START, "chat_node")
    graph.add_edge("chat_node", END)

    return graph.compile(checkpointer=checkpointer)
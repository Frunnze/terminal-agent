from langgraph.graph import StateGraph, START, END

from states import MessagesState
from nodes.llm_model import LlmModelNode
from nodes.tool import ToolNode
from routers.continue_with_tools import ContinueWithToolsRouter


class AgentBuilder:
    def __init__(self, model, tools_by_name):
        self.model = model
        self.tools_by_name = tools_by_name

    def build(self):
        agent_builder = StateGraph(MessagesState)

        # Add nodes
        agent_builder.add_node(
            "llm_call", 
            LlmModelNode(self.model).llm_model
        )
        agent_builder.add_node(
            "tool_node", 
            ToolNode(self.tools_by_name).tool_node
        )

        # Add edges
        agent_builder.add_edge(START, "llm_call")
        agent_builder.add_conditional_edges(
            "llm_call",
            ContinueWithToolsRouter().should_continue,
            ["tool_node", END]
        )
        agent_builder.add_edge("tool_node", "llm_call")

        return agent_builder.compile()
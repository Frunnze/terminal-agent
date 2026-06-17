from langgraph.graph import StateGraph, START, END

from states import MessagesState
from nodes.llm_model import LlmModelNode
from nodes.tool import ToolNode
from routers.continue_with_tools import ContinueWithToolsRouter
from interfaces.prompt_loader import IPromptLoader


class AgentBuilder:
    def __init__(
        self,
        model,
        tools_by_name,
        emitter,
        prompt_loader: IPromptLoader,
    ):
        self.model = model
        self.tools_by_name = tools_by_name
        self.emitter = emitter
        self.prompt_loader = prompt_loader

    def build(self):
        agent_builder = StateGraph(MessagesState)

        # Add nodes
        agent_builder.add_node(
            "llm_call",
            LlmModelNode(self.model, self.prompt_loader).llm_model
        )
        agent_builder.add_node(
            "tool_node", 
            ToolNode(self.tools_by_name, self.emitter).tool_node
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
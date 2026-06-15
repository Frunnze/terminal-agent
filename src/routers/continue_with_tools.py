from typing import Literal
from langgraph.graph import END


class ContinueWithToolsRouter:
    def __int__(self):
        pass


    def should_continue(self, state: dict) -> Literal["tool_node", END]:
        messages = state["messages"]
        last_message = messages[-1]

        if last_message.tool_calls:
            return "tool_node"
        
        return END
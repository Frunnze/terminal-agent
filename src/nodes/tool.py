from langchain.messages import ToolMessage


class ToolNode:
    def __init__(self, tools_by_name: dict, emitter):
        self.tools_by_name = tools_by_name
        self.emitter = emitter

    def tool_node(self, state: dict) -> dict:
        result = []

        for tool_call in state["messages"][-1].tool_calls:
            self.emitter.emit_tool_call(
                tool_call["name"], tool_call["args"]
            )

            tool = self.tools_by_name[tool_call["name"]]            
            observation = tool.invoke(tool_call["args"])
            result.append(ToolMessage(
                content=observation, 
                tool_call_id=tool_call["id"]
            ))

        return {"messages": result}
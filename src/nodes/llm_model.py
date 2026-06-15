from langchain.messages import SystemMessage


class LlmModelNode:
    def __init__(self, model):
        self.model = model

    def llm_model(self, state: dict):
        messages = [SystemMessage(content="You are a helpful assistant!")] + state["messages"]
        response = self.model.invoke(messages)
        return {
            "messages": [response],
            "llm_calls": state.get("llm_calls", 0) + 1
        }
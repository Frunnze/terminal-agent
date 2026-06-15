from langchain.messages import SystemMessage


class LlmModelNode:
    def __init__(self, model):
        self.model = model

    def llm_model(self, state: dict):
        system_prompt = self.load_prompt()
        messages = [
            SystemMessage(content=system_prompt)
        ] + state["messages"]
        response = self.model.invoke(messages)
        return {
            "messages": [response],
            "llm_calls": state.get("llm_calls", 0) + 1
        }
    
    def load_prompt(self):
        with open("src/prompts/system_prompt.md") as file:
            return file.read()
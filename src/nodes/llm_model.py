from langchain.messages import SystemMessage

from interfaces.prompt_loader import IPromptLoader


class LlmModelNode:
    def __init__(self, model, prompt_loader: IPromptLoader):
        self.model = model
        self.prompt_loader = prompt_loader

    def llm_model(self, state: dict):
        system_prompt = self.prompt_loader.load_system_prompt()
        messages = [SystemMessage(content=system_prompt)] + state["messages"]
        response = self.model.invoke(messages)
        return {
            "messages": [response],
            "llm_calls": state.get("llm_calls", 0) + 1,
        }

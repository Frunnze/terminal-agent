from abc import ABC, abstractmethod


class IPromptLoader(ABC):
    @abstractmethod
    def load_system_prompt(self) -> str: ...

    @abstractmethod
    def load_tool_description(self, tool_name: str) -> str: ...

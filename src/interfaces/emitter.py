from abc import ABC, abstractmethod


class IEmitter(ABC):
    @abstractmethod
    def emit(self, message: str) -> None: ...

    @abstractmethod
    def emit_tool_call(self, name: str, args: dict) -> None: ...

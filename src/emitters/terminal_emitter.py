from config import MAX_TOOL_ARG_PRINT_CHARS
from interfaces.emitter import IEmitter


class TerminalEmitter(IEmitter):
    def __init__(self):
        pass

    def emit(self, input: str):
        print(input)

    def emit_tool_call(self, name: str, args: dict):
        trimmed = {
            k: str(v)[:MAX_TOOL_ARG_PRINT_CHARS]
            for k, v in args.items()
        }
        print(f"Tool: {name}({trimmed})")
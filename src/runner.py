import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent))

from langchain_core.messages import HumanMessage

from model import model
from graph import AgentBuilder

from emitters.terminal_emitter import TerminalEmitter
from prompts.prompt_loader import PromptLoader

from tools.read_text_file import TextFileReaderTool
from tools.modify_text_file import TextFileModifierTool
from tools.bash import BashTool
from tools.memorize import MemorizeTool
from tools.recall import RecallTool
from vectordb.chroma_db_manager import ChromaDb


def main():
    emitter = TerminalEmitter()
    prompt_loader = PromptLoader()
    vdb = ChromaDb()

    tools = [
        TextFileReaderTool(),
        TextFileModifierTool(emitter),
        BashTool().bash,
        MemorizeTool(vdb=vdb),
        RecallTool(vdb=vdb),
    ]
    tools_by_name = {tool.name: tool for tool in tools}

    model_with_tools = model.bind_tools(tools=tools)

    agent = AgentBuilder(
        model=model_with_tools,
        tools_by_name=tools_by_name,
        emitter=emitter,
        prompt_loader=prompt_loader,
    )
    agent = agent.build()

    messages = {"messages": []}
    while True:
        emitter.emit("="*50)
        user_input = input(">")

        if user_input == "/clear":
            messages = {"messages": []}
            continue

        if user_input == "/exit":
            break

        messages["messages"].append(
            HumanMessage(
                content=user_input
            )
        )
        messages = agent.invoke(messages)
        last_message = messages["messages"][-1]
        emitter.emit(f"\n>AI: {last_message.content}")

main()
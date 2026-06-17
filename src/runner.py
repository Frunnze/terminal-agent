from langchain.messages import HumanMessage

from model import model
from graph import AgentBuilder
from tools.read_text_file import TextFileReaderTool
from tools.modify_text_file import TextFileModifierTool
from tools.bash import BashTool
from emitters.terminal_emitter import TerminalEmitter

emitter = TerminalEmitter()

# Add tools
tools = [
    TextFileReaderTool().read_text_file,
    TextFileModifierTool(emitter).modify_text_file,
    BashTool().bash
]
tools_by_name = {tool.name: tool for tool in tools}

# Add tools to the agent
model_with_tools = model.bind_tools(tools=tools)

agent = AgentBuilder(
    model=model_with_tools,
    tools_by_name=tools_by_name,
    emitter=emitter
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
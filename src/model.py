import os
import json
from pathlib import Path
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain_core.callbacks import BaseCallbackHandler

load_dotenv()


LOGS_DIR = Path(__file__).parent.parent / "logs"
LOGS_DIR.mkdir(exist_ok=True)


class RawLogger(BaseCallbackHandler):
    def on_chat_model_start(self, serialized, messages, *, run_id, parent_run_id=None, tags=None, metadata=None, **kwargs):
        with open(LOGS_DIR / "input.json", "w") as file:
            data = [msg.dict() for msg in messages[0]]
            json.dump(data, file, indent=2)

    def on_llm_end(self, response, *, run_id, parent_run_id=None, **kwargs):
        with open(LOGS_DIR / "output.json", "w") as file:
            data = [[g.message.dict() for g in gen] for gen in response.generations]
            json.dump(data, file, indent=2)


model = ChatOpenAI(
    model="gpt-5.4-nano",
    api_key=os.getenv("OPENAI_API_KEY"),
    callbacks=[RawLogger()]
)
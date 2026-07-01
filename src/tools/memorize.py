from typing import Literal
from langchain.tools import BaseTool

from interfaces.vector_db_manager import VectorDbManager
from prompts.prompt_loader import PromptLoader


class MemorizeTool(BaseTool):
    name: str = "memorize"
    description: str = PromptLoader().load_tool_description("memorize")
    vdb: VectorDbManager | None = None

    def __init__(self, vdb: VectorDbManager):
        super().__init__()
        self.vdb = vdb

    def _run(
        self,
        information: str,
        information_type: Literal["fact", "idea", "mistake", "solution"] = "fact"
    ) -> str:
        try:
            # Save the information in vector db
            self.vdb.save(
                document=information,
                collection_name=information_type
            )

            return (
                f"Information '{information}' was saved"
                f" in '{information_type}' collection."
            )
        except Exception as e:
            return f"Error memorizing information: {e}"

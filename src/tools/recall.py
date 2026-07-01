from langchain.tools import BaseTool

from interfaces.vector_db_manager import VectorDbManager
from prompts.prompt_loader import PromptLoader

_COLLECTIONS = ["fact", "idea", "mistake", "solution"]


class RecallTool(BaseTool):
    name: str = "recall"
    description: str = PromptLoader().load_tool_description("recall")
    vdb: VectorDbManager | None = None

    def __init__(self, vdb: VectorDbManager):
        super().__init__()
        self.vdb = vdb

    def _run(self, query: str, n_results: int = 3) -> str:
        results = []
        for collection in _COLLECTIONS:
            try:
                data = self.vdb.query(
                    query=query,
                    collection_name=collection,
                    n_results=n_results
                )
                docs = data.get("documents", [[]])[0] if data else []
                for doc in docs:
                    results.append(f"[{collection}] {doc}")
            except Exception:
                continue

        if not results:
            return "No relevant memories found."

        return "\n".join(results)

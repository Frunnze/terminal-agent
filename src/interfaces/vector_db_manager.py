from abc import ABC, abstractmethod


class VectorDbManager(ABC):
    @abstractmethod
    def save(self, document: str, collection_name: str) -> bool: ...

    @abstractmethod
    def query(self, query: str, collection_name: str, n_results: int = 2) -> dict | None: ...

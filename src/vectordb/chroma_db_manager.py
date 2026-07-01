import os
import hashlib
import chromadb
from chromadb.utils.embedding_functions import OpenAIEmbeddingFunction

from interfaces.vector_db_manager import VectorDbManager


class ChromaDb(VectorDbManager):
    def __init__(self):
        self.chroma_client = chromadb.PersistentClient(
            path="./chroma_vector_db"
        )
        self.embedding_function = OpenAIEmbeddingFunction(
            api_key=os.getenv("OPENAI_API_KEY"),
            model_name="text-embedding-3-small"
        )

    def save(self, document: str, collection_name: str):
        try:
            collection = self.chroma_client.get_or_create_collection(
                name=collection_name,
                embedding_function=self.embedding_function
            )

            id = hashlib.md5(document.encode()).hexdigest()
            collection.add(
                ids=[id],
                documents=[document]
            )

            return True
        except Exception as e:
            print(e)
            return False


    def query(self, query: str, collection_name: str, n_results: int = 2):
        try:
            collection = self.chroma_client.get_or_create_collection(
                name=collection_name,
                embedding_function=self.embedding_function
            )

            results = collection.query(
                query_texts=[query],
                n_results=n_results
            )

            return results
        except Exception as e:
            print(e)
            return None
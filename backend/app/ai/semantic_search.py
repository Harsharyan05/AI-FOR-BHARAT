"""
Semantic Search

Searches repository knowledge using vector similarity.

Author: Harsh Aryan
Project: Cognisys
"""

from typing import List

from sentence_transformers import SentenceTransformer

from app.ai.vector_store import VectorStore


class SemanticSearch:
    """
    Semantic search over repository documents.
    """

    MODEL_NAME = "sentence-transformers/all-MiniLM-L6-v2"

    def __init__(self):

        print("Loading embedding model...")

        self.model = SentenceTransformer(
            self.MODEL_NAME
        )

        print("Embedding model loaded.")

        self.vector_store = VectorStore()

        self.vector_store.load()

    def search(
        self,
        query: str,
        top_k: int = 15,
    ) -> List[dict]:
        """
        Search repository using natural language.
        """

        query_vector = self.model.encode(
            query,
            convert_to_numpy=True,
        )

        return self.vector_store.search(
            query_vector.tolist(),
            top_k=top_k,
        )
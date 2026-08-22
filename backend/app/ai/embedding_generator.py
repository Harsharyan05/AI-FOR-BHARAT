"""
Embedding Generator

Generates embeddings for document chunks.

Author: Harsh Aryan
Project: Cognisys
"""

import json
from pathlib import Path
from typing import List

from sentence_transformers import SentenceTransformer

from app.ai.chunk_models import Chunk
from app.ai.embedding_models import Embedding


class EmbeddingGenerator:
    """
    Generates embeddings using Sentence Transformers.
    """

    MODEL_NAME = "sentence-transformers/all-MiniLM-L6-v2"

    def __init__(
        self,
        output_directory: str = "storage/embeddings",
    ):
        self.output_directory = Path(output_directory)

        self.output_directory.mkdir(
            parents=True,
            exist_ok=True,
        )

        print("Loading embedding model...")

        self.model = SentenceTransformer(
            self.MODEL_NAME
        )

        print("Embedding model loaded.")

    def generate(
        self,
        chunks: List[Chunk],
    ) -> List[Embedding]:
        """
        Generate embeddings for chunks.
        """

        embeddings = []

        for chunk in chunks:

            vector = self.model.encode(
                chunk.content,
                convert_to_numpy=True,
            )

            embedding = Embedding(
                chunk_id=chunk.id,
                title=chunk.title,
                vector=vector.tolist(),
                dimension=len(vector),
                word_count=chunk.word_count,
            )

            embeddings.append(embedding)

        self._save_embeddings(
            embeddings
        )

        return embeddings

    def _save_embeddings(
        self,
        embeddings: List[Embedding],
    ):
        """
        Save embeddings as JSON.
        """

        output_file = (
            self.output_directory /
            "embeddings.json"
        )

        data = []

        for embedding in embeddings:

            data.append(
                {
                    "chunk_id": embedding.chunk_id,
                    "title": embedding.title,
                    "dimension": embedding.dimension,
                    "word_count": embedding.word_count,
                    "vector": embedding.vector,
                }
            )

        with open(
            output_file,
            "w",
            encoding="utf-8",
        ) as file:

            json.dump(
                data,
                file,
                indent=4,
            )
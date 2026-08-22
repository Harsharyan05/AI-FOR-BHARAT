"""
Multi Vector Store

Builds a FAISS vector database from repository embeddings.

Author: Harsh Aryan
Project: Cognisys
"""

from pathlib import Path
import pickle
from typing import List

import faiss
import numpy as np

from app.ai.embedding_models import Embedding


class MultiVectorStore:
    """
    FAISS vector store for repository embeddings.
    """

    def __init__(
        self,
        output_directory: str = "storage/vector_db",
    ):

        self.output_directory = Path(output_directory)

        self.output_directory.mkdir(
            parents=True,
            exist_ok=True,
        )

        self.index = None
        self.metadata = []

    def build(
        self,
        embeddings: List[Embedding],
    ):

        if not embeddings:
            raise ValueError(
                "No embeddings were provided."
            )

        dimension = embeddings[0].dimension

        self.index = faiss.IndexFlatL2(
            dimension
        )

        vectors = np.array(
            [
                embedding.vector.astype("float32")
                for embedding in embeddings
            ]
        )

        self.index.add(vectors)

        self.metadata = embeddings

        self._save()

        return self.index

    def search(
        self,
        query_vector,
        k: int = 15,
    ):

        if self.index is None:
            self._load()

        query = np.array(
            [query_vector.astype("float32")]
        )

        distances, indices = self.index.search(
            query,
            k,
        )

        results = []

        for distance, index in zip(
            distances[0],
            indices[0],
        ):

            if index == -1:
                continue

            results.append(
                (
                    self.metadata[index],
                    float(distance),
                )
            )

        return results

    def _save(self):

        faiss.write_index(
            self.index,
            str(
                self.output_directory /
                "index.faiss"
            ),
        )

        with open(
            self.output_directory /
            "metadata.pkl",
            "wb",
        ) as file:

            pickle.dump(
                self.metadata,
                file,
            )

    def _load(self):

        self.index = faiss.read_index(
            str(
                self.output_directory /
                "index.faiss"
            )
        )

        with open(
            self.output_directory /
            "metadata.pkl",
            "rb",
        ) as file:

            self.metadata = pickle.load(
                file
            )
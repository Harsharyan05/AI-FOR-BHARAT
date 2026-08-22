"""
Vector Store

Stores and searches embeddings using FAISS.

Author: Harsh Aryan
Project: Cognisys
"""

import json
from pathlib import Path
from typing import List

import faiss
import numpy as np


class VectorStore:
    """
    FAISS Vector Store.
    """

    def __init__(
        self,
        embedding_file: str = "storage/embeddings/embeddings.json",
        output_directory: str = "storage/vector_db",
    ):
        self.embedding_file = Path(embedding_file)

        self.output_directory = Path(output_directory)

        self.output_directory.mkdir(
            parents=True,
            exist_ok=True,
        )

        self.index = None
        self.metadata = []

    def build(self):
        """
        Build FAISS index.
        """

        with open(
            self.embedding_file,
            "r",
            encoding="utf-8",
        ) as file:

            embeddings = json.load(file)

        vectors = np.array(
            [
                item["vector"]
                for item in embeddings
            ],
            dtype=np.float32,
        )

        dimension = vectors.shape[1]

        self.index = faiss.IndexFlatL2(
            dimension
        )

        self.index.add(vectors)

        self.metadata = embeddings

        faiss.write_index(
            self.index,
            str(
                self.output_directory /
                "faiss.index"
            ),
        )

        with open(
            self.output_directory /
            "metadata.json",
            "w",
            encoding="utf-8",
        ) as file:

            json.dump(
                embeddings,
                file,
                indent=4,
            )

    def load(self):
        """
        Load existing FAISS index.
        """

        self.index = faiss.read_index(
            str(
                self.output_directory /
                "faiss.index"
            )
        )

        with open(
            self.output_directory /
            "metadata.json",
            "r",
            encoding="utf-8",
        ) as file:

            self.metadata = json.load(file)

    def search(
        self,
        vector: List[float],
        top_k: int = 10,
    ):
        """
        Search nearest embeddings.
        """

        query = np.array(
            [vector],
            dtype=np.float32,
        )

        distances, indices = self.index.search(
            query,
            top_k,
        )

        results = []

        for distance, index in zip(
            distances[0],
            indices[0],
        ):

            if index == -1:
                continue

            item = self.metadata[index].copy()

            item["distance"] = float(
                distance
            )

            results.append(item)

        return results
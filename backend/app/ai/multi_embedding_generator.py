"""
Multi Embedding Generator

Generates embeddings for every semantic chunk.

Author: Harsh Aryan
Project: Cognisys
"""

from pathlib import Path
from typing import List

from sentence_transformers import SentenceTransformer

from app.ai.embedding_models import Embedding


class MultiEmbeddingGenerator:
    """
    Generates embeddings for all chunk files.
    """

    def __init__(
        self,
        chunks_directory: str = "storage/chunks",
        model_name: str = "sentence-transformers/all-MiniLM-L6-v2",
    ):

        self.chunks_directory = Path(chunks_directory)

        print("Loading embedding model...")

        self.model = SentenceTransformer(model_name)

        print("Embedding model loaded.")

    def generate(self) -> List[Embedding]:

        embeddings = []

        chunk_files = sorted(
            self.chunks_directory.glob("chunk_*.md")
        )

        for index, chunk_file in enumerate(chunk_files, start=1):

            text = chunk_file.read_text(
                encoding="utf-8"
            )

            lines = text.splitlines()

            title = "Unknown"

            source_document = "Unknown"

            if lines:

                if lines[0].startswith("#"):

                    title = (
                        lines[0]
                        .replace("#", "")
                        .strip()
                    )

            for line in lines:

                if line.startswith(
                    "Source Document:"
                ):

                    source_document = (
                        line.split(
                            ":",
                            1,
                        )[1]
                        .strip()
                    )

                    break

            vector = self.model.encode(
                text,
                convert_to_numpy=True,
            )

            embeddings.append(

                Embedding(

                    chunk_id=index,

                    title=title,

                    source_document=source_document,

                    text=text,

                    vector=vector,

                    dimension=len(vector),

                    word_count=len(
                        text.split()
                    ),

                )

            )

        return embeddings
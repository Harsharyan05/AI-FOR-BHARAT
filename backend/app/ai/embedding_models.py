"""
Embedding Models

Defines the data model used for storing repository
embeddings and metadata.

Author: Harsh Aryan
Project: Cognisys
"""

from dataclasses import dataclass, field
from typing import Dict, Any
import numpy as np


@dataclass
class Embedding:
    """
    Represents one repository chunk embedding.
    """

    # -------------------------
    # Chunk Metadata
    # -------------------------

    chunk_id: int

    title: str

    source_document: str

    section: str = ""

    # -------------------------
    # Chunk Content
    # -------------------------

    text: str = ""

    word_count: int = 0

    # -------------------------
    # Embedding
    # -------------------------

    vector: np.ndarray = field(
        default_factory=lambda: np.array([])
    )

    dimension: int = 0

    # -------------------------
    # Source Information
    # -------------------------

    line_start: int = 0

    line_end: int = 0

    # -------------------------
    # Additional Metadata
    # -------------------------

    metadata: Dict[str, Any] = field(
        default_factory=dict
    )

    # -------------------------
    # Utility
    # -------------------------

    def preview(
        self,
        length: int = 200,
    ) -> str:
        """
        Returns a short preview of the chunk.
        """

        if len(self.text) <= length:
            return self.text

        return self.text[:length] + "..."

    @property
    def filename(self) -> str:
        """
        Alias for source document.
        """

        return self.source_document

    def __repr__(self):

        return (
            f"Embedding("
            f"chunk_id={self.chunk_id}, "
            f"title='{self.title}', "
            f"document='{self.source_document}', "
            f"words={self.word_count}, "
            f"dimension={self.dimension})"
        )
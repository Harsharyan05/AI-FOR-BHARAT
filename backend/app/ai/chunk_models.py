"""
Chunk Models

Author: Harsh Aryan
Project: Cognisys
"""

from dataclasses import dataclass


@dataclass
class Chunk:
    """
    Represents a semantic document chunk.
    """

    id: int
    title: str
    content: str
    word_count: int
    line_count: int
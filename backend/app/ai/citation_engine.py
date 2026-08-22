"""
Citation Engine

Generates repository citations for retrieved
knowledge chunks.

Author: Harsh Aryan
Project: Cognisys
"""

from dataclasses import dataclass
from typing import List

from app.ai.embedding_models import Embedding


@dataclass
class Citation:
    """
    Represents a repository citation.
    """

    document: str
    title: str
    chunk_id: int
    score: float


class CitationEngine:
    """
    Generates citations from retrieved chunks.

    Features
    --------
    • Remove duplicate citations
    • Sort by score
    • Markdown formatting
    • Plain text formatting
    """

    def __init__(self):

        pass
    
    # ---------------------------------------------------------
    # Extract Citations
    # ---------------------------------------------------------

    def extract(
        self,
        retrieved_results,
    ) -> List[Citation]:
        """
        Extracts citations from HybridRetriever results.

        Parameters
        ----------
        retrieved_results

            [
                (
                    score,
                    embedding,
                    distance,
                ),
                ...
            ]
        """

        citations = []

        for score, embedding, distance in retrieved_results:

            citations.append(

                Citation(

                    document=embedding.source_document,

                    title=embedding.title,

                    chunk_id=embedding.chunk_id,

                    score=score,

                )

            )

        citations = self.remove_duplicates(
            citations
        )

        citations = self.sort_by_score(
            citations
        )

        return citations

    # ---------------------------------------------------------
    # Remove Duplicate Citations
    # ---------------------------------------------------------

    def remove_duplicates(
        self,
        citations: List[Citation],
    ) -> List[Citation]:
        """
        Removes duplicate citations.
        """

        unique = []

        seen = set()

        for citation in citations:

            key = (

                citation.document,

                citation.chunk_id,

            )

            if key in seen:

                continue

            seen.add(key)

            unique.append(
                citation
            )

        return unique

    # ---------------------------------------------------------
    # Sort By Score
    # ---------------------------------------------------------

    def sort_by_score(
        self,
        citations: List[Citation],
    ) -> List[Citation]:
        """
        Sorts citations by descending score.
        """

        return sorted(

            citations,

            key=lambda citation: citation.score,

            reverse=True,

        )
        
    # ---------------------------------------------------------
    # Markdown Formatter
    # ---------------------------------------------------------

    def to_markdown(
        self,
        citations: List[Citation],
    ) -> str:
        """
        Returns citations formatted as Markdown.
        """

        if not citations:

            return "No citations available."

        lines = []

        lines.append("## Sources\n")

        for index, citation in enumerate(
            citations,
            start=1,
        ):

            lines.append(
                f"{index}. **{citation.document}**"
            )

            lines.append(
                f"   - Title : {citation.title}"
            )

            lines.append(
                f"   - Chunk ID : {citation.chunk_id}"
            )

            lines.append(
                f"   - Score : {citation.score:.2f}\n"
            )

        return "\n".join(lines)

    # ---------------------------------------------------------
    # Plain Text Formatter
    # ---------------------------------------------------------

    def to_text(
        self,
        citations: List[Citation],
    ) -> str:
        """
        Returns citations formatted as plain text.
        """

        if not citations:

            return "No citations available."

        lines = []

        lines.append("=" * 70)
        lines.append("Repository Sources")
        lines.append("=" * 70)

        for index, citation in enumerate(
            citations,
            start=1,
        ):

            lines.append(
                f"\nSource {index}"
            )

            lines.append("-" * 70)

            lines.append(
                f"Document : {citation.document}"
            )

            lines.append(
                f"Title : {citation.title}"
            )

            lines.append(
                f"Chunk ID : {citation.chunk_id}"
            )

            lines.append(
                f"Score : {citation.score:.2f}"
            )

        return "\n".join(lines)

    # ---------------------------------------------------------
    # Display Citations
    # ---------------------------------------------------------

    def display(
        self,
        citations: List[Citation],
    ) -> None:
        """
        Prints citations to the console.
        """

        print(
            self.to_text(
                citations
            )
        )
        
    # ---------------------------------------------------------
    # Markdown Formatter
    # ---------------------------------------------------------

    def to_markdown(
        self,
        citations: List[Citation],
    ) -> str:
        """
        Returns citations formatted as Markdown.
        """

        if not citations:

            return "No citations available."

        lines = []

        lines.append("## Sources\n")

        for index, citation in enumerate(
            citations,
            start=1,
        ):

            lines.append(
                f"{index}. **{citation.document}**"
            )

            lines.append(
                f"   - Title : {citation.title}"
            )

            lines.append(
                f"   - Chunk ID : {citation.chunk_id}"
            )

            lines.append(
                f"   - Score : {citation.score:.2f}\n"
            )

        return "\n".join(lines)

    # ---------------------------------------------------------
    # Plain Text Formatter
    # ---------------------------------------------------------

    def to_text(
        self,
        citations: List[Citation],
    ) -> str:
        """
        Returns citations formatted as plain text.
        """

        if not citations:

            return "No citations available."

        lines = []

        lines.append("=" * 70)
        lines.append("Repository Sources")
        lines.append("=" * 70)

        for index, citation in enumerate(
            citations,
            start=1,
        ):

            lines.append(
                f"\nSource {index}"
            )

            lines.append("-" * 70)

            lines.append(
                f"Document : {citation.document}"
            )

            lines.append(
                f"Title : {citation.title}"
            )

            lines.append(
                f"Chunk ID : {citation.chunk_id}"
            )

            lines.append(
                f"Score : {citation.score:.2f}"
            )

        return "\n".join(lines)

    # ---------------------------------------------------------
    # Display Citations
    # ---------------------------------------------------------

    def display(
        self,
        citations: List[Citation],
    ) -> None:
        """
        Prints citations to the console.
        """

        print(
            self.to_text(
                citations
            )
        )
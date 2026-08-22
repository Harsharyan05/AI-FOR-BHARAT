"""
Answer Formatter

Formats AI responses into clean, structured,
professional repository answers.

Author: Harsh Aryan
Project: Cognisys
"""

from typing import List

from app.ai.citation_engine import Citation


class AnswerFormatter:
    """
    Formats repository answers.

    Features
    --------
    • Adds section headings
    • Formats citations
    • Formats markdown
    • Builds final response
    """

    def __init__(self):

        pass
    
    # ---------------------------------------------------------
    # Clean Answer
    # ---------------------------------------------------------

    def _clean_answer(
        self,
        answer: str,
    ) -> str:
        """
        Cleans the raw LLM response.
        """

        if not answer:

            return "No answer generated."

        answer = answer.strip()

        while "\n\n\n" in answer:

            answer = answer.replace(
                "\n\n\n",
                "\n\n",
            )

        return answer

    # ---------------------------------------------------------
    # Format Header
    # ---------------------------------------------------------

    def _format_header(
        self,
        title: str,
    ) -> str:
        """
        Creates a section header.
        """

        return (
            "\n"
            + "=" * 80
            + "\n"
            + title
            + "\n"
            + "=" * 80
        )

    # ---------------------------------------------------------
    # Format Citations
    # ---------------------------------------------------------

    def _format_citations(
        self,
        citations: List[Citation],
    ) -> str:
        """
        Formats repository citations.
        """

        if not citations:

            return (
                "No repository sources available."
            )

        lines = []

        for index, citation in enumerate(
            citations,
            start=1,
        ):

            lines.append(

                f"{index}. {citation.document}"

            )

            lines.append(

                f"   Title : {citation.title}"

            )

            lines.append(

                f"   Chunk : {citation.chunk_id}"

            )

            lines.append(

                f"   Score : {citation.score:.2f}"

            )

            lines.append("")

        return "\n".join(lines)
    
    # ---------------------------------------------------------
    # Format Plain Text
    # ---------------------------------------------------------

    def format_text(
        self,
        answer: str,
        citations: List[Citation],
    ) -> str:
        """
        Formats the final response as plain text.
        """

        answer = self._clean_answer(
            answer
        )

        sections = []

        sections.append(
            self._format_header(
                "Repository Answer"
            )
        )

        sections.append(answer)

        sections.append(
            self._format_header(
                "Repository Sources"
            )
        )

        sections.append(
            self._format_citations(
                citations
            )
        )

        return "\n".join(
            sections
        )

    # ---------------------------------------------------------
    # Format Markdown
    # ---------------------------------------------------------

    def format_markdown(
        self,
        answer: str,
        citations: List[Citation],
    ) -> str:
        """
        Formats the final response in Markdown.
        """

        answer = self._clean_answer(
            answer
        )

        markdown = []

        markdown.append(
            "# Repository Answer\n"
        )

        markdown.append(answer)

        markdown.append(
            "\n---\n"
        )

        markdown.append(
            "## Repository Sources\n"
        )

        if not citations:

            markdown.append(
                "_No citations available._"
            )

        else:

            for citation in citations:

                markdown.append(

                    f"- **{citation.document}**"

                )

                markdown.append(

                    f"  - Title: {citation.title}"

                )

                markdown.append(

                    f"  - Chunk ID: {citation.chunk_id}"

                )

                markdown.append(

                    f"  - Score: {citation.score:.2f}\n"

                )

        return "\n".join(
            markdown
        )
        
    # ---------------------------------------------------------
    # Display Answer
    # ---------------------------------------------------------

    def display(
        self,
        answer: str,
        citations: List[Citation],
    ) -> None:
        """
        Prints the formatted repository answer.
        """

        print(
            self.format_text(
                answer,
                citations,
            )
        )

    # ---------------------------------------------------------
    # Statistics
    # ---------------------------------------------------------

    def statistics(
        self,
        answer: str,
        citations: List[Citation],
    ) -> None:
        """
        Displays formatting statistics.
        """

        answer = self._clean_answer(
            answer
        )

        print("\n")
        print("=" * 60)
        print("Answer Formatter Statistics")
        print("=" * 60)

        print(
            f"Characters : {len(answer)}"
        )

        print(
            f"Words : {len(answer.split())}"
        )

        print(
            f"Lines : {len(answer.splitlines())}"
        )

        print(
            f"Citations : {len(citations)}"
        )

        print("=" * 60)

    # ---------------------------------------------------------
    # Format Final Response
    # ---------------------------------------------------------

    def format(
        self,
        answer: str,
        citations: List[Citation],
        markdown: bool = False,
    ) -> str:
        """
        Formats the final repository response.

        Parameters
        ----------
        answer : str
            Raw LLM response.

        citations : List[Citation]
            Repository citations.

        markdown : bool
            If True, returns Markdown.
            Otherwise returns plain text.
        """

        if markdown:

            return self.format_markdown(
                answer,
                citations,
            )

        return self.format_text(
            answer,
            citations,
        )    
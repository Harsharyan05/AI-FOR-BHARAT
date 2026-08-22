"""
Chunking Engine

Splits repository documents into semantic chunks.

Author: Harsh Aryan
Project: Cognisys
"""

from pathlib import Path
from typing import List

from app.ai.chunk_models import Chunk


class Chunker:
    """
    Semantic document chunker.
    """

    def __init__(
        self,
        document_path: str,
        output_directory: str = "storage/chunks",
    ):
        self.document_path = Path(document_path)
        self.output_directory = Path(output_directory)

        self.output_directory.mkdir(
            parents=True,
            exist_ok=True,
        )

    def chunk(self) -> List[Chunk]:
        """
        Split markdown document into semantic chunks.
        """

        text = self.document_path.read_text(
            encoding="utf-8"
        )

        sections = self._split_sections(text)

        chunks: List[Chunk] = []

        for index, section in enumerate(sections, start=1):

            lines = [
                line
                for line in section.splitlines()
                if line.strip()
            ]

            if not lines:
                continue

            title = lines[0].replace("#", "").strip()

            content = section.strip()

            chunk = Chunk(
                id=index,
                title=title,
                content=content,
                word_count=len(content.split()),
                line_count=len(lines),
            )

            chunks.append(chunk)

            self._save_chunk(chunk)

        return chunks

    def _split_sections(
        self,
        text: str,
    ) -> List[str]:
        """
        Split markdown using second-level headings.
        """

        sections = []

        current = []

        for line in text.splitlines():

            if line.startswith("## ") and current:

                sections.append(
                    "\n".join(current).strip()
                )

                current = []

            current.append(line)

        if current:
            sections.append(
                "\n".join(current).strip()
            )

        return sections

    def _save_chunk(
        self,
        chunk: Chunk,
    ):
        """
        Save chunk as markdown file.
        """

        filename = (
            self.output_directory /
            f"chunk_{chunk.id:03}.md"
        )

        with open(
            filename,
            "w",
            encoding="utf-8",
        ) as file:

            file.write(chunk.content)
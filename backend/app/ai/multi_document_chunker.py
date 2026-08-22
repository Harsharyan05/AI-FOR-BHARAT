"""
Multi Document Chunker

Splits every Markdown document into semantic chunks.

Author: Harsh Aryan
Project: Cognisys
"""

from pathlib import Path
from dataclasses import dataclass
from typing import List


@dataclass
class Chunk:
    """
    Represents a semantic chunk.
    """

    chunk_id: int
    source_document: str
    title: str
    content: str
    word_count: int


class MultiDocumentChunker:
    """
    Chunks every markdown document inside storage/documents.
    """

    def __init__(
        self,
        documents_directory: str = "storage/documents",
        output_directory: str = "storage/chunks",
    ):

        self.documents_directory = Path(
            documents_directory
        )

        self.output_directory = Path(
            output_directory
        )

        self.output_directory.mkdir(
            parents=True,
            exist_ok=True,
        )

    def chunk(self) -> List[Chunk]:

        chunks = []

        chunk_id = 1

        markdown_files = sorted(
            self.documents_directory.glob("*.md")
        )

        for document in markdown_files:

            text = document.read_text(
                encoding="utf-8"
            )

            sections = self._split_sections(
                text
            )

            for title, content in sections:

                chunk = Chunk(
                    chunk_id=chunk_id,
                    source_document=document.name,
                    title=title,
                    content=content.strip(),
                    word_count=len(
                        content.split()
                    ),
                )

                chunks.append(chunk)

                self._save_chunk(chunk)

                chunk_id += 1

        return chunks

    def _split_sections(
        self,
        text: str,
    ):

        sections = []

        current_title = "Introduction"

        current_content = []

        for line in text.splitlines():

            if line.startswith("#"):

                if current_content:

                    sections.append(
                        (
                            current_title,
                            "\n".join(
                                current_content
                            ),
                        )
                    )

                current_title = line.replace(
                    "#",
                    "",
                ).strip()

                current_content = []

            else:

                current_content.append(line)

        if current_content:

            sections.append(
                (
                    current_title,
                    "\n".join(
                        current_content
                    ),
                )
            )

        return sections

    def _save_chunk(
        self,
        chunk: Chunk,
    ):

        filename = (
            self.output_directory /
            f"chunk_{chunk.chunk_id:03}.md"
        )

        with open(
            filename,
            "w",
            encoding="utf-8",
        ) as file:

            file.write(
                f"# {chunk.title}\n\n"
            )

            file.write(
                f"Source Document: "
                f"{chunk.source_document}\n\n"
            )

            file.write(chunk.content)
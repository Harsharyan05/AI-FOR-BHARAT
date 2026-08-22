"""
Repository Overview Generator

Generates a high-level repository overview that is
prepended to every LLM prompt.

Author: Harsh Aryan
Project: Cognisys
"""

from pathlib import Path
from typing import Dict


class RepositoryOverviewGenerator:
    """
    Generates a concise repository overview using
    previously generated knowledge documents.
    """

    def __init__(
        self,
        documents_directory: str = "storage/documents",
    ):

        self.documents_directory = Path(
            documents_directory
        )

    # ---------------------------------------------------------
    # Read Document
    # ---------------------------------------------------------

    def _read_document(
        self,
        filename: str,
    ) -> str:
        """
        Reads a markdown document.
        """

        path = self.documents_directory / filename

        if not path.exists():
            return ""

        return path.read_text(
            encoding="utf-8",
            errors="ignore",
        )

    # ---------------------------------------------------------
    # Extract Headings
    # ---------------------------------------------------------

    def _extract_headings(
        self,
        text: str,
    ) -> list[str]:
        """
        Returns markdown headings.
        """

        headings = []

        for line in text.splitlines():

            line = line.strip()

            if line.startswith("#"):

                headings.append(
                    line.replace("#", "").strip()
                )

        return headings

    # ---------------------------------------------------------
    # Count Sections
    # ---------------------------------------------------------

    def _count_sections(
        self,
        text: str,
    ) -> int:

        return len(
            self._extract_headings(text)
        )

    # ---------------------------------------------------------
    # Build Statistics
    # ---------------------------------------------------------

    def _build_statistics(self) -> Dict:

        stats = {}

        documents = list(
            self.documents_directory.glob("*.md")
        )

        stats["documents"] = len(documents)

        stats["total_size"] = sum(
            document.stat().st_size
            for document in documents
        )

        stats["names"] = sorted(
            document.name
            for document in documents
        )

        return stats

    # ---------------------------------------------------------
    # Generate Repository Overview
    # ---------------------------------------------------------

    def generate(self) -> str:
        """
        Generates a high-level repository overview.
        """

        architecture = self._read_document(
            "architecture.md"
        )

        services = self._read_document(
            "services.md"
        )

        apis = self._read_document(
            "apis.md"
        )

        technologies = self._read_document(
            "technologies.md"
        )

        dependency_graph = self._read_document(
            "dependency_graph.md"
        )

        hotspots = self._read_document(
            "hotspots.md"
        )

        recommendations = self._read_document(
            "recommendations.md"
        )

        patterns = self._read_document(
            "architecture_patterns.md"
        )

        stats = self._build_statistics()

        overview = []

        overview.append("# Repository Overview\n")

        overview.append(
            "This repository has been automatically analysed by Cognisys.\n"
        )

        overview.append(
            "It contains architecture knowledge, dependency analysis, "
            "services, APIs, hotspots and recommendations.\n"
        )

        # -------------------------------------------------
        # Repository Statistics
        # -------------------------------------------------

        overview.append("\n## Repository Statistics\n")

        overview.append(
            f"- Knowledge Documents : {stats['documents']}"
        )

        overview.append(
            f"- Total Size : {stats['total_size']} bytes\n"
        )

        # -------------------------------------------------
        # Architecture
        # -------------------------------------------------

        if architecture:

            overview.append("## Architecture\n")

            headings = self._extract_headings(
                architecture
            )

            for heading in headings[1:]:

                overview.append(
                    f"- {heading}"
                )

            overview.append("")

        # -------------------------------------------------
        # Services
        # -------------------------------------------------

        if services:

            overview.append("## Services\n")

            overview.append(
                f"Detected {max(self._count_sections(services)-1,0)} service sections.\n"
            )

        # -------------------------------------------------
        # APIs
        # -------------------------------------------------

        if apis:

            overview.append("## APIs\n")

            overview.append(
                f"Detected {max(self._count_sections(apis)-1,0)} API groups.\n"
            )

        # -------------------------------------------------
        # Technologies
        # -------------------------------------------------

        if technologies:

            overview.append("## Technologies\n")

            overview.append(
                technologies[:800]
            )

            overview.append("")

        # -------------------------------------------------
        # Architecture Patterns
        # -------------------------------------------------

        if patterns:

            overview.append("## Architecture Patterns\n")

            overview.append(
                f"{max(self._count_sections(patterns)-1,0)} architecture patterns detected.\n"
            )

        # -------------------------------------------------
        # Dependency Graph
        # -------------------------------------------------

        if dependency_graph:

            overview.append("## Dependency Graph\n")

            overview.append(
                "Dependency graph generated successfully.\n"
            )

        # -------------------------------------------------
        # Hotspots
        # -------------------------------------------------

        if hotspots:

            overview.append("## Repository Hotspots\n")

            overview.append(
                f"{max(self._count_sections(hotspots)-1,0)} hotspot modules identified.\n"
            )

        # -------------------------------------------------
        # Recommendations
        # -------------------------------------------------

        if recommendations:

            overview.append("## Recommendations\n")

            overview.append(
                f"{max(self._count_sections(recommendations)-1,0)} recommendations generated.\n"
            )

        # -------------------------------------------------
        # Knowledge Documents
        # -------------------------------------------------

        overview.append("## Knowledge Documents\n")

        for document in stats["names"]:

            overview.append(
                f"- {document}"
            )

        overview.append("")

        overview.append(
            "End of Repository Overview."
        )

        return "\n".join(overview)

    # ---------------------------------------------------------
    # Save Overview
    # ---------------------------------------------------------

    def save(
        self,
        output_file: str = "repository_overview.md",
    ) -> str:
        """
        Generates and saves the repository overview.
        """

        overview = self.generate()

        output_path = (
            self.documents_directory /
            output_file
        )

        output_path.write_text(
            overview,
            encoding="utf-8",
        )

        return str(output_path)
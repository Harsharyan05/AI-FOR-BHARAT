"""
Document Generator

Generates AI-readable repository documents.

Author: Harsh Aryan
Project: Cognisys
"""

from pathlib import Path
from typing import Dict
from datetime import datetime


class DocumentGenerator:
    """
    Generates structured repository documentation.
    """

    def __init__(
        self,
        repository_path: str,
        output_directory: str = "storage/documents",
    ):
        self.repository_path = Path(repository_path)
        self.output_directory = Path(output_directory)

        self.output_directory.mkdir(
            parents=True,
            exist_ok=True,
        )

    def generate(
        self,
        analysis: Dict,
    ) -> Path:
        """
        Generate repository documentation.
        """

        repository_name = self.repository_path.resolve().name

        output_file = (
            self.output_directory /
            "repository_summary.md"
        )

        generated_on = datetime.now().strftime(
            "%d-%m-%Y %H:%M:%S"
        )

        with open(
            output_file,
            "w",
            encoding="utf-8",
        ) as file:

            # -------------------------------------------------
            # Title
            # -------------------------------------------------

            file.write("# Repository Summary\n\n")

            file.write(
                f"**Repository:** {repository_name}\n\n"
            )

            file.write(
                f"**Generated On:** {generated_on}\n\n"
            )

            # -------------------------------------------------
            # Table of Contents
            # -------------------------------------------------

            file.write("## Table of Contents\n\n")

            file.write("- Repository Statistics\n")
            file.write("- Repository Health\n")
            file.write("- Architecture Layers\n")
            file.write("- Repository Hotspots\n")
            file.write("- Architecture Patterns\n")
            file.write("- Circular Dependencies\n")
            file.write("- Recommendations\n\n")

            # -------------------------------------------------
            # Statistics
            # -------------------------------------------------

            file.write("## Repository Statistics\n\n")

            file.write(
                f"- Modules: {len(analysis['dependency_graph'])}\n"
            )

            file.write(
                f"- Architecture Layers: {len(analysis['layers'])}\n"
            )

            file.write(
                f"- Hotspots: {len(analysis['hotspots'])}\n"
            )

            file.write(
                f"- Patterns Detected: {len(analysis['patterns'])}\n"
            )

            file.write(
                f"- Circular Dependencies: {len(analysis['cycles'])}\n"
            )

            file.write(
                f"- Recommendations: {len(analysis['recommendations'])}\n\n"
            )

            # -------------------------------------------------
            # Repository Health
            # -------------------------------------------------

            file.write("## Repository Health\n\n")

            high_risk = sum(
                hotspot.risk == "HIGH"
                for hotspot in analysis["hotspots"]
            )

            if high_risk == 0:
                health = "GOOD"
            elif high_risk <= 3:
                health = "MODERATE"
            else:
                health = "POOR"

            file.write(f"- Overall Health: **{health}**\n")
            file.write(
                f"- High Risk Modules: {high_risk}\n"
            )
            file.write(
                f"- Circular Dependencies: {len(analysis['cycles'])}\n"
            )
            file.write(
                f"- Architecture Patterns: {len(analysis['patterns'])}\n\n"
            )

            # -------------------------------------------------
            # Layers
            # -------------------------------------------------

            file.write("## Architecture Layers\n\n")

            for layer, folders in analysis["layers"].items():

                file.write(f"### {layer}\n")

                for folder in folders:
                    file.write(f"- {folder}\n")

                file.write("\n")

            # -------------------------------------------------
            # Hotspots
            # -------------------------------------------------

            file.write("## Repository Hotspots\n\n")

            for risk in ["HIGH", "MEDIUM", "LOW"]:

                file.write(f"### {risk} Risk\n\n")

                found = False

                for hotspot in analysis["hotspots"]:

                    if hotspot.risk != risk:
                        continue

                    found = True

                    file.write(
                        f"- **{hotspot.module}** | "
                        f"Fan-In: {hotspot.fan_in} | "
                        f"Fan-Out: {hotspot.fan_out} | "
                        f"Score: {hotspot.score}\n"
                    )

                if not found:
                    file.write("None\n")

                file.write("\n")

            # -------------------------------------------------
            # Architecture Patterns
            # -------------------------------------------------

            file.write("## Architecture Patterns\n\n")

            for pattern in analysis["patterns"]:

                file.write(
                    f"### {pattern.name}\n"
                )

                file.write(
                    f"- Confidence: {pattern.confidence:.2f}\n"
                )

                file.write("- Evidence:\n")

                for evidence in pattern.evidence:

                    file.write(
                        f"  - {evidence}\n"
                    )

                file.write("\n")

            # -------------------------------------------------
            # Circular Dependencies
            # -------------------------------------------------

            file.write("## Circular Dependencies\n\n")

            if analysis["cycles"]:

                for cycle in analysis["cycles"]:

                    file.write(
                        "- "
                        + " → ".join(cycle)
                        + "\n"
                    )

            else:

                file.write(
                    "No circular dependencies detected.\n"
                )

            file.write("\n")

            # -------------------------------------------------
            # Recommendations
            # -------------------------------------------------

            file.write("## Recommendations\n\n")

            for recommendation in analysis[
                "recommendations"
            ]:

                file.write(
                    f"### {recommendation.title}\n"
                )

                file.write(
                    f"- Priority: {recommendation.priority}\n"
                )

                file.write(
                    f"- Module: {recommendation.module}\n"
                )

                file.write(
                    f"- Recommendation: {recommendation.recommendation}\n\n"
                )

        return output_file
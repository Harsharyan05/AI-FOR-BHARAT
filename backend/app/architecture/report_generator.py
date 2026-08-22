"""
Report Generator

Author: Harsh Aryan
Project: Cognisys
"""

import json
from pathlib import Path
from dataclasses import asdict

from app.architecture.hotspot_detector import Hotspot
from app.architecture.architecture_models import (
    ArchitecturePattern,
)
from app.architecture.recommendation_models import (
    Recommendation,
)


class ReportGenerator:
    """
    Generates architecture reports.
    """

    def __init__(
        self,
        output_directory: str = "reports",
    ):
        self.output_directory = Path(output_directory)
        self.output_directory.mkdir(
            exist_ok=True,
            parents=True,
        )

    def generate_json(
        self,
        hotspots,
        patterns,
        recommendations,
        cycles,
    ) -> Path:

        report = {
            "hotspots": [
                asdict(h)
                for h in hotspots
            ],
            "patterns": [
                asdict(p)
                for p in patterns
            ],
            "recommendations": [
                asdict(r)
                for r in recommendations
            ],
            "cycles": cycles,
        }

        output = self.output_directory / "architecture_report.json"

        with open(
            output,
            "w",
            encoding="utf-8",
        ) as file:

            json.dump(
                report,
                file,
                indent=4,
            )

        return output

    def generate_markdown(
        self,
        hotspots,
        patterns,
        recommendations,
        cycles,
    ) -> Path:

        output = self.output_directory / "architecture_report.md"

        with open(
            output,
            "w",
            encoding="utf-8",
        ) as file:

            file.write("# Cognisys Architecture Report\n\n")

            file.write("## Architecture Patterns\n\n")

            for pattern in patterns:

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

            file.write("## Hotspots\n\n")

            for hotspot in hotspots:

                file.write(
                    f"- **{hotspot.module}** "
                    f"(Score: {hotspot.score}, "
                    f"Risk: {hotspot.risk})\n"
                )

            file.write("\n")

            file.write("## Circular Dependencies\n\n")

            if cycles:

                for cycle in cycles:

                    file.write(
                        "- "
                        + " -> ".join(cycle)
                        + "\n"
                    )

            else:

                file.write(
                    "No circular dependencies detected.\n"
                )

            file.write("\n")

            file.write("## Recommendations\n\n")

            for recommendation in recommendations:

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
                    f"- Recommendation: "
                    f"{recommendation.recommendation}\n\n"
                )

        return output
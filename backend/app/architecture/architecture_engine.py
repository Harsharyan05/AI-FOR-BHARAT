"""
Architecture Engine

Orchestrates the complete architecture analysis pipeline.

Author: Harsh Aryan
Project: Cognisys
"""

from pathlib import Path

from app.architecture.layer_detector import LayerDetector
from app.architecture.dependency_graph import DependencyGraph
from app.architecture.hotspot_detector import HotspotDetector
from app.architecture.circular_dependency_detector import (
    CircularDependencyDetector,
)
from app.architecture.architecture_pattern_detector import (
    ArchitecturePatternDetector,
)
from app.architecture.recommendation_engine import (
    RecommendationEngine,
)
from app.architecture.report_generator import (
    ReportGenerator,
)


class ArchitectureEngine:
    """
    Complete Software Architecture Analysis Engine.
    """

    def __init__(
        self,
        repository_path: str,
        output_directory: str = "reports",
    ):
        self.repository_path = Path(repository_path)
        self.output_directory = output_directory

    def analyze(self):
        """
        Run the complete architecture analysis.
        """

        print("\n[1/6] Detecting Layers...")
        layers = LayerDetector(
            str(self.repository_path)
        ).detect()

        print("[2/6] Building Dependency Graph...")
        dependency_graph = DependencyGraph(
            str(self.repository_path)
        ).build()

        print("[3/6] Detecting Circular Dependencies...")
        cycles = CircularDependencyDetector(
            dependency_graph
        ).detect()

        print("[4/6] Detecting Hotspots...")
        hotspots = HotspotDetector(
            dependency_graph
        ).detect()

        print("[5/6] Detecting Architecture Patterns...")
        patterns = ArchitecturePatternDetector(
            layers,
            dependency_graph,
        ).detect()

        print("[6/6] Generating Recommendations...")
        recommendations = RecommendationEngine(
            hotspots,
            cycles,
            patterns,
        ).generate()

        generator = ReportGenerator(
            self.output_directory
        )

        json_report = generator.generate_json(
            hotspots,
            patterns,
            recommendations,
            cycles,
        )

        markdown_report = generator.generate_markdown(
            hotspots,
            patterns,
            recommendations,
            cycles,
        )

        return {
            "layers": layers,
            "dependency_graph": dependency_graph,
            "cycles": cycles,
            "hotspots": hotspots,
            "patterns": patterns,
            "recommendations": recommendations,
            "json_report": json_report,
            "markdown_report": markdown_report,
        }
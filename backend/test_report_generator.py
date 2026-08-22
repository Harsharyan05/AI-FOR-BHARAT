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


def main():

    graph = DependencyGraph(".").build()

    layers = LayerDetector(".").detect()

    hotspots = HotspotDetector(
        graph
    ).detect()

    cycles = CircularDependencyDetector(
        graph
    ).detect()

    patterns = ArchitecturePatternDetector(
        layers,
        graph,
    ).detect()

    recommendations = RecommendationEngine(
        hotspots,
        cycles,
        patterns,
    ).generate()

    generator = ReportGenerator()

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

    print("\nReports Generated Successfully")
    print("=" * 70)
    print(f"JSON Report      : {json_report}")
    print(f"Markdown Report  : {markdown_report}")


if __name__ == "__main__":
    main()
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

    engine = RecommendationEngine(
        hotspots,
        cycles,
        patterns,
    )

    recommendations = engine.generate()

    print("\nArchitecture Recommendations")
    print("=" * 80)

    if not recommendations:
        print("No recommendations generated.")
        return

    for recommendation in recommendations:

        print(f"\nPriority       : {recommendation.priority}")
        print(f"Title          : {recommendation.title}")
        print(f"Module         : {recommendation.module}")
        print(
            f"Recommendation : "
            f"{recommendation.recommendation}"
        )


if __name__ == "__main__":
    main()
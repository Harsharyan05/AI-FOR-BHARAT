from app.architecture.layer_detector import LayerDetector
from app.architecture.dependency_graph import DependencyGraph

from app.architecture.architecture_pattern_detector import (
    ArchitecturePatternDetector,
)


def main():

    layers = LayerDetector(".").detect()

    graph = DependencyGraph(".").build()

    detector = ArchitecturePatternDetector(
        layers,
        graph,
    )

    patterns = detector.detect()

    print("\nDetected Architecture Patterns")
    print("=" * 70)

    if not patterns:
        print("No patterns detected.")
        return

    for pattern in patterns:

        print(f"\nPattern     : {pattern.name}")
        print(f"Confidence : {pattern.confidence:.2f}")

        print("Evidence")

        for item in pattern.evidence:
            print(f"  • {item}")


if __name__ == "__main__":
    main()
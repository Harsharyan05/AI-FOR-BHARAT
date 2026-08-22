from app.architecture.dependency_graph import DependencyGraph
from app.architecture.hotspot_detector import HotspotDetector


def main():

    graph = DependencyGraph(".").build()

    detector = HotspotDetector(graph)

    hotspots = detector.detect()

    print("\nDetected Repository Hotspots")
    print("=" * 90)

    if not hotspots:
        print("No hotspots detected.")
        return

    print(
        f"{'Module':45}"
        f"{'Fan-In':>10}"
        f"{'Fan-Out':>10}"
        f"{'Score':>10}"
        f"{'Risk':>12}"
    )

    print("-" * 90)

    for hotspot in hotspots:

        print(
            f"{hotspot.module:45}"
            f"{hotspot.fan_in:>10}"
            f"{hotspot.fan_out:>10}"
            f"{hotspot.score:>10}"
            f"{hotspot.risk:>12}"
        )


if __name__ == "__main__":
    main()
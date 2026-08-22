from app.architecture.architecture_engine import (
    ArchitectureEngine,
)


def main():

    engine = ArchitectureEngine(".")

    result = engine.analyze()

    print("\n")
    print("=" * 80)
    print("COGNISYS ARCHITECTURE ANALYSIS")
    print("=" * 80)

    print(
        f"Layers Detected            : {len(result['layers'])}"
    )

    print(
        f"Dependency Graph Nodes     : {len(result['dependency_graph'])}"
    )

    print(
        f"Circular Dependencies      : {len(result['cycles'])}"
    )

    print(
        f"Hotspots                   : {len(result['hotspots'])}"
    )

    print(
        f"Architecture Patterns      : {len(result['patterns'])}"
    )

    print(
        f"Recommendations            : {len(result['recommendations'])}"
    )

    print("\nGenerated Reports")

    print(
        f"JSON       : {result['json_report']}"
    )

    print(
        f"Markdown   : {result['markdown_report']}"
    )


if __name__ == "__main__":
    main()
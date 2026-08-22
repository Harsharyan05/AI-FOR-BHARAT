from app.architecture.dependency_graph import DependencyGraph


def main():

    graph = DependencyGraph(".").build()

    print("\nDependency Graph")
    print("=" * 70)

    for module, dependencies in sorted(graph.items()):

        print(f"\n{module}")

        if not dependencies:
            print("  └── No dependencies")
            continue

        for dependency in dependencies:
            print(f"  └── {dependency}")


if __name__ == "__main__":
    main()
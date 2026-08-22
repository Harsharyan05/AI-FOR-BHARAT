from app.architecture.dependency_graph import DependencyGraph
from app.architecture.circular_dependency_detector import (
    CircularDependencyDetector,
)


graph = DependencyGraph(".").build()

detector = CircularDependencyDetector(graph)

cycles = detector.detect()

print("\nDetected Circular Dependencies")
print("=" * 60)

if not cycles:
    print("No circular dependencies found.")

for cycle in cycles:
    print(" -> ".join(cycle))
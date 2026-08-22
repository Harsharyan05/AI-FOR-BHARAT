"""
Circular Dependency Detector

Author: Harsh Aryan
Project: Cognisys
"""

from typing import Dict, List, Set


class CircularDependencyDetector:
    """
    Detects circular dependencies in a dependency graph
    using Depth First Search (DFS).
    """

    def __init__(self, graph: Dict[str, List[str]]):
        self.graph = graph
        self.visited: Set[str] = set()
        self.recursion_stack: Set[str] = set()
        self.path: List[str] = []
        self.cycles: List[List[str]] = []

    def detect(self) -> List[List[str]]:
        """
        Detect all circular dependencies.
        """

        for node in self.graph:

            if node not in self.visited:
                self._dfs(node)

        return self.cycles

    def _dfs(self, node: str):
        """
        DFS traversal.
        """

        self.visited.add(node)
        self.recursion_stack.add(node)
        self.path.append(node)

        for neighbour in self.graph.get(node, []):

            if neighbour not in self.graph:
                continue

            if neighbour not in self.visited:

                self._dfs(neighbour)

            elif neighbour in self.recursion_stack:

                self._record_cycle(neighbour)

        self.recursion_stack.remove(node)
        self.path.pop()

        # TODO:
        # Mark node visited
        # Add node to recursion stack
        # Add node to current path

        # Visit neighbours

        # Remove node from recursion stack
        # Remove node from current path

    def _record_cycle(self, start_node: str):
        """
        Extract and store a detected cycle.
        """

        index = self.path.index(start_node)

        cycle = self.path[index:] + [start_node]

        if cycle not in self.cycles:
            self.cycles.append(cycle)

        # TODO:
        # Find start_node in current path.
        # Slice the cycle.
        # Append start_node again.
        # Avoid duplicate cycles.
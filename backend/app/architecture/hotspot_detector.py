"""
Hotspot Detector

Detects highly coupled modules in a repository.

Author: Harsh Aryan
Project: Cognisys
"""

from dataclasses import dataclass
from typing import Dict, List


@dataclass
class Hotspot:
    """
    Represents a repository hotspot.
    """

    module: str
    fan_in: int
    fan_out: int
    score: int
    risk: str


class HotspotDetector:
    """
    Detect highly coupled modules using dependency graph.
    """

    def __init__(self, graph: Dict[str, List[str]]):
        self.graph = graph

    def detect(self) -> List[Hotspot]:
        """
        Detect hotspots in the dependency graph.
        """

        # Initialize Fan-In
        fan_in = {
            module: 0
            for module in self.graph
            if not module.endswith("__init__")
        }

        # Calculate Fan-In
        for module, dependencies in self.graph.items():

            if module.endswith("__init__"):
                continue

            for dependency in dependencies:

                if dependency.endswith("__init__"):
                    continue

                if dependency in fan_in:
                    fan_in[dependency] += 1

        hotspots: List[Hotspot] = []

        # Calculate Fan-Out, Score and Risk
        for module, dependencies in self.graph.items():

            if module.endswith("__init__"):
                continue

            filtered_dependencies = [
                dependency
                for dependency in dependencies
                if not dependency.endswith("__init__")
            ]

            fan_out = len(filtered_dependencies)

            score = fan_in[module] + fan_out

            risk = self._calculate_risk(score)

            hotspots.append(
                Hotspot(
                    module=module,
                    fan_in=fan_in[module],
                    fan_out=fan_out,
                    score=score,
                    risk=risk,
                )
            )

        hotspots.sort(
            key=lambda hotspot: hotspot.score,
            reverse=True,
        )

        return hotspots

    def _calculate_risk(self, score: int) -> str:
        """
        Calculate hotspot risk.
        """

        if score >= 10:
            return "HIGH"

        if score >= 5:
            return "MEDIUM"

        return "LOW"
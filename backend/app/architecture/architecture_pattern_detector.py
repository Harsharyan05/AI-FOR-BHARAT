"""
Architecture Pattern Detector

Detects software architecture patterns.

Author: Harsh Aryan
Project: Cognisys
"""

from typing import Dict, List

from app.architecture.architecture_models import (
    ArchitecturePattern,
)


class ArchitecturePatternDetector:
    """
    Detect software architecture patterns.
    """

    def __init__(
        self,
        layers: Dict[str, List[str]],
        dependency_graph: Dict[str, List[str]],
    ):
        self.layers = layers
        self.graph = dependency_graph

    def detect(self) -> List[ArchitecturePattern]:
        """
        Detect architecture patterns.
        """

        patterns = []

        layered = self._detect_layered()

        if layered:
            patterns.append(layered)

        mvc = self._detect_mvc()

        if mvc:
            patterns.append(mvc)

        monolith = self._detect_monolith()

        if monolith:
            patterns.append(monolith)

        return patterns

    def _detect_layered(self):

        required_layers = {
            "Presentation",
            "Business",
            "Persistence",
        }

        detected = set(self.layers.keys())

        if required_layers.issubset(detected):

            evidence = []

            for layer in sorted(required_layers):
                evidence.append(
                    f"{layer} layer detected"
                )

            return ArchitecturePattern(
                name="Layered Architecture",
                confidence=0.95,
                evidence=evidence,
            )

        return None

    def _detect_mvc(self):

        has_models = "Persistence" in self.layers
        has_controllers = "Presentation" in self.layers

        if has_models and has_controllers:

            return ArchitecturePattern(
                name="MVC",
                confidence=0.60,
                evidence=[
                    "Presentation layer detected",
                    "Persistence layer detected",
                ],
            )

        return None

    def _detect_monolith(self):

        module_count = len(self.graph)

        if module_count > 20:

            return ArchitecturePattern(
                name="Monolithic Architecture",
                confidence=0.85,
                evidence=[
                    f"{module_count} modules detected",
                    "Single deployable project",
                ],
            )

        return None
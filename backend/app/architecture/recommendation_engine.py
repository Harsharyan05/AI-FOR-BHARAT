"""
Recommendation Engine

Author: Harsh Aryan
Project: Cognisys
"""

from typing import List

from app.architecture.hotspot_detector import Hotspot
from app.architecture.architecture_models import (
    ArchitecturePattern,
)
from app.architecture.recommendation_models import (
    Recommendation,
)


class RecommendationEngine:
    """
    Generates architecture recommendations.
    """

    def __init__(
        self,
        hotspots: List[Hotspot],
        cycles: List[List[str]],
        patterns: List[ArchitecturePattern],
    ):
        self.hotspots = hotspots
        self.cycles = cycles
        self.patterns = patterns

    def generate(self) -> List[Recommendation]:

        recommendations = []

        recommendations.extend(
            self._hotspot_recommendations()
        )

        recommendations.extend(
            self._cycle_recommendations()
        )

        recommendations.extend(
            self._pattern_recommendations()
        )

        return recommendations

    def _hotspot_recommendations(
        self,
    ) -> List[Recommendation]:

        recommendations = []

        for hotspot in self.hotspots:

            if hotspot.risk == "HIGH":

                recommendations.append(

                    Recommendation(
                        priority="HIGH",
                        title="High Coupling Detected",
                        module=hotspot.module,
                        recommendation=(
                            "Split this module into smaller "
                            "services to reduce coupling."
                        ),
                    )

                )

            elif hotspot.risk == "MEDIUM":

                recommendations.append(

                    Recommendation(
                        priority="MEDIUM",
                        title="Medium Coupling",
                        module=hotspot.module,
                        recommendation=(
                            "Consider refactoring this "
                            "module if it continues to grow."
                        ),
                    )

                )

        return recommendations

    def _cycle_recommendations(
        self,
    ) -> List[Recommendation]:

        recommendations = []

        for cycle in self.cycles:

            recommendations.append(

                Recommendation(
                    priority="HIGH",
                    title="Circular Dependency",
                    module=cycle[0],
                    recommendation=(
                        "Break this circular dependency "
                        "using interfaces or dependency inversion."
                    ),
                )

            )

        return recommendations

    def _pattern_recommendations(
        self,
    ) -> List[Recommendation]:

        recommendations = []

        names = {
            pattern.name
            for pattern in self.patterns
        }

        if "Layered Architecture" in names:

            recommendations.append(

                Recommendation(
                    priority="LOW",
                    title="Architecture Pattern",
                    module="Repository",
                    recommendation=(
                        "Layered architecture detected. "
                        "Continue enforcing layer separation."
                    ),
                )

            )

        if "Monolithic Architecture" in names:

            recommendations.append(

                Recommendation(
                    priority="LOW",
                    title="Scalability",
                    module="Repository",
                    recommendation=(
                        "Consider modularization or "
                        "microservices as the project grows."
                    ),
                )

            )

        return recommendations
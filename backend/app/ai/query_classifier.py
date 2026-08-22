"""
Query Classifier

Classifies repository questions into categories to enable
adaptive retrieval and prompt generation.

Author: Harsh Aryan
Project: Cognisys
"""

from dataclasses import dataclass
from typing import List
import re


@dataclass
class QueryClassification:
    """
    Classification result.
    """

    category: str
    confidence: float
    top_k: int
    overview: bool
    keywords: List[str]


class QueryClassifier:
    """
    Rule-based query classifier.

    Determines:
    - Query category
    - Retrieval strategy
    - Number of chunks to retrieve
    """

    CATEGORY_KEYWORDS = {

        "OVERVIEW": [
            "overview",
            "summary",
            "describe",
            "backend",
            "repository",
            "project",
            "complete",
            "entire",
            "whole",
            "start to finish",
            "workflow",
            "flow",
        ],

        "ARCHITECTURE": [
            "architecture",
            "layer",
            "layers",
            "design",
            "structure",
            "component",
            "pattern",
            "mvc",
            "monolithic",
            "microservice",
        ],

        "API": [
            "api",
            "endpoint",
            "route",
            "rest",
            "http",
            "post",
            "get",
            "put",
            "delete",
        ],

        "IMPLEMENTATION": [
            "where",
            "implemented",
            "implementation",
            "code",
            "file",
            "function",
            "class",
            "method",
            "logic",
        ],

        "DEPENDENCY": [
            "dependency",
            "dependencies",
            "depend",
            "imports",
            "import",
            "fan-in",
            "fan-out",
            "coupling",
            "graph",
        ],

        "SECURITY": [
            "security",
            "secret",
            "vulnerability",
            "permission",
            "scan",
            "risk",
            "credential",
        ],

        "DATABASE": [
            "database",
            "postgres",
            "sql",
            "table",
            "schema",
            "model",
            "orm",
        ],

        "TECHNOLOGY": [
            "technology",
            "framework",
            "language",
            "library",
            "stack",
            "tools",
            "python",
            "react",
            "fastapi",
        ],

        "HOTSPOT": [
            "hotspot",
            "risk",
            "coupling",
            "refactor",
            "recommendation",
        ],

        "SERVICE": [
            "service",
            "services",
            "business",
            "repository service",
            "analysis service",
        ],
    }

    TOP_K = {
        "OVERVIEW": 20,
        "ARCHITECTURE": 15,
        "DEPENDENCY": 10,
        "API": 10,
        "IMPLEMENTATION": 8,
        "HOTSPOT": 8,
        "SERVICE": 8,
        "DATABASE": 8,
        "TECHNOLOGY": 8,
        "SECURITY": 8,
        "GENERAL": 5,
    }

    OVERVIEW_CATEGORIES = {
        "OVERVIEW",
        "ARCHITECTURE",
    }

    def classify(
        self,
        question: str,
    ) -> QueryClassification:
        """
        Classify a repository question.
        """

        normalized = question.lower()

        normalized = re.sub(
            r"[^\w\s-]",
            "",
            normalized,
        )

        scores = {}

        matched_keywords = {}

        for category, keywords in self.CATEGORY_KEYWORDS.items():

            count = 0
            found = []

            for keyword in keywords:

                if keyword in normalized:
                    count += 1
                    found.append(keyword)

            scores[category] = count
            matched_keywords[category] = found

        best_category = max(
            scores,
            key=scores.get,
        )

        if scores[best_category] == 0:

            return QueryClassification(
                category="GENERAL",
                confidence=0.40,
                top_k=self.TOP_K["GENERAL"],
                overview=False,
                keywords=[],
            )

        total = sum(scores.values())

        confidence = (
            scores[best_category]
            / max(total, 1)
        )

        return QueryClassification(
            category=best_category,
            confidence=round(confidence, 2),
            top_k=self.TOP_K[best_category],
            overview=(
                best_category
                in self.OVERVIEW_CATEGORIES
            ),
            keywords=matched_keywords[
                best_category
            ],
        )
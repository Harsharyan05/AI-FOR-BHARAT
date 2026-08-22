"""
Intelligent File Classifier

Author: Harsh Aryan
Project: Cognisys
"""

from pathlib import Path

from app.graph.graph_models import NodeType


class FileClassifier:
    """
    Classifies repository files based on
    filename and software conventions.
    """

    @staticmethod
    def classify(file_path: str) -> NodeType:

        path = Path(file_path)

        name = path.name.lower()

        suffix = path.suffix.lower()

        # -----------------------------
        # Documentation
        # -----------------------------

        if name in {
            "readme.md",
            "license",
            "changelog.md",
            "documentation.md",
            "design.md",
        }:
            return NodeType.DOCUMENTATION

        # -----------------------------
        # Configuration Files
        # -----------------------------

        if name in {
            ".env",
            ".gitignore",
            "requirements.txt",
            "pyproject.toml",
            "package.json",
            "docker-compose.yml",
            "docker-compose.yaml",
        }:
            return NodeType.CONFIG

        # -----------------------------
        # Docker
        # -----------------------------

        if name == "dockerfile":
            return NodeType.TECHNOLOGY

        # -----------------------------
        # Python Files
        # -----------------------------

        if suffix == ".py":

            if "service" in name:
                return NodeType.SERVICE

            if "model" in name:
                return NodeType.CLASS

            if "api" in name:
                return NodeType.API_ENDPOINT

            if "route" in name:
                return NodeType.API_ENDPOINT

            if "workflow" in name:
                return NodeType.WORKFLOW

            return NodeType.PYTHON_FILE

        return NodeType.CONFIG
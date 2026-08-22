"""
Knowledge Graph Entity Extractor

Author: Harsh Aryan
Project: Cognisys
"""

from pathlib import Path

from app.graph.graph_models import Node

from app.parser.file_classifier import FileClassifier

class EntityExtractor:
    """
    Extracts repository entities and converts them into graph nodes.
    """

    def extract(self, repository_path: str):

        root = Path(repository_path)

        nodes = []

        # -----------------------------
        # Repository Node
        # -----------------------------

        nodes.append(
            Node(
                id="repository",
                label=root.name,
                type="Repository",
            )
        )

        # -----------------------------
        # Traverse Repository
        # -----------------------------

        IGNORE_DIRECTORIES = {
        ".git",
        "__pycache__",
        "node_modules",
        ".next",
        "venv",
        ".venv",
        "dist",
        "build",
        ".idea",
        ".vscode",
    }

        for item in root.rglob("*"):

            if any(part in IGNORE_DIRECTORIES for part in item.parts):
                continue

            relative_path = str(item.relative_to(root))

            node_id = relative_path.replace("\\", "/")

            if item.is_dir():

                nodes.append(
                    Node(
                        id=node_id,
                        label=item.name,
                        type="Folder",
                    )
                )

            elif item.is_file():

                nodes.append(
                    Node(
                        id=node_id,
                        label=item.name,
                        type=FileClassifier.classify(str(item)),
                        properties={
                            "extension": item.suffix.lower(),
                            "size": item.stat().st_size,
                        },
                    )
                )

        return nodes
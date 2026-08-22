"""
Knowledge Graph Relationship Extractor

Author: Harsh Aryan
Project: Cognisys
"""

from pathlib import Path

from app.graph.graph_models import Edge


class RelationshipExtractor:
    """
    Extracts relationships between repository entities.
    """

    def extract(self, repository_path: str):

        root = Path(repository_path)

        edges = []

        # Repository contains top-level folders/files
        for item in root.iterdir():

            edges.append(
                Edge(
                    source="repository",
                    target=str(item.relative_to(root)).replace("\\", "/"),
                    relationship="contains",
                )
            )

        # Folder contains children
        for item in root.rglob("*"):

            if item.parent == root:
                continue

            parent = str(item.parent.relative_to(root)).replace("\\", "/")
            child = str(item.relative_to(root)).replace("\\", "/")

            edges.append(
                Edge(
                    source=parent,
                    target=child,
                    relationship="contains",
                )
            )

        return edges
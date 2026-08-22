"""
Import Graph Builder

Author: Harsh Aryan
Project: Cognisys
"""

from pathlib import Path
import ast


class ImportGraphBuilder:
    """
    Extracts import relationships
    between Python files.
    """

    def build(self, repository_path: str):

        root = Path(repository_path)

        relationships = []

        for file in root.rglob("*.py"):

            relative = str(file.relative_to(root)).replace("\\", "/")

            try:

                tree = ast.parse(
                    file.read_text(
                        encoding="utf-8",
                        errors="ignore"
                    )
                )

            except Exception:
                continue

            for node in ast.walk(tree):

                if isinstance(node, ast.Import):

                    for alias in node.names:

                        relationships.append({

                            "source": relative,

                            "target": alias.name,

                            "relationship": "imports"

                        })

                elif isinstance(node, ast.ImportFrom):

                    if node.module:

                        relationships.append({

                            "source": relative,

                            "target": node.module,

                            "relationship": "imports"

                        })

        return relationships
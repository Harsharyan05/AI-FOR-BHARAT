"""
Dependency Analyzer

Author: Harsh Aryan
Project: Cognisys
"""

from pathlib import Path
import ast


class DependencyAnalyzer:
    """
    Extracts Python import relationships from a repository.
    """

    def analyze(self, repository_path: str) -> dict:

        root = Path(repository_path)

        dependencies = {}

        python_files = list(root.rglob("*.py"))

        for file in python_files:

            relative_path = str(file.relative_to(root))

            imports = []

            try:

                tree = ast.parse(
                    file.read_text(
                        encoding="utf-8",
                        errors="ignore",
                    )
                )

                for node in ast.walk(tree):

                    if isinstance(node, ast.Import):

                        for alias in node.names:
                            imports.append(alias.name)

                    elif isinstance(node, ast.ImportFrom):

                        if node.module:
                            imports.append(node.module)

            except Exception:
                continue

            dependencies[relative_path] = sorted(
                list(set(imports))
            )

        return dependencies
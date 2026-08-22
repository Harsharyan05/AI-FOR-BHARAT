"""
Python AST Parser

Author: Harsh Aryan
Project: Cognisys
"""

from pathlib import Path
import ast


class PythonASTParser:
    """
    Parses Python source files using
    Python's built-in AST module.
    """

    def parse(self, repository_path: str):

        root = Path(repository_path)

        results = {}

        python_files = list(root.rglob("*.py"))

        for file in python_files:

            relative_path = str(file.relative_to(root))

            try:

                source = file.read_text(
                    encoding="utf-8",
                    errors="ignore",
                )

                tree = ast.parse(source)

            except Exception:
                continue

            imports = []
            classes = []
            functions = []

            for node in ast.walk(tree):

                # -------------------------
                # Imports
                # -------------------------

                if isinstance(node, ast.Import):

                    for alias in node.names:

                        imports.append(alias.name)

                elif isinstance(node, ast.ImportFrom):

                    if node.module:

                        imports.append(node.module)

                # -------------------------
                # Classes
                # -------------------------

                elif isinstance(node, ast.ClassDef):

                    classes.append(node.name)

                # -------------------------
                # Functions
                # -------------------------

                elif isinstance(node, ast.FunctionDef):

                    functions.append(node.name)

                elif isinstance(node, ast.AsyncFunctionDef):

                    functions.append(node.name)

            results[relative_path] = {

                "imports": sorted(set(imports)),

                "classes": sorted(set(classes)),

                "functions": sorted(set(functions)),
            }

        return results
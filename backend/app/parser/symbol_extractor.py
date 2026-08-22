"""
Symbol Extractor

Author: Harsh Aryan
Project: Cognisys
"""

from pathlib import Path
import ast


class SymbolExtractor:
    """
    Extracts classes and functions from Python files.
    """

    def extract(self, repository_path: str):

        root = Path(repository_path)

        symbols = {}

        for file in root.rglob("*.py"):

            relative_path = str(file.relative_to(root))

            try:

                source = file.read_text(
                    encoding="utf-8",
                    errors="ignore",
                )

                tree = ast.parse(source)

            except Exception:
                continue

            file_symbols = {

                "classes": [],

                "functions": [],
            }

            for node in ast.walk(tree):

                if isinstance(node, ast.ClassDef):

                    file_symbols["classes"].append({

                        "name": node.name,

                        "line": node.lineno,
                    })

                elif isinstance(node, ast.FunctionDef):

                    file_symbols["functions"].append({

                        "name": node.name,

                        "line": node.lineno,
                    })

                elif isinstance(node, ast.AsyncFunctionDef):

                    file_symbols["functions"].append({

                        "name": node.name,

                        "line": node.lineno,
                    })

            symbols[relative_path] = file_symbols

        return symbols
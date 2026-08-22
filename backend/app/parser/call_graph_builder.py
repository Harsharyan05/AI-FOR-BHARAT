"""
Call Graph Builder

Author: Harsh Aryan
Project: Cognisys
"""

from pathlib import Path
import ast


class CallGraphBuilder(ast.NodeVisitor):
    """
    Builds a function call graph for Python files.
    """

    def __init__(self):

        self.current_function = None

        self.calls = []

    def visit_FunctionDef(self, node):

        previous = self.current_function

        self.current_function = node.name

        self.generic_visit(node)

        self.current_function = previous

    def visit_AsyncFunctionDef(self, node):

        previous = self.current_function

        self.current_function = node.name

        self.generic_visit(node)

        self.current_function = previous

    def visit_Call(self, node):

        if self.current_function is not None:

            function_name = None

            if isinstance(node.func, ast.Name):

                function_name = node.func.id

            elif isinstance(node.func, ast.Attribute):

                function_name = node.func.attr

            if function_name:

                self.calls.append(
                    {
                        "caller": self.current_function,
                        "callee": function_name,
                    }
                )

        self.generic_visit(node)

    def build(self, repository_path: str):

        self.calls = []

        root = Path(repository_path)

        for file in root.rglob("*.py"):

            try:

                source = file.read_text(
                    encoding="utf-8",
                    errors="ignore",
                )

                tree = ast.parse(source)

                self.visit(tree)

            except Exception:

                continue

        return self.calls
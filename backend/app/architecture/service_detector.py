"""
Service Detector

Detects FastAPI services inside a repository.

Author: Harsh Aryan
Project: Cognisys
"""

from pathlib import Path
from typing import Dict, List
import ast


class ServiceDetector:
    """
    Detect FastAPI application components.
    """

    IGNORE_DIRS = {
        ".git",
        "__pycache__",
        ".venv",
        "venv",
        "node_modules",
        ".idea",
        ".vscode",
    }

    def __init__(self, repository_path: str):
        self.repository_path = Path(repository_path)

    def detect(self) -> List[Dict]:

        services = []

        for file in self.repository_path.rglob("*.py"):

            if any(part in self.IGNORE_DIRS for part in file.parts):
                continue

            try:
                tree = ast.parse(file.read_text(encoding="utf-8"))

                visitor = FastAPIVisitor(
                    file.relative_to(self.repository_path)
                )

                visitor.visit(tree)

                services.extend(visitor.services)

            except Exception:
                continue

        return services


class FastAPIVisitor(ast.NodeVisitor):

    def __init__(self, file_path: Path):
        self.file_path = str(file_path)
        self.services = []
        self.detected = set()
        
    def visit_Assign(self, node):

        if not isinstance(node.value, ast.Call):
            return self.generic_visit(node)

        func = node.value.func

        if isinstance(func, ast.Name):
            name = func.id

        elif isinstance(func, ast.Attribute):
            name = func.attr

        else:
            name = None

        if name == "FastAPI":

            service = ("FastAPI Application", self.file_path)

            if service not in self.detected:
                self.detected.add(service)

                self.services.append(
                    {
                        "type": "FastAPI Application",
                        "file": self.file_path,
                    }
                )

        elif name == "APIRouter":

            service = ("APIRouter", self.file_path)

            if service not in self.detected:
                self.detected.add(service)

                self.services.append(
                    {
                        "type": "APIRouter",
                        "file": self.file_path,
                    }
                )

        self.generic_visit(node)

    def visit_FunctionDef(self, node):

        for decorator in node.decorator_list:

            if not isinstance(decorator, ast.Call):
                continue

            func = decorator.func

            if not isinstance(func, ast.Attribute):
                continue

            method = func.attr.lower()

            if method in {
                "get",
                "post",
                "put",
                "delete",
                "patch",
                "options",
                "head",
            }:

                self.services.append(
                    {
                        "type": "API Endpoint",
                        "method": method.upper(),
                        "function": node.name,
                        "file": self.file_path,
                    }
                )

        self.generic_visit(node)
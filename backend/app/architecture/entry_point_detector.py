"""
Entry Point Detector

Detects application entry points inside a repository.

Author: Harsh Aryan
Project: Cognisys
"""

from pathlib import Path
from typing import Dict, List


class EntryPointDetector:
    """
    Detects application entry point files and identifies
    the framework used by inspecting their contents.
    """

    ENTRY_FILES = {
        "main.py",
        "app.py",
        "manage.py",
        "__main__.py",
        "server.py",
        "run.py",
        "wsgi.py",
        "asgi.py",
    }

    IGNORE_DIRS = {
        ".git",
        "__pycache__",
        "venv",
        ".venv",
        "node_modules",
        ".idea",
        ".vscode",
    }

    def __init__(self, repository_path: str):
        self.repository_path = Path(repository_path)

    def detect_framework(self, file_path: Path) -> str:
        """
        Detect the application framework by inspecting the file content.
        """

        try:
            content = file_path.read_text(
                encoding="utf-8",
                errors="ignore",
            )

            framework_patterns = {
                "FastAPI": [
                    "FastAPI(",
                    "from fastapi import",
                    "import fastapi",
                    "uvicorn.run",
                ],
                "Flask": [
                    "Flask(",
                    "from flask import",
                    "import flask",
                ],
                "Django": [
                    "django.core",
                    "DJANGO_SETTINGS_MODULE",
                    "execute_from_command_line",
                ],
            }

            for framework, patterns in framework_patterns.items():
                if any(pattern in content for pattern in patterns):
                    return framework

            return "Unknown"

        except Exception:
            return "Unknown"

    def detect(self) -> List[Dict]:
        """
        Scan the repository and return all detected entry points.
        """

        entry_points = []

        for file in self.repository_path.rglob("*"):

            if not file.is_file():
                continue

            if any(part in self.IGNORE_DIRS for part in file.parts):
                continue

            if file.name not in self.ENTRY_FILES:
                continue

            entry_points.append(
                {
                    "file": file.name,
                    "path": str(file.relative_to(self.repository_path)),
                    "framework": self.detect_framework(file),
                    "confidence": 1.0,
                }
            )

        return entry_points
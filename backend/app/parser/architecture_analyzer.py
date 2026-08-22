"""
Architecture Analyzer

Author: Harsh Aryan
Project: Cognisys
"""

from pathlib import Path


class ArchitectureAnalyzer:
    """
    Infers the high-level architecture of a repository.
    """

    def analyze(self, repository_path: str) -> dict:

        root = Path(repository_path)

        architecture = {
            "frontend": False,
            "backend": False,
            "database": False,
            "docker": False,
            "github_actions": False,
            "architecture_type": "Unknown",
            "components": [],
        }

        # ---------- Frontend ----------

        frontend_markers = {
            "package.json",
            "next.config.js",
            "next.config.ts",
            "vite.config.ts",
            "vite.config.js",
        }

        # ---------- Backend ----------

        backend_markers = {
            "requirements.txt",
            "pyproject.toml",
            "main.py",
        }

        for file in root.rglob("*"):

            if not file.is_file():
                continue

            name = file.name

            path = str(file)

            # Frontend

            if name in frontend_markers:
                architecture["frontend"] = True

            # Backend

            if name in backend_markers:
                architecture["backend"] = True

            # Docker

            if name == "Dockerfile":
                architecture["docker"] = True

            # GitHub Actions

            if ".github/workflows" in path.replace("\\", "/"):
                architecture["github_actions"] = True

            # Databases

            if "postgres" in path.lower():
                architecture["database"] = True

        # ---------------------------------
        # Infer Architecture
        # ---------------------------------

        if architecture["frontend"] and architecture["backend"]:
            architecture["architecture_type"] = "Full Stack"

        elif architecture["frontend"]:
            architecture["architecture_type"] = "Frontend"

        elif architecture["backend"]:
            architecture["architecture_type"] = "Backend"

        # Components

        if architecture["frontend"]:
            architecture["components"].append("Frontend")

        if architecture["backend"]:
            architecture["components"].append("Backend")

        if architecture["database"]:
            architecture["components"].append("Database")

        if architecture["docker"]:
            architecture["components"].append("Docker")

        if architecture["github_actions"]:
            architecture["components"].append("CI/CD")

        return architecture
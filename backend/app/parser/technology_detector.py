"""
Technology Detector

Author: Harsh Aryan
Project: Cognisys
"""

from pathlib import Path
import json


class TechnologyDetector:
    """
    Detects technologies used in a repository.
    """

    def detect(self, repository_path: str) -> dict:

        root = Path(repository_path)

        technologies = {
            "languages": set(),
            "frameworks": set(),
            "databases": set(),
            "deployment": set(),
            "ml_libraries": set(),
        }

        # -------------------------
        # requirements.txt
        # -------------------------

        requirements = root / "requirements.txt"

        if requirements.exists():

            technologies["languages"].add("Python")

            packages = requirements.read_text(
                encoding="utf-8",
                errors="ignore"
            ).lower()

            if "fastapi" in packages:
                technologies["frameworks"].add("FastAPI")

            if "sqlalchemy" in packages:
                technologies["databases"].add("SQLAlchemy")

            if "psycopg" in packages:
                technologies["databases"].add("PostgreSQL")

            if "langchain" in packages:
                technologies["ml_libraries"].add("LangChain")

            if "networkx" in packages:
                technologies["ml_libraries"].add("NetworkX")

        # -------------------------
        # package.json
        # -------------------------

        package = root / "package.json"

        if package.exists():

            technologies["languages"].update(
                ["JavaScript", "TypeScript"]
            )

            data = json.loads(
                package.read_text(
                    encoding="utf-8",
                    errors="ignore"
                )
            )

            dependencies = {}

            dependencies.update(
                data.get("dependencies", {})
            )

            dependencies.update(
                data.get("devDependencies", {})
            )

            if "react" in dependencies:
                technologies["frameworks"].add("React")

            if "next" in dependencies:
                technologies["frameworks"].add("Next.js")

            if "tailwindcss" in dependencies:
                technologies["frameworks"].add("TailwindCSS")

        # -------------------------
        # Docker
        # -------------------------

        if (root / "Dockerfile").exists():

            technologies["deployment"].add("Docker")

        return {
            key: sorted(list(value))
            for key, value in technologies.items()
        }
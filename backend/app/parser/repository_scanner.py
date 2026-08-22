"""
Repository Scanner

Author: Harsh Aryan
Project: Cognisys

Scans a cloned repository and extracts structural metadata
that will later be used for technology detection, dependency
analysis, architecture reconstruction, and AI reasoning.
"""

from pathlib import Path


class RepositoryScanner:
    """
    Repository Scanner

    Extracts:
    - File statistics
    - Directory statistics
    - File extensions
    - Configuration files
    - Docker files
    - Documentation
    - GitHub Actions workflows
    - Largest files
    - Empty directories
    """

    CONFIG_FILES = {
        "requirements.txt",
        "package.json",
        "pyproject.toml",
        ".env",
        ".env.example",
        ".gitignore",
        "tsconfig.json",
        "vite.config.ts",
        "vite.config.js",
        "next.config.js",
        "next.config.ts",
        "tailwind.config.js",
        "tailwind.config.ts",
    }

    DOCKER_FILES = {
        "Dockerfile",
        "docker-compose.yml",
        "docker-compose.yaml",
        ".dockerignore",
    }

    DOCUMENTATION_FILES = {
        "README.md",
        "LICENSE",
        "CONTRIBUTING.md",
        "CHANGELOG.md",
    }

    def scan(self, repository_path: str) -> dict:
        """
        Scan an entire repository and return metadata.
        """

        root = Path(repository_path)

        if not root.exists():
            raise FileNotFoundError(
                f"Repository not found: {repository_path}"
            )

        total_files = 0
        total_directories = 0

        extensions = {}

        docker_files = []
        configuration_files = []
        documentation_files = []
        github_workflows = []
        empty_directories = []
        largest_files = []

        for item in root.rglob("*"):

            # -------------------------------
            # Directories
            # -------------------------------

            if item.is_dir():

                total_directories += 1

                if not any(item.iterdir()):
                    empty_directories.append(
                        str(item.relative_to(root))
                    )

                continue

            # -------------------------------
            # Files
            # -------------------------------

            total_files += 1

            extension = item.suffix.lower()

            if extension == "":
                extension = "no_extension"

            extensions[extension] = (
                extensions.get(extension, 0) + 1
            )

            relative_path = str(item.relative_to(root))

            # -------------------------------
            # Docker Files
            # -------------------------------

            if item.name in self.DOCKER_FILES:
                docker_files.append(relative_path)

            # -------------------------------
            # Configuration Files
            # -------------------------------

            if item.name in self.CONFIG_FILES:
                configuration_files.append(relative_path)

            # -------------------------------
            # Documentation
            # -------------------------------

            if item.name in self.DOCUMENTATION_FILES:
                documentation_files.append(relative_path)

            # -------------------------------
            # GitHub Workflows
            # -------------------------------

            if ".github/workflows" in relative_path.replace("\\", "/"):
                github_workflows.append(relative_path)

            # -------------------------------
            # Largest Files
            # -------------------------------

            largest_files.append(
                {
                    "path": relative_path,
                    "size_bytes": item.stat().st_size,
                }
            )

        # Sort largest files

        largest_files.sort(
            key=lambda file: file["size_bytes"],
            reverse=True,
        )

        largest_files = largest_files[:10]

        return {
            "repository_name": root.name,
            "total_files": total_files,
            "total_directories": total_directories,
            "extensions": extensions,
            "docker_files": docker_files,
            "configuration_files": configuration_files,
            "documentation_files": documentation_files,
            "github_workflows": github_workflows,
            "largest_files": largest_files,
            "empty_directories": empty_directories,
        }
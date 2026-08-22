"""
Layer Detector

Detects architectural layers inside a repository.

Author: Harsh Aryan
Project: Cognisys
"""

from pathlib import Path
from typing import Dict, List


class LayerDetector:
    """
    Detect architectural layers based on directory names.
    """

    LAYER_MAPPING = {
        "Presentation": {"api"},
        "Business": {"services", "workflows"},
        "Knowledge": {"graph", "ai"},
        "Analysis": {"parser"},
        "Persistence": {"database", "models", "schemas"},
        "Infrastructure": {"core","security","architecture",},
    }    
        
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

    def detect(self) -> Dict[str, List[str]]:
        """
        Detect repository layers.
        """

        layers = {}

        for directory in self.repository_path.rglob("*"):

            if not directory.is_dir():
                continue

            if any(part in self.IGNORE_DIRS for part in directory.parts):
                continue

            folder = directory.name.lower()

            for layer, names in self.LAYER_MAPPING.items():

                if folder in names:

                    layers.setdefault(layer, []).append(
                        str(directory.relative_to(self.repository_path))
                    )

        return layers
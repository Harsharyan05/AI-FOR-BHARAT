"""
Repository Metadata Models

Author: Harsh Aryan
Project: Cognisys
"""

from dataclasses import dataclass, field


@dataclass
class LargestFile:
    path: str
    size_bytes: int


@dataclass
class RepositoryMetadata:

    repository_name: str

    total_files: int = 0

    total_directories: int = 0

    extensions: dict = field(default_factory=dict)

    special_files: list = field(default_factory=list)

    github_workflows: list = field(default_factory=list)

    docker_files: list = field(default_factory=list)

    configuration_files: list = field(default_factory=list)

    documentation_files: list = field(default_factory=list)

    largest_files: list = field(default_factory=list)

    empty_directories: list = field(default_factory=list)
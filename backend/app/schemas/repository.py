"""
Repository request and response schemas.

Author: Harsh Aryan
Project: Cognisys
"""

from pydantic import BaseModel, HttpUrl


class RepositoryCloneRequest(BaseModel):
    """Request model for cloning a GitHub repository."""

    repository_url: HttpUrl

from typing import Dict, List


class RepositoryScanResponse(BaseModel):
    """
    Response model for repository scanning.
    """

    repository_name: str
    total_files: int
    total_directories: int
    extensions: Dict[str, int]
    special_files: List[str]

class RepositoryCloneResponse(BaseModel):
    """Response model after cloning a GitHub repository."""

    status: str
    repository_name: str
    local_path: str
"""
Analysis Schemas

Author: Harsh Aryan
Project: Cognisys
"""

from typing import Any

from pydantic import BaseModel, HttpUrl


class AnalysisRequest(BaseModel):
    """
    Request model for repository analysis.
    """

    repository_url: HttpUrl


class AnalysisResponse(BaseModel):
    """
    Response model for repository analysis.
    """

    status: str
    repository: Any
    technology: Any
    dependencies: Any
    architecture: Any
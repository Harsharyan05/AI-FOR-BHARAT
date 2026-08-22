"""
Repository API endpoints.

Author: Harsh Aryan
Project: Cognisys
"""

from fastapi import APIRouter, HTTPException

from app.schemas.repository import (
    RepositoryCloneRequest,
    RepositoryCloneResponse,
)
from app.services.repository_service import RepositoryService

router = APIRouter(
    prefix="/repositories",
    tags=["Repositories"],
)


@router.post(
    "/clone",
    response_model=RepositoryCloneResponse,
)
def clone_repository(request: RepositoryCloneRequest):
    """
    Clone a GitHub repository.
    """
    try:
        return RepositoryService.clone_repository(
            str(request.repository_url)
        )

    except ValueError as error:
        raise HTTPException(
            status_code=400,
            detail=str(error),
        )
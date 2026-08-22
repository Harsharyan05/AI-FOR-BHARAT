"""
Repository cloning engine.

Author: Harsh Aryan
Project: Cognisys
"""

from pathlib import Path

from git import Repo, GitCommandError

from app.core.constants import TEMP_DIR
from app.core.logger import logger


class RepositoryCloner:
    """
    Handles cloning GitHub repositories.
    """

    @staticmethod
    def clone(repository_url: str) -> tuple[str, str]:
        """
        Clone a GitHub repository if it does not already exist.

        Args:
            repository_url: Public GitHub repository URL.

        Returns:
            Tuple containing:
                Repository name
                Local repository path

        Raises:
            ValueError
        """

        repository_name = Path(repository_url).stem

        destination = TEMP_DIR / repository_name

        destination.parent.mkdir(
            parents=True,
            exist_ok=True,
        )

        # --------------------------------------------------
        # Repository already exists
        # --------------------------------------------------

        if destination.exists():

            logger.info(
                "Repository '%s' already exists. Using cached copy.",
                repository_name,
            )

            return (
                repository_name,
                str(destination),
            )

        # --------------------------------------------------
        # Clone Repository
        # --------------------------------------------------

        logger.info(
            "Cloning repository: %s",
            repository_url,
        )

        try:

            Repo.clone_from(
                repository_url,
                destination,
            )

            logger.info(
                "Repository cloned successfully."
            )

            return (
                repository_name,
                str(destination),
            )

        except GitCommandError as error:

            logger.exception(
                "Repository cloning failed."
            )

            raise ValueError(
                "Failed to clone repository."
            ) from error
"""
Database engine configuration.

Author: Harsh Aryan
Project: Cognisys
"""

from sqlalchemy import create_engine

from app.core.config import settings


engine = create_engine(
    settings.DATABASE_URL,
    echo=settings.DEBUG,
)
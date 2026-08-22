"""
Application constants.

Author: Harsh Aryan
Project: Cognisys
"""

from pathlib import Path


BASE_DIR = Path(__file__).resolve().parents[2]

STORAGE_DIR = BASE_DIR / "storage"

TEMP_DIR = STORAGE_DIR / "temp"

ANALYSIS_DIR = STORAGE_DIR / "analysis"

GRAPH_DIR = STORAGE_DIR / "graphs"

REPORT_DIR = STORAGE_DIR / "reports"

API_PREFIX = "/api/v1"

DOCUMENTS_DIR = STORAGE_DIR / "documents"

VECTOR_DB_DIR = STORAGE_DIR / "vector_db"

EMBEDDINGS_DIR = STORAGE_DIR / "embeddings"

LOG_DIR = BASE_DIR / "logs"

DEFAULT_TOP_K = 10

DEFAULT_MAX_HISTORY = 10

DEFAULT_MAX_CHUNK_LENGTH = 1500

DEFAULT_PORT = 8000
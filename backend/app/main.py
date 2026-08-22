"""
Main FastAPI Application

Author: Harsh Aryan
Project: Cognisys
"""

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.api.router import api_router
from app.core.config import settings
from app.core.logger import logger

app = FastAPI(
    title="Cognisys",
    description="AI System Behaviour & Automation Intelligence Engine",
    version=settings.API_VERSION,
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.on_event("startup")
async def startup():
    logger.info("Starting Cognisys Backend...")


@app.get("/", tags=["Root"])
def root():
    return {
        "project": "Cognisys",
        "version": settings.API_VERSION,
    }


@app.get("/api/v1/health", tags=["Health"])
def health():
    return {
        "status": "healthy",
        "project": settings.PROJECT_NAME,
        "version": settings.API_VERSION,
    }


app.include_router(
    api_router,
    prefix="/api/v1",
)
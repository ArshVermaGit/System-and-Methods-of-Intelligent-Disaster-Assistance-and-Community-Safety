"""Health check and status route handlers."""

from fastapi import APIRouter, Depends

from backend.app.core.config import Settings, get_settings
from backend.app.schemas.health import (
    ApiHealthResponse,
    LegacyHealthResponse,
    LegacyRootResponse,
)

router = APIRouter(tags=["Health & Status"])


@router.get(
    "/",
    response_model=LegacyRootResponse,
    summary="Root API Info",
)
def get_root():
    """Return legacy root information."""
    return {
        "project": "System and Methods of Intelligent Disaster Assistance and Community Safety",
        "phase": "EPICS Phase I",
        "status": "operational",
        "docs": "/docs",
    }


@router.get(
    "/health",
    response_model=LegacyHealthResponse,
    summary="Legacy Health Check",
)
def get_legacy_health(settings: Settings = Depends(get_settings)):
    """Return legacy /health endpoint status."""
    return {
        "status": "healthy",
        "service": "backend",
        "environment": settings.ENVIRONMENT,
    }


@router.get(
    "/api/health",
    response_model=ApiHealthResponse,
    summary="CONTRACTS.md /api/health",
)
def get_api_health(settings: Settings = Depends(get_settings)):
    """Return CONTRACTS.md Section 3 health status.

    Must include {'status':'running', 'application':'NIRVYX'}.
    Works independently of database or model availability.
    """
    return {
        "status": "running",
        "application": "NIRVYX",
        "version": settings.VERSION,
        "environment": settings.ENVIRONMENT,
    }

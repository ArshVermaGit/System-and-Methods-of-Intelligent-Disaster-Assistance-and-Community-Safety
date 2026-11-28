"""Health and status schemas."""

from pydantic import BaseModel, Field


class LegacyRootResponse(BaseModel):
    """Response model for root index endpoint."""

    project: str = Field(..., description="Project name")
    phase: str = Field(..., description="Project phase")
    status: str = Field(..., description="Operational status")
    docs: str = Field(..., description="API documentation endpoint")


class LegacyHealthResponse(BaseModel):
    """Response model for legacy /health endpoint."""

    status: str = Field(..., description="Service status")
    service: str = Field(..., description="Component identifier")
    environment: str = Field(..., description="Active environment name")


class ApiHealthResponse(BaseModel):
    """Response model for CONTRACTS.md Section 3 /api/health endpoint."""

    status: str = Field("running", description="API running status")
    application: str = Field("NIRVYX", description="Application name")
    version: str = Field("1.0.0", description="Application version")
    environment: str = Field("development", description="Runtime environment")

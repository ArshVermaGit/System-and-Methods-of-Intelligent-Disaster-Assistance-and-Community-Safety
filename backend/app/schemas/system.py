"""System info and diagnostic schemas conforming to CONTRACTS.md Section 3."""

from typing import Dict

from pydantic import BaseModel, Field


class DatabaseInfo(BaseModel):
    """Database connectivity and state."""

    status: str = Field(..., description="Database connection status: ready or not_configured")
    message: str = Field(..., description="Current status message")


class ModelInfo(BaseModel):
    """Model status and availability."""

    status: str = Field(..., description="Model status: ready, mock, or unavailable")
    reason: str = Field(..., description="Reason for current status")


class LimitsInfo(BaseModel):
    """Application limits."""

    max_upload_mb: int = Field(..., description="Maximum allowed file upload size in megabytes")
    max_pixels: int = Field(..., description="Maximum total pixel count per raster image")


class InputSpec(BaseModel):
    """Input format and channel specifications."""

    format: str = Field(..., description="Supported file formats")
    channels: int = Field(..., description="Expected channel/band count")
    description: str = Field(..., description="Channel composition details")


class SystemInfoResponse(BaseModel):
    """System information payload."""

    application: str = Field("NIRVYX", description="Application identifier")
    version: str = Field("1.0.0", description="Application semantic version")
    environment: str = Field(..., description="Runtime environment")
    database: DatabaseInfo
    models: Dict[str, ModelInfo]
    limits: LimitsInfo
    input_specs: Dict[str, InputSpec]
    disclaimer: str = Field(
        ...,
        description="Legal and operational disclaimer",
    )

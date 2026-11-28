"""Error response schemas conforming to CONTRACTS.md Section 3."""

from typing import Any, Dict

from pydantic import BaseModel, Field


class ErrorDetail(BaseModel):
    """Detailed error object."""

    code: str = Field(..., description="Machine-readable error code")
    message: str = Field(..., description="Human-readable error description")
    details: Dict[str, Any] = Field(
        default_factory=dict,
        description="Optional structured validation details or metadata",
    )


class ErrorResponse(BaseModel):
    """Standard top-level error response envelope."""

    error: ErrorDetail

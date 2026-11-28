"""Custom application error hierarchy and FastAPI exception handlers."""

import logging
from typing import Any, Dict, Optional

from fastapi import FastAPI, Request, status
from fastapi.exceptions import RequestValidationError
from fastapi.responses import JSONResponse
from starlette.exceptions import HTTPException as StarletteHTTPException

logger = logging.getLogger("nirvyx.errors")


class AppError(Exception):
    """Base exception for all application errors."""

    def __init__(
        self,
        code: str,
        message: str,
        status_code: int = status.HTTP_500_INTERNAL_SERVER_ERROR,
        details: Optional[Dict[str, Any]] = None,
    ):
        super().__init__(message)
        self.code = code
        self.message = message
        self.status_code = status_code
        self.details = details or {}


# 422 Errors
class ValidationError(AppError):
    def __init__(self, message: str, details: Optional[Dict[str, Any]] = None):
        super().__init__(
            code="VALIDATION_ERROR",
            message=message,
            status_code=422,
            details=details,
        )


class InvalidInputError(AppError):
    def __init__(self, message: str, details: Optional[Dict[str, Any]] = None):
        super().__init__(
            code="INVALID_INPUT",
            message=message,
            status_code=422,
            details=details,
        )


class InvalidChannelCountError(AppError):
    def __init__(self, message: str, details: Optional[Dict[str, Any]] = None):
        super().__init__(
            code="INVALID_CHANNEL_COUNT",
            message=message,
            status_code=422,
            details=details,
        )


class InvalidGeometryError(AppError):
    def __init__(self, message: str, details: Optional[Dict[str, Any]] = None):
        super().__init__(
            code="INVALID_GEOMETRY",
            message=message,
            status_code=422,
            details=details,
        )


# 415 Error
class UnsupportedFormatError(AppError):
    def __init__(self, message: str, details: Optional[Dict[str, Any]] = None):
        super().__init__(
            code="UNSUPPORTED_FORMAT",
            message=message,
            status_code=status.HTTP_415_UNSUPPORTED_MEDIA_TYPE,
            details=details,
        )


# 413 Error
class FileTooLargeError(AppError):
    def __init__(self, message: str, details: Optional[Dict[str, Any]] = None):
        super().__init__(
            code="FILE_TOO_LARGE",
            message=message,
            status_code=413,
            details=details,
        )


# 404 Error
class NotFoundError(AppError):
    def __init__(self, message: str, details: Optional[Dict[str, Any]] = None):
        super().__init__(
            code="NOT_FOUND",
            message=message,
            status_code=status.HTTP_404_NOT_FOUND,
            details=details,
        )


# 409 Errors
class NotGeoreferencedError(AppError):
    def __init__(self, message: str, details: Optional[Dict[str, Any]] = None):
        super().__init__(
            code="NOT_GEOREFERENCED",
            message=message,
            status_code=status.HTTP_409_CONFLICT,
            details=details,
        )


class AssessmentNotCompletedError(AppError):
    def __init__(self, message: str, details: Optional[Dict[str, Any]] = None):
        super().__init__(
            code="ASSESSMENT_NOT_COMPLETED",
            message=message,
            status_code=status.HTTP_409_CONFLICT,
            details=details,
        )


# 503 Errors
class ModelUnavailableError(AppError):
    def __init__(self, message: str, details: Optional[Dict[str, Any]] = None):
        super().__init__(
            code="MODEL_UNAVAILABLE",
            message=message,
            status_code=status.HTTP_503_SERVICE_UNAVAILABLE,
            details=details,
        )


class DatabaseUnavailableError(AppError):
    def __init__(self, message: str, details: Optional[Dict[str, Any]] = None):
        super().__init__(
            code="DATABASE_UNAVAILABLE",
            message=message,
            status_code=status.HTTP_503_SERVICE_UNAVAILABLE,
            details=details,
        )


# 500 Errors
class InferenceFailedError(AppError):
    def __init__(self, message: str, details: Optional[Dict[str, Any]] = None):
        super().__init__(
            code="INFERENCE_FAILED",
            message=message,
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            details=details,
        )


class InternalError(AppError):
    def __init__(self, message: str, details: Optional[Dict[str, Any]] = None):
        super().__init__(
            code="INTERNAL_ERROR",
            message=message,
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            details=details,
        )


def _format_error_response(
    code: str, message: str, details: Optional[Dict[str, Any]] = None
) -> dict:
    return {
        "error": {
            "code": code,
            "message": message,
            "details": details or {},
        }
    }


async def app_error_handler(request: Request, exc: AppError) -> JSONResponse:
    """Handle custom application errors."""
    logger.warning("Application error [%s]: %s (details: %s)", exc.code, exc.message, exc.details)
    return JSONResponse(
        status_code=exc.status_code,
        content=_format_error_response(exc.code, exc.message, exc.details),
    )


async def validation_error_handler(request: Request, exc: RequestValidationError) -> JSONResponse:
    """Handle request schema validation errors (422)."""
    logger.info("Validation error on %s: %s", request.url.path, exc.errors())
    formatted_errors = []
    for err in exc.errors():
        loc = " -> ".join(str(item) for item in err.get("loc", []))
        formatted_errors.append({"field": loc, "issue": err.get("msg")})

    return JSONResponse(
        status_code=422,
        content=_format_error_response(
            code="VALIDATION_ERROR",
            message="Request validation failed. Verify input types and required fields.",
            details={"validation_errors": formatted_errors},
        ),
    )


async def http_exception_handler(request: Request, exc: StarletteHTTPException) -> JSONResponse:
    """Handle standard HTTP exceptions (e.g. 404, 405)."""
    code_map = {
        status.HTTP_404_NOT_FOUND: ("NOT_FOUND", "The requested resource was not found."),
        status.HTTP_405_METHOD_NOT_ALLOWED: (
            "METHOD_NOT_ALLOWED",
            "HTTP method not allowed for this endpoint.",
        ),
        413: (
            "FILE_TOO_LARGE",
            "Request entity is too large.",
        ),
        status.HTTP_415_UNSUPPORTED_MEDIA_TYPE: (
            "UNSUPPORTED_FORMAT",
            "Unsupported media type format.",
        ),
    }

    code, default_msg = code_map.get(
        exc.status_code, ("HTTP_ERROR", str(exc.detail) if exc.detail else "HTTP error")
    )
    message = (
        str(exc.detail)
        if exc.detail and exc.status_code != status.HTTP_404_NOT_FOUND
        else default_msg
    )

    logger.info("HTTP %s on %s: %s", exc.status_code, request.url.path, message)
    return JSONResponse(
        status_code=exc.status_code,
        content=_format_error_response(code=code, message=message),
    )


async def unexpected_exception_handler(request: Request, exc: Exception) -> JSONResponse:
    """Handle unhandled server exceptions (500) and log tracebacks server-side only."""
    logger.exception("Unhandled server exception on %s: %s", request.url.path, str(exc))
    return JSONResponse(
        status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
        content=_format_error_response(
            code="INTERNAL_ERROR",
            message="An unexpected internal server error occurred.",
        ),
    )


def register_error_handlers(app: FastAPI) -> None:
    """Register all exception handlers on the FastAPI application."""
    app.add_exception_handler(AppError, app_error_handler)
    app.add_exception_handler(RequestValidationError, validation_error_handler)
    app.add_exception_handler(StarletteHTTPException, http_exception_handler)
    app.add_exception_handler(Exception, unexpected_exception_handler)

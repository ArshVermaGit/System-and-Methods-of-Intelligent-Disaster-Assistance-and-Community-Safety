"""Compatibility shim exposing FastAPI app from backend.app.main."""

from backend.app.main import app

__all__ = ["app"]

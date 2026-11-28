"""FastAPI application factory and instance for NIRVYX."""

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from backend.app.core.config import get_settings
from backend.app.core.errors import register_error_handlers
from backend.app.core.logging import setup_logging
from backend.app.routes import health, system


def create_app() -> FastAPI:
    """Instantiate and configure the NIRVYX FastAPI application."""
    settings = get_settings()
    setup_logging(settings.LOG_LEVEL)

    app = FastAPI(
        title="NIRVYX API",
        description="Flood and landslide assessment system",
        version="1.0.0",
        docs_url="/docs",
        redoc_url="/redoc",
    )

    # Register standard application exception handlers
    register_error_handlers(app)

    # Configure CORS strictly from settings (allow_credentials=False, never '*' by default)
    app.add_middleware(
        CORSMiddleware,
        allow_origins=settings.ALLOWED_ORIGINS,
        allow_credentials=False,
        allow_methods=["*"],
        allow_headers=["*"],
    )

    # Mount API routers
    app.include_router(health.router)
    app.include_router(system.router)

    return app


app = create_app()

"""System diagnostic and information route handlers."""

from fastapi import APIRouter, Depends

from backend.app.core.config import Settings, get_settings
from backend.app.schemas.system import SystemInfoResponse

router = APIRouter(tags=["System Info"])


@router.get(
    "/api/system/info",
    response_model=SystemInfoResponse,
    summary="System and Component Info",
)
def get_system_info(settings: Settings = Depends(get_settings)):
    """Return diagnostic system info, model availability, database status, and limits."""
    # Database is not yet connected in Step 2
    database_status = {
        "status": "not_configured",
        "message": "Database connection and PostGIS tables not initialized (scheduled for Step 4)",
    }

    # Models are not loaded in Step 2
    models_status = {
        "flood": {
            "status": "unavailable",
            "reason": ("Flood segmentation predictor module not yet loaded (scheduled for Step 5)"),
        },
        "landslide": {
            "status": "unavailable",
            "reason": (
                "Landslide segmentation predictor module not yet loaded (scheduled for Step 5)"
            ),
        },
    }

    limits = {
        "max_upload_mb": settings.MAX_UPLOAD_MB,
        "max_pixels": settings.MAX_PIXELS,
    }

    input_specs = {
        "flood": {
            "format": "GeoTIFF (.tif/.tiff)",
            "channels": 2,
            "description": "Band 1: VV polarization, Band 2: VH polarization (dB backscatter)",
        },
        "landslide": {
            "format": "GeoTIFF (.tif/.tiff) or HDF5 (.h5)",
            "channels": 14,
            "description": "B1–B12 Sentinel-2 MSI bands, B13 slope, B14 DEM",
        },
    }

    disclaimer = (
        "NIRVYX supports preparedness and decision-making; "
        "it does not forecast future events and does not replace official warning authorities. "
        "Geographical overlap indicates potential exposure only."
    )

    return {
        "application": settings.APPLICATION_NAME,
        "version": settings.VERSION,
        "environment": settings.ENVIRONMENT,
        "database": database_status,
        "models": models_status,
        "limits": limits,
        "input_specs": input_specs,
        "disclaimer": disclaimer,
    }

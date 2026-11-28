"""Comprehensive tests for NIRVYX backend API endpoints, error shapes, and CORS."""

from fastapi import APIRouter
from fastapi.testclient import TestClient
from pydantic import BaseModel

from backend.app.main import app, create_app

client = TestClient(app)


def test_app_starts_cleanly():
    """Verify fresh app creation without environment variables or dependencies."""
    new_app = create_app()
    assert new_app.title == "NIRVYX API"
    assert new_app.version == "1.0.0"


def test_root_endpoint():
    """Verify GET / root endpoint."""
    response = client.get("/")
    assert response.status_code == 200
    data = response.json()
    assert (
        data["project"]
        == "System and Methods of Intelligent Disaster Assistance and Community Safety"
    )
    assert data["phase"] == "EPICS Phase I"
    assert data["status"] == "operational"
    assert data["docs"] == "/docs"


def test_legacy_health_endpoint():
    """Verify GET /health legacy endpoint."""
    response = client.get("/health")
    assert response.status_code == 200
    data = response.json()
    assert data["status"] == "healthy"
    assert data["service"] == "backend"
    assert "environment" in data


def test_api_health_endpoint():
    """Verify GET /api/health per CONTRACTS.md Section 3."""
    response = client.get("/api/health")
    assert response.status_code == 200
    data = response.json()
    # CONTRACTS.md requirement: exactly includes status=running and application=NIRVYX
    assert data["status"] == "running"
    assert data["application"] == "NIRVYX"
    assert data["version"] == "1.0.0"


def test_system_info_endpoint():
    """Verify GET /api/system/info diagnostic payload."""
    response = client.get("/api/system/info")
    assert response.status_code == 200
    data = response.json()

    assert data["application"] == "NIRVYX"
    assert data["version"] == "1.0.0"

    # Database status should be not_configured in Step 2
    assert data["database"]["status"] == "not_configured"

    # Models must report unavailable in Step 2 with explicit reasons
    assert data["models"]["flood"]["status"] == "unavailable"
    assert "reason" in data["models"]["flood"]
    assert data["models"]["landslide"]["status"] == "unavailable"
    assert "reason" in data["models"]["landslide"]

    # Limits and specs
    assert data["limits"]["max_upload_mb"] > 0
    assert data["limits"]["max_pixels"] > 0
    assert data["input_specs"]["flood"]["channels"] == 2
    assert data["input_specs"]["landslide"]["channels"] == 14

    # Disclaimer
    assert "does not forecast" in data["disclaimer"]
    assert "official warning authorities" in data["disclaimer"]


def test_not_found_error_envelope():
    """Verify 404 errors use standard error envelope."""
    response = client.get("/api/nonexistent-endpoint-test-404")
    assert response.status_code == 404
    data = response.json()

    assert "error" in data
    assert data["error"]["code"] == "NOT_FOUND"
    assert "message" in data["error"]
    assert isinstance(data["error"]["details"], dict)


def test_validation_error_envelope():
    """Verify 422 validation errors use standard error envelope."""
    # Mount temporary test router to trigger a validation error cleanly
    test_router = APIRouter()

    class TestPayload(BaseModel):
        count: int

    @test_router.post("/test-validation")
    def sample_endpoint(payload: TestPayload):
        return {"count": payload.count}

    app.include_router(test_router)

    response = client.post("/test-validation", json={"count": "invalid-non-integer"})
    assert response.status_code == 422
    data = response.json()

    assert "error" in data
    assert data["error"]["code"] == "VALIDATION_ERROR"
    assert "validation_errors" in data["error"]["details"]


def test_cors_allowed_origin():
    """Verify CORS headers for allowed origin http://localhost:5173."""
    response = client.get(
        "/api/health",
        headers={"Origin": "http://localhost:5173"},
    )
    assert response.status_code == 200
    assert response.headers.get("access-control-allow-origin") == "http://localhost:5173"


def test_cors_rejected_origin():
    """Verify CORS does not allow unauthorized origins."""
    response = client.get(
        "/api/health",
        headers={"Origin": "http://unauthorized-domain.com"},
    )
    assert response.status_code == 200
    # Should NOT return the unauthorized origin in access-control-allow-origin
    assert response.headers.get("access-control-allow-origin") != "http://unauthorized-domain.com"

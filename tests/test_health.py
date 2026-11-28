"""Baseline tests verifying the environment and API endpoints."""


def test_environment_sanity():
    """Verify that Python testing runs cleanly."""
    assert 1 + 1 == 2


def test_backend_import():
    """Verify backend main module imports without error and has the updated title."""
    from backend.main import app

    assert app.title == "NIRVYX API"

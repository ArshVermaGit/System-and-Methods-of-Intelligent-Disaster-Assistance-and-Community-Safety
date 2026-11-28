# Project Progress — NIRVYX

Tracks progress across implementation steps per `AGENTS.md`.

| Step | Branch | Status | Date | Description |
|---|---|---|---|---|
| 1 | `chore/step-1-foundation` | `done` | 2026-11-28 | CI, tooling, ruff/pytest config, .gitignore, .env.example, structure docs |
| 2 | `feat/step-2-backend` | `done` | 2026-11-28 | FastAPI backend architecture, settings, error hierarchy, health endpoints |
| 3 | `feat/step-3-react-frontend` | `pending` | — | React frontend connected to backend |
| 4 | `feat/step-4-postgis-database` | `pending` | — | PostGIS database and history API |
| 5 | `feat/step-5-hazard-pipelines` | `pending` | — | Flood and landslide pipelines |
| 6 | `feat/step-6-geospatial-exposure` | `pending` | — | Geospatial and exposure analysis |
| 7 | `feat/step-7-dashboard-pages` | `pending` | — | Dashboard pages |
| 8 | `feat/step-8-interactive-map` | `pending` | — | Interactive map |
| 9 | `test/step-9-system-testing` | `pending` | — | System testing and report |
| 10 | `docs/step-10-documentation` | `pending` | — | Documentation and deliverables |
| 11 | `model/step-11-real-models` | `pending` | — | Real model integration |

---

## Step 2 Details

- **Date:** 2026-11-28
- **Status:** `done`
- **What changed:**
  - Created `backend/app/` package structure with `core/`, `routes/`, `schemas/`, `services/`, and `database/`.
  - Implemented `core/config.py` using `pydantic-settings`, cached singleton `get_settings()`, resolving relative paths from repo root, and loading root `.env`.
  - Implemented `core/logging.py` for structured application logging.
  - Implemented `core/errors.py` with `AppError` base class, domain error subclasses, and exception handlers returning standard error envelopes (`{"error": {"code": ..., "message": ..., "details": ...}}`). Tracebacks logged server-side only.
  - Implemented Pydantic models in `schemas/` (`health.py`, `system.py`, `error.py`).
  - Implemented API routes in `routes/` (`health.py`, `system.py`):
    - `GET /` and `GET /health` legacy compatibility endpoints.
    - `GET /api/health` returning `{"status": "running", "application": "NIRVYX", ...}`.
    - `GET /api/system/info` returning diagnostic info, database status (`not_configured`), models status (`unavailable`), limits, input specs, and official disclaimer.
  - Built `app/main.py` with title `NIRVYX API`, description, version `1.0.0`, strict CORS middleware from settings (`allow_credentials=False`), and error handlers.
  - Converted `backend/main.py` to a compatibility shim.
  - Added `backend/requirements.txt` pointing to `-r ../requirements.txt`.
  - Updated `backend/README.md` with instructions to run from repo root.
  - Created `tests/backend/test_api.py` covering all endpoints, 404, 422, CORS, and fresh startup; updated `tests/test_health.py` with new API title assertion.
- **Checks run:**
  - `ruff check .`: Passed (0 errors)
  - `ruff format --check .`: Passed (24 files formatted)
  - `pytest`: Passed (11 passed in 0.24s)
  - Live server verification:
    - `curl http://127.0.0.1:8000/api/health` -> HTTP 200 `{"status":"running","application":"NIRVYX",...}`
    - `curl http://127.0.0.1:8000/docs` -> HTTP 200
  - `pre-commit run --all-files`: Passed (all hooks green)
- **Open items / Hand-off:**
  - Arsh to push `feat/step-2-backend` and open PR to merge into `main`.

---

## Step 1 Details

- **Date:** 2026-11-28
- **Status:** `done`
- **What changed:**
  - Fixed `.github/workflows/ci.yml`: expression syntax, Node 24, Python 3.11/3.12 matrix, Vitest flags, Ruff strict checks, non-blocking docs lint.
  - Added `ruff.toml` with E, F, I, B rules and FastAPI immutable calls allowed under B008.
  - Pinned `ruff==0.4.10` in `requirements-dev.txt` matching `.pre-commit-config.yaml`.
  - Added `pytest.ini` with `db` and `real_model` test markers.
  - Updated `.pre-commit-config.yaml` to exclude Vite tsconfig comments in `check-json`.
  - Updated `.gitignore` for `/lib/`, recursive `/data/**` DVC rules, and `/results/**`.
  - Aligned `.env.example` with `CONTRACTS.md` Section 2 (PostGIS psycopg2 driver, limits, predictor paths).
  - Added `models/README.md`, `results/README.md`, `results/flood/README.md`, `results/landslide/README.md`, and `docs/STRUCTURE.md`.
  - Updated `README.md`, `.github/labeler.yml`, `.github/CODEOWNERS`, and `CONTRIBUTING.md`.
  - Fixed `backend/main.py` import ordering and line length; formatted `tests/test_health.py`.
- **Checks run:**
  - `ruff check .`: Passed (0 errors)
  - `ruff format --check .`: Passed (6 files formatted)
  - `pytest`: Passed (2 tests passed)
  - `actionlint .github/workflows/*.yml`: Passed (0 errors)
  - `git check-ignore` checks: `frontend/src/lib/api.ts` (1, not ignored), `results/flood/x/mask.tif` (0, ignored) — Passed
  - `pre-commit run --all-files`: Passed (all hooks green)
- **Open items / Hand-off:**
  - Arsh to install Python 3.12 and Node 24 on macOS via Homebrew (`brew install python@3.12 node@24`).
  - Arsh to push `chore/step-1-foundation` and verify GitHub Actions CI run is green.

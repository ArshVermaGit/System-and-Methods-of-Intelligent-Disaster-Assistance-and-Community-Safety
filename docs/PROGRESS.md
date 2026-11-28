# Project Progress — NIRVYX

Tracks progress across implementation steps per `AGENTS.md`.

| Step | Branch | Status | Date | Description |
|---|---|---|---|---|
| 1 | `chore/step-1-foundation` | `done` | 2026-11-28 | CI, tooling, ruff/pytest config, .gitignore, .env.example, structure docs |
| 2 | `feat/step-2-fastapi-backend` | `pending` | — | FastAPI backend |
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

# NIRVYX — Repository Structure & Mapping

This document maps the project assignment layout to this repository and defines component boundaries.

## Assignment to Repository Mapping

| Assignment Spec | Repository Location | Owner | Description |
|---|---|---|---|
| `ml/flood` | `flood/` | Ayush Gupta | Flood segmentation models, preprocessing, Sen1Floods11 / Sentinel-1 |
| `ml/landslide` | `landslide/` | Akshay Ujjwal | Landslide segmentation, Sentinel-2 / Landslide4Sense / SRTM |
| `datasets/` | `data/` | Shared (DVC) | Raw, interim, and processed datasets |
| `backend/` | `backend/app/` | Arsh Verma | FastAPI services, routes, schemas, core configuration |
| `database/` | `database/` | Arsh Verma | PostgreSQL + PostGIS schemas, Alembic migrations |
| `frontend/` | `frontend/` | Arsh Verma | React + TypeScript + MapLibre GL JS interactive dashboard |
| `models/` | `models/` | Model owners | Checkpoints (`*.pt`) tracked via DVC (not in Git) |
| `results/` | `results/` | Runtime | Runtime inference outputs (`mask.tif`, `overlay.png`, etc.) |
| `docs/` | `docs/` | Shared | Architecture specs, contracts, progress logs |

## Architectural Principles
1. **Module Independence:** `flood/` and `landslide/` are maintained independently by model owners. The backend adapts to their model prediction interfaces inside `backend/app/services/`.
2. **Geospatial Integrity:** All geospatial analysis requires verified coordinate reference systems (CRS) and affine transforms. Non-georeferenced inputs produce pixel previews without false coordinates.
3. **Clean Storage:** Large rasters, checkpoints, and datasets are tracked via DVC or external storage; Git stays fast and lightweight.

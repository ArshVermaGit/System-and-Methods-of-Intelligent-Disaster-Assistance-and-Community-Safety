## 📌 Description of Changes

<!-- Briefly describe the problem you are solving or feature you are adding. -->


## 🎯 Type of Change

- [ ] ✨ `feat`: New feature (non-breaking change which adds functionality)
- [ ] 🐛 `fix`: Bug fix (non-breaking change which fixes an issue)
- [ ] 🧠 `model`: ML / Deep learning model architecture, training, or evaluation change
- [ ] 🗺️ `geospatial`: Geospatial data preprocessing, ingestion, or analysis
- [ ] ⚡ `perf`: Performance improvement (faster queries, optimized raster pipeline, etc.)
- [ ] ♻️ `refactor`: Code refactoring without changing functionality
- [ ] 🧪 `test`: Adding or updating tests
- [ ] 📝 `docs`: Documentation updates or research notes
- [ ] 👷 `ci`: CI/CD pipeline or repository tooling updates
- [ ] 🗄️ `database`: Schema change or PostGIS migration

---

## 📦 Module(s) Affected

- [ ] `flood/` (Flood segmentation, Sentinel-1, Sen1Floods11)
- [ ] `landslide/` (Landslide segmentation, Landslide4Sense, Sentinel-2, SRTM)
- [ ] `backend/` (FastAPI services, API endpoints, Pydantic schemas)
- [ ] `frontend/` (React, MapLibre GL JS / Leaflet dashboard)
- [ ] `database/` (PostgreSQL, PostGIS, spatial queries)
- [ ] `data/` (DVC data management, dataset scripts)
- [ ] `docs/` (Architecture, reports, research specs)
- [ ] `scripts/` (Utility and operational scripts)

---

## 🔗 Related Issue(s)

<!-- Closes #123 / Fixes #123 -->
Closes #

---

## 📊 ML / Data Provenance (if applicable)

- **Dataset / Source:** (e.g. Sen1Floods11, Sentinel-1, Sentinel-2, SRTM DEM, GPM IMERG)
- **Tracking:** Are large data files tracked with DVC rather than committed directly to git?
  - [ ] Yes, tracked with DVC (`*.dvc` file committed)
  - [ ] Not applicable (no datasets touched)
- **Evaluation Metrics Reported:**
  - Precision: `N/A`
  - Recall: `N/A`
  - F1-Score: `N/A`
  - IoU / mIoU: `N/A`
  - Dice: `N/A`

---

## 🧪 Testing & Verification

<!-- Explain how you tested these changes (e.g., unit tests run, Postman API calls, manual UI testing, raster visualization). -->
- Steps to reproduce / verify:
  1.
  2.

---

## 🖼️ Screenshots / Visual Demos (if applicable)

<!-- Add screenshots of the frontend map, segmented masks, terminal output, or metric plots. -->

---

## ✅ Author Checklist

- [ ] My code follows the project's coding conventions and style guidelines.
- [ ] I have executed `pre-commit run --all-files` locally and all checks passed.
- [ ] I have not committed raw dataset binaries (`.tif`, `.nc`, `.h5`, `.zip`) to git; DVC is used where necessary.
- [ ] I have not committed any `.env` files, API keys, credentials, or private secrets.
- [ ] I have updated the documentation / README if my change introduces new dependencies or API contracts.
- [ ] New and existing tests pass locally with my changes.

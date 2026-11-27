# System and Methods of Intelligent Disaster Assistance and Community Safety

**An Engineering Project in Community Service — Phase I**
VIT Bhopal University, Bhopal, Madhya Pradesh – 466114

B.Tech in Computer Science and Engineering

> **Status:** Under development. Features listed as planned are not yet implemented, and no model performance results are reported until experiments are complete. This project supports preparedness and decision-making and does not replace official disaster-management or warning authorities.

---

## Overview

A geographical platform for flood and landslide risk assessment. It brings together historical disaster records, satellite imagery, rainfall, river discharge and terrain data into one map-based dashboard, and links hazard outputs to nearby settlements and infrastructure.

## Objectives

- Organise reliable disaster-related datasets with documented provenance
- Develop flood-water and landslide segmentation modules
- Analyse rainfall, river discharge and terrain characteristics
- Assess exposure of settlements, roads and public facilities
- Provide a backend, geospatial database and interactive dashboard
- Evaluate components with standard metrics (Precision, Recall, F1, IoU, Dice)

## Data Sources

| Hazard | Sources |
|---|---|
| Flood | Sen1Floods11, Sentinel-1, Global Flood Database, GPM IMERG, GloFAS |
| Landslide | Landslide4Sense, Sentinel-2, SRTM DEM |
| Exposure | OpenStreetMap |

## Tech Stack

- **Frontend:** React, TypeScript, MapLibre GL JS / Leaflet
- **Backend:** Python, FastAPI, Pydantic
- **Database:** PostgreSQL, PostGIS
- **ML / Geospatial:** PyTorch, scikit-learn, Rasterio, GDAL, GeoPandas
- **Tooling:** Git, Docker, DVC

## Repository Structure

```
├── docs/          # research, architecture, reports
├── data/          # raw, interim, processed, metadata (DVC-managed)
├── flood/         # flood preprocessing, models, evaluation
├── landslide/     # landslide preprocessing, models, evaluation
├── backend/       # FastAPI services
├── frontend/      # React dashboard
├── database/      # schema and migrations
├── tests/
└── scripts/
```

## Getting Started

```bash
git clone <repository-url>
cd <repository-folder>
python -m venv venv && source venv/bin/activate
pip install -r requirements.txt
cp .env.example .env     # add credentials locally; never commit .env
```

## Limitations

- Segmentation identifies mapped water or landslide areas; it does not forecast future events.
- Rainfall and river-discharge products are estimates with their own latency and coverage limits.
- All outputs require validation against reference data before use.

## Team

| Name | Registration No. |
|---|---|
| Ayush Gupta | 24BAI10220 |
| Arsh Verma | 24BCG10026 |
| Reshabh Lahoti | 24BCE10343 |
| Vanshita Patidar | 24BCE11216 |
| Chesta Singh | 24BCE10016 |
| Akshay Ujjwal | 24BSA10374 |

## Licence

To be decided by the team.

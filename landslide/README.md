# Landslide Hazard Module

This module develops landslide detection, scar segmentation, and terrain susceptibility analysis.

## Key Datasets & Products
- **Landslide4Sense**: Multi-sensor benchmark for landslide detection.
- **Sentinel-2 MSI**: Optical multispectral imagery (NDVI, NDWI, false-color composites).
- **SRTM DEM**: Digital Elevation Model for slope, aspect, and curvature extraction.

## Planned Structure
- `preprocessing/`: Terrain feature engineering (slope, aspect, flow accumulation) and optical cloud masking.
- `models/`: Segmentation models trained on multi-sensor features.
- `evaluation/`: Standard classification and segmentation metrics.

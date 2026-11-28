# Landslide Assessment Results

Runtime outputs for landslide segmentation assessments.

Each assessment creates a subdirectory: `results/landslide/<assessment_id>/` containing:
- `mask.tif`: Landslide hazard mask GeoTIFF.
- `probability.tif`: Landslide probability surface GeoTIFF.
- `overlay.png`: RGBA transparent visualization overlay for map display.
- `mask.geojson`: Vectorized hazard polygons (when georeferenced).
- `metadata.json`: Assessment metadata and summary statistics.

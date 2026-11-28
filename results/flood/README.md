# Flood Assessment Results

Runtime outputs for flood segmentation assessments.

Each assessment creates a subdirectory: `results/flood/<assessment_id>/` containing:
- `mask.tif`: Binary or categorized hazard mask GeoTIFF.
- `probability.tif`: Float32 flood probability GeoTIFF.
- `overlay.png`: RGBA transparent visualization overlay for map display.
- `mask.geojson`: Vectorized hazard polygons (for georeferenced inputs).
- `metadata.json`: Assessment metadata and summary statistics.

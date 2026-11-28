# Runtime Assessment Results

This directory stores runtime inference and geospatial assessment outputs.

## Structure
- `flood/<assessment_id>/`: Generated flood masks, probabilities, overlays, and GeoJSON.
- `landslide/<assessment_id>/`: Generated landslide hazard maps and assessment artifacts.
- `uploads/`: Temporary uploaded rasters.

## Guidelines
- Output files in this directory are generated at runtime and are **never committed to Git**.
- See `CONTRACTS.md` Section 8 for exact output schemas and file naming conventions.

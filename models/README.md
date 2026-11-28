# Model Checkpoints

This directory stores trained deep learning checkpoints for flood and landslide segmentation (e.g. `flood.pt`, `landslide.pt`).

## Guidelines
- Checkpoints and binary weights are **never committed to Git**.
- Files here are tracked via DVC or hosted on designated external model storage.
- The default predictor modules look for checkpoints defined in `FLOOD_CHECKPOINT_PATH` and `LANDSLIDE_CHECKPOINT_PATH`.

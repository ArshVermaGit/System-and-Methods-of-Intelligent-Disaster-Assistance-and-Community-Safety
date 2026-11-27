# Data Directory (DVC-Managed)

All datasets are version-controlled using [DVC](https://dvc.org/).

## Directory Layout
- `raw/`: Untouched primary satellite tiles and sensor data.
- `interim/`: Clipped, reprojected, or normalized intermediate rasters.
- `processed/`: Final training tensors, feature matrices, and evaluation splits.

## Usage Rule
Never commit files inside `raw/`, `interim/`, or `processed/` directly to Git.
Use:
```bash
dvc add data/raw/<dataset_archive>
git add data/raw/<dataset_archive>.dvc
```

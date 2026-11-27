# Flood Hazard Module

This module handles flood-water segmentation and hydrological hazard analysis.

## Key Datasets & Products
- **Sen1Floods11**: Sentinel-1 SAR imagery and ground-truth flood masks.
- **Sentinel-1 GRD**: Surface water detection via VV/VH polarizations.
- **GPM IMERG**: Near-real-time precipitation rate estimates.
- **GloFAS**: Global flood awareness system discharge forecasts.

## Planned Structure
- `preprocessing/`: SAR calibration, speckle filtering, and band composition.
- `models/`: PyTorch deep learning architectures for water surface segmentation.
- `evaluation/`: IoU, Dice coefficient, Precision, Recall, and confusion matrix calculation.

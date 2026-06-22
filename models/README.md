# Trained model

The trained YOLOv8s weight is distributed through the repository's GitHub Releases rather than Git history.

## Model summary

- File: `best.pt`
- Size: approximately 22.5 MB
- Classes: 18
- Input size: 640 × 640
- Training: 25 epochs on a Tesla T4
- Validation mAP@0.5: 0.381
- Validation mAP@0.5:0.95: 0.292

```python
from ultralytics import YOLO

model = YOLO("best.pt")
results = model.predict(source=0, imgsz=640, conf=0.25)
```

The original TACO-derived dataset is not bundled with this repository. Follow the attribution and license information in the main README when reproducing the training process.

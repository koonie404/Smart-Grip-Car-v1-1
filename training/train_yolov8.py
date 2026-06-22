"""Train Smart Grip Car's 18-class TACO detector with Ultralytics YOLOv8."""

from argparse import ArgumentParser
from pathlib import Path

from ultralytics import YOLO


def parse_args():
    parser = ArgumentParser()
    parser.add_argument("--data", type=Path, required=True, help="Path to data.yaml")
    parser.add_argument("--model", default="yolov8s.pt")
    parser.add_argument("--epochs", type=int, default=25)
    parser.add_argument("--imgsz", type=int, default=640)
    parser.add_argument("--batch", type=int, default=16)
    parser.add_argument("--device", default="0")
    parser.add_argument("--project", default="runs/detect")
    parser.add_argument("--name", default="smart_grip_car_v11")
    return parser.parse_args()


def main():
    args = parse_args()
    if not args.data.is_file():
        raise FileNotFoundError(f"Dataset config not found: {args.data}")

    model = YOLO(args.model)
    model.train(
        data=str(args.data.resolve()),
        epochs=args.epochs,
        imgsz=args.imgsz,
        batch=args.batch,
        device=args.device,
        project=args.project,
        name=args.name,
        plots=True,
    )


if __name__ == "__main__":
    main()

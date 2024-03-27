from ultralytics import YOLO

model = YOLO('yolov8x')

model.predict('inputdata/image2.jpeg', save=True)
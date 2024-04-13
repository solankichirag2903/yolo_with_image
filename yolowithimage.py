from ultralytics import YOLO
import cv2

model = YOLO('yolomodels/yolov8l.pt')
results = model('car_img.jpg', show=True)
cv2.waitKey(0)

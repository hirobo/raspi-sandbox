import cv2
from datetime import datetime
from time import sleep
import os

CASCADE_DIR = "data/opencv/haarcascades"
CASCADE_FILE = os.path.join(CASCADE_DIR, "haarcascade_frontalface_default.xml")
IMG_OUTPUT_DIR = "data/output"
MIN_SIZE = (150, 150)

cascade = cv2.CascadeClassifier(CASCADE_FILE)

camera = cv2.VideoCapture(0)

try:
    while True:
        _, img = camera.read()
        img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        faces = cascade.detectMultiScale(img_gray, minSize=MIN_SIZE)
        if len(faces) == 0:
            continue
        for (x, y, w, h) in faces:
            color = (255, 0, 0)
            cv2.rectangle(img, (x, y), (x+w, y+h), color, thickness=8)
            time_s = datetime.now().strftime("%Y-%m-%d_%H_%M_%S")
            file_name = f"face_{time_s}.jpg"
            cv2.imwrite(os.path.join(IMG_OUTPUT_DIR, file_name), img)
            print("saved a face!")
            sleep(3)

except KeyboardInterrupt:
    print("ok.")

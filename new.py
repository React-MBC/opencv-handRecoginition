import cv2
from cvzone.HandTrackingModule import HandDetector
import numpy as np

cap = cv2.VideoCapture(0)
detector = HandDetector(maxHands=1)

offset = 20
imgsize = 300
while True:
    success, img = cap.read()
    hands, img = detector.findHands(img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
    try:
        if hands:
            hand = hands[0]
            x, y, w, h = hand['bbox']
            img_white = np.ones((imgsize, imgsize, 3), np.uint8) * 255
            img_crp = img[y - offset:y + h + offset, x - offset:x + w + offset]
            img_crp_shp = img_crp.shape
            cv2.imshow('ImageCrop', img_crp)
    except:
        print("out of bound")
    cv2.imshow('Image', img)
    cv2.waitKey(1)

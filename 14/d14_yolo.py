from aocd import data, submit
import sys
from collections import defaultdict, deque
import re
import cv2
import numpy as np
from ultralytics import YOLO

model = YOLO("yolo11m.pt")

def main(s):
    s = s.split("\n")
    p = []
    for i in s:
        p.append(list(map(int, re.findall(r'(?:-)*\d+', i))))
    w = 101
    h = 103
    for t in range(10000):
        for i in p:
            i[0] = (i[0] + i[2]) % w
            i[1] = (i[1] + i[3]) % h
        # yolo look for christmas trees
        if t == 8257:
            print(t+1)
            mat = np.zeros((h,w,3), np.uint8)
            for i in p:
                mat[i[1],i[0]] = [0, 255, 0]
            # predict confidence
            # scale mat to 512x512
            mat = cv2.resize(mat, (512, 512))
            r = model.predict([mat])
            print(r)
            img = r[0].plot()  # This plots the detections on the image

            # Convert BGR to RGB (OpenCV uses BGR by default)
            img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
            cv2.imshow('Detection Results', img_rgb)
            cv2.waitKey(0)

            cv2.imshow('image', mat)
            cv2.imwrite('d14.png', mat)
            cv2.waitKey(0)

if __name__ == "__main__":
    main(data)
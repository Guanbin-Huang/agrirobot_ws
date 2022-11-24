#!/usr/bin/python

import cv2
cap = cv2.VideoCapture(0) # 0->front  2->back
print(cap.isOpened())

if not cap.isOpened():
    print("Cannot open camera")

while True:
    ret, frame = cap.read()
    cv2.imwrite("frame.jpg", frame)
    
    if not ret:
        break
    
    cv2.imshow("frame", frame)

    if cv2.waitKey(1) == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()
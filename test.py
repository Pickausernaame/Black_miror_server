
# coding: utf-8

import requests
import json
import cv2

if __name__ == "__main__":

    cap = cv2.VideoCapture(0)
    
    while True:
        ret, frame = cap.read()
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        _, img_encoded = cv2.imencode('.jpg', gray)
        cv2.imshow("Client image", gray )
        if cv2.waitKey(1) & 0xFF == ord('q'):  # Условия выхода
            break
    cap.release()


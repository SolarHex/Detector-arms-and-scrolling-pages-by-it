import mediapipe as mp
import cv2
import numpy as np
import time
import math
import pyautogui as aut

wCam, hCam = 640, 720

cap = cv2.VideoCapture(0)
cap.set(3, wCam)
cap.set(4,hCam)
pTime = 0

mpHands = mp.solutions.hands
hands = mpHands.Hands()
mpDraws = mp.solutions.drawing_utils

while True: 
    success, img = cap.read()
    
    
    imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    results = hands.process(imgRGB)

    lmList = []    
    if results.multi_hand_landmarks:
        for handLms in results.multi_hand_landmarks:
            for id, lm in enumerate(handLms.landmark):
                h, w, c = img.shape
                cx, cy = int(lm.x*100), int(lm.y*100)
                lmList.append([id, cx, cy])
                mpDraws.draw_landmarks(img, handLms, mpHands.HAND_CONNECTIONS)

    if len(lmList) != 0:
        if lmList[8][2] == lmList[6][2] & lmList[12][2] == lmList[10][2]:
            aut.scroll(-1500)
        if lmList[8][2] > lmList[6][2] & lmList[12][2] > lmList[10][2]:
           aut.scroll(1500) 

    cTime = time.time()
    fps = 1/(cTime - pTime)
    pTime = cTime
    
    cv2.putText(img, f'FPS : {int(fps)}', (40,70), cv2.FONT_HERSHEY_COMPLEX_SMALL, 1, (255,0,0), 3)
    
    cv2.imshow('Smart Laptop', img)
    cv2.waitKey(1)
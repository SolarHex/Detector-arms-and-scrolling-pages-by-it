import mediapipe as mp
import cv2
import numpy as np
import time
import webbrowser

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
    # print(results.multi_hand_landmarks)
    
    if results.multi_hand_landmarks:
        for handLms in results.multi_hand_landmarks:
            for id, lm in enumerate(handLms.landmark):
                # print(id,lm)
                h, w, c = img.shape
                cx, cy = int(lm.x*100), int(lm.y*h)
                print(id, cx, cy)
                
                if cx == 70: 
                    webbrowser.open('https://vk.com/al_feed.php')
                
            mpDraws.draw_landmarks(img, handLms, mpHands.HAND_CONNECTIONS)
        
    
    
    cTime = time.time()
    fps = 1/(cTime - pTime)
    pTime = cTime
    
    cv2.putText(img, f'FPS : {int(fps)}', (40,70), cv2.FONT_HERSHEY_COMPLEX_SMALL, 1, (255,0,0), 3)
    
    cv2.imshow('Smart Laptop', img)
    cv2.waitKey(1)
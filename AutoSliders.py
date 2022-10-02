import mediapipe as mp
import cv2
import numpy as np
import time
# import webbrowser
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
                # print(id, cx, cy)
                
                # if cx == 70: 
                #     webbrowser.open('https://vk.com/al_feed.php')
                lmList.append([id, cx, cy])
                
                mpDraws.draw_landmarks(img, handLms, mpHands.HAND_CONNECTIONS)

    if len(lmList) != 0:
        # print(lmList[4],lmList[8])
        
        x1, y1 = lmList[4][1], lmList[4][2]
        x2, y2 = lmList[8][1], lmList[8][2]

        
        cv2.circle(img, (x1,y1), 15, (0,0,255),3)
        cv2.circle(img, (x2,y2), 15, (0,0,255),3)

        
        cv2.line(img, (x1,y1), (x2,y2), (255,0,255),3)
        
        lenght = math.hypot(x2-x1, y2-y1) 
        print(round(lenght)) 
          
   
        # if lenght>30: 
        #         aut.hotkey('ctrl','+')
        # elif lenght<20:
        #         aut.hotkey('ctrl','-')

        x1, y1 = lmList[20][1], lmList[20][2]
        cv2.circle(img, (x1,y1), 15, (0,0,255),3)
        print(x1,y1)
            
        if lmList[8][2] > lmList[6][2]:
                aut.scroll(200)
        elif lmList[8][2] < lmList[6][2]:
                aut.scroll(-200)
                
        if lmList[12][2] > lmList[10][2]: 
                aut.hotkey('ctrl','+')
        elif lmList[16][2] > lmList[14][2]:
                aut.hotkey('ctrl','-')
        # elif lmList[20][2] < lmList[18][2]:
        #         aut.screenshot('Russia')
                
            
    
    cTime = time.time()
    fps = 1/(cTime - pTime)
    pTime = cTime
    
    cv2.putText(img, f'FPS : {int(fps)}', (40,70), cv2.FONT_HERSHEY_COMPLEX_SMALL, 1, (255,0,0), 3)
    
    cv2.imshow('Smart Laptop', img)
    cv2.waitKey(1)
import cv2
import mediapipe as mp
import FindUserHand as fuh
import HandDetectorModule as hdm
import WinOrLoose as wl
import time
import threading
# import StopTime as st

rockimg=cv2.imread('rock.jpg',1)
paperimg=cv2.imread('paper.jpg',1)
sisorimg=cv2.imread('sisor.webp',1)
rockimg=cv2.resize(rockimg, (600, 400))
paperimg=cv2.resize(paperimg, (600, 400))
sisorimg=cv2.resize(sisorimg, (600, 400))
# cv2.imshow('win', sisorimg)
# cv2.waitKey(0)
gameimg=[rockimg, paperimg, sisorimg]
pwin=0
cwin=0
win=4
imgVal=None
# lee=0
# id=4s
cap=cv2.VideoCapture(0)
while True:
    ret, img=cap.read()
    id=fuh.userImg(img)
    if id!=None:
        win, img, cid=wl.doAll(img, id, gameimg)
        if(win==1):
            pwin=pwin+1
            win=3
        elif(win==0):
            cwin=cwin+1
            win=3
        cv2.imshow('Ai Game',gameimg[cid])
        cv2.imshow('user Game',gameimg[id])
        time.sleep(1)

    cv2.putText(img, "user wins | Ai wins",(20,400), cv2.FONT_HERSHEY_COMPLEX_SMALL, 1, (255,23,0), 2)
    cv2.putText(img, str(pwin), (50, 450), cv2.FONT_ITALIC, 1, (255,23,0), 2)
    cv2.putText(img, str(cwin), (200, 450), cv2.FONT_ITALIC, 1, (255,23,0), 2)
    cv2.imshow('win', img)
    if cv2.waitKey(1)==ord('s'):
        break
cap.release()
cv2.destroyAllWindows()


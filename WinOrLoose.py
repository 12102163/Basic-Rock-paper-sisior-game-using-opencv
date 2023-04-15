import cv2
import mediapipe as mp
import random as rd

cid = 4
def winLoose(id, cid):
    if( (id==0 and cid==0) or (id==1 and cid==1) or (id==2 and cid==2) ):
        return 2
    elif( (id==0 and cid==2) or (id==1 and cid==0) or (id==2 and cid==1) ):
        return 1
    return 0

def doAll(img, id, gameimg):
    cid=rd.randint(0,2)
    # h, w, c=img.shape
    
    win=winLoose(id, cid)
    return win, img, cid
    # winLose(id, cid)

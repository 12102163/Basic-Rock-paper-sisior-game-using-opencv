import cv2
import mediapipe as mp
import HandDetectorModule as hdm

hd=hdm.HandDetector()

#############################################################################################  rock check

def rockCheck(t, i, m, r, l, tb, ib, mb, rb, lb):
    if(t > tb or i>ib and m>mb and r>rb and l>lb):
        return True
    return False

############################################################################################### paper check

def paperCheck(t, i, m, r, l, tb, ib, mb, rb, lb):
    if(t < tb and i<ib and m<mb and r<rb and l<lb):
        return True
    return False

############################################################################################### sisor check

def sisorCheck(t, i, m, r, l, tb, ib, mb, rb, lb):
    if(t > tb or i<ib and m<mb and r>rb and l>lb):
        return True
    return False

#################################################################################################

def userImg(img):
    img =hd.findHands(img, draw=False)
    lmlist=hd.getPoints(img)
    if len(lmlist)!=0:
        # print("in")
        t, i, m, r, l=lmlist[4][2], lmlist[8][2], lmlist[12][2], lmlist[16][2], lmlist[20][2]
        tb, ib, mb, rb, lb= lmlist[2][2], lmlist[5][2], lmlist[9][2], lmlist[13][2], lmlist[17][2]
        if (rockCheck(t, i, m, r, l, tb, ib, mb, rb, lb)):
            return 0
        elif(paperCheck(t, i, m, r, l, tb, ib, mb, rb, lb)):
            return 1
        elif(sisorCheck(t, i, m, r, l, tb, ib, mb, rb, lb)):
            return 2
        

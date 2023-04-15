import cv2
import mediapipe as mp

class HandDetector():
    def __init__(self, detectconf=50, trackconf=50):
        # self.mode=mode
        # self.nohands=nohands
        self.detectconf=detectconf
        self.trackconf=trackconf


        self.mpHands=mp.solutions.hands
        self.hands=self.mpHands.Hands(self.detectconf,
        self.trackconf)

        
        self.mpDraw=mp.solutions.drawing_utils

    def findHands(self, img, draw=True):
        rgb=cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        self.res=self.hands.process(rgb)
        if self.res.multi_hand_landmarks:
            for handml in self.res.multi_hand_landmarks:
                if draw:
                    self.mpDraw.draw_landmarks(img, handml, 
                                           self.mpHands.HAND_CONNECTIONS)
        return img
    
    def getPoints(self, img, handpo=0):
        lst =[]
        if self.res.multi_hand_landmarks:
            myhand = self.res.multi_hand_landmarks[handpo]
            for id,lm in enumerate(myhand.landmark):
                h,w,c=img.shape
                lst.append([id,int(w*lm.x),int(h*lm.y)])
        return lst

    
def main():
    cap=cv2.VideoCapture(0)
    detect=HandDetector()

    while True:
        ret, img=cap.read()
        img =cv2.resize(img, (800,500))
        img = detect.findHands(img)
        lst = detect.getPoints(img)
        if(len(lst)!=0):
            print(lst[4])
        cv2.imshow('image',img)
        
        if cv2.waitKey(1)==ord('s'):
            break
    cap.release()
    cv2.destroyAllWindows()

if __name__=="__main__":
    main()




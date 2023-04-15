import cv2
import mediapipe as mp

class PoseDetector():
    def __init__(self, Static_mode=False, model_comp=1, smooth_landmark=True, enable_segme=False, smooth_segmen=True,detconf=0.5, trackconf=0.5):
        self.Static_mode=Static_mode
        self.model_comp=model_comp
        self.smooth_landmark=smooth_landmark
        self.enable_segme=enable_segme
        self.detconf=detconf
        self.trackconf=trackconf
        
        # static_image_mode=False,
        #        model_complexity=1,
        #        smooth_landmarks=True,
        #        enable_segmentation=False,
        #        smooth_segmentation=True,
        #        min_detection_confidence=0.5,
        #        min_tracking_confidence=0.5
        
        self.mpPose=mp.solutions.pose
        self.pose=self.mpPose.Pose(Static_mode, model_comp, smooth_landmark, enable_segme, detconf, trackconf)
        self.mpDraw=mp.solutions.drawing_utils
    
    def findPose(self, img, draw=True):
        
        rgb=cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        self.res=self.pose.process(rgb)
        if self.res.pose_landmarks:
            if draw:
                self.mpDraw.draw_landmarks(img, self.res.pose_landmarks, self.mpPose.POSE_CONNECTIONS)
        return img

    def getPoints(self, img, ):
        lst=[]
        if self.res.pose_landmarks:
            for id,lm in enumerate(self.res.pose_landmarks.landmark):
                h, w, c=img.shape
                lst.append([str(id),str(int(w*lm.x)),str(int(h*lm.y))])
        return lst

    
def main():
    cap=cv2.VideoCapture("1.mp4")
    pdetect=PoseDetector()
    while True:
        ret, img=cap.read()
        img = cv2.resize(img, (800,500))
        img=pdetect.findPose(img, False)
        lst=pdetect.getPoints(img)
        print(lst[23])
        cv2.imshow('win', img)
        if cv2.waitKey(1)==ord('s'):
            break
    cap.release()
    cv2.destroyAllWindows()
if __name__=="__main__":
    main()
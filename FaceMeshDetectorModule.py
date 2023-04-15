import cv2
import mediapipe as mp

class FaceMeshDetector():
    def __init__(self, sta_img_mode=False, no_of_faces=4, refine_landmark=False, min_detection_confi=0.5, min_tracking_confi=0.5):
        self.sta_img_mode=sta_img_mode
        self.no_of_faces=no_of_faces
        self.refine_landmark=refine_landmark
        self.min_detection_confi=min_detection_confi
        self.min_tracking_confi=min_tracking_confi
        print("in")
        self.mpFaceMesh=mp.solutions.face_mesh
        self.facemesh=self.mpFaceMesh.FaceMesh(sta_img_mode, no_of_faces, refine_landmark, min_detection_confi, min_tracking_confi)

        self.mpDraw=mp.solutions.drawing_utils
        self.drawspec=self.mpDraw.DrawingSpec(thickness=1,circle_radius=1)
    def findFaceMesh(self, img, draw=True):
        lst=[]
        rgb=cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        self.res=self.facemesh.process(rgb)
        # print(lst)
        if self.res.multi_face_landmarks:
            for face_id,faceml in enumerate(self.res.multi_face_landmarks):
                if draw:
                    self.mpDraw.draw_landmarks(img, faceml, self.mpFaceMesh.FACEMESH_CONTOURS, self.drawspec, self.drawspec)
                for id,lm in enumerate(faceml.landmark):
                    h, w, c=img.shape
                    lst.append([face_id, id, int(lm.x*w), int(lm.y*h)])
        return lst, img
def main():

    cap = cv2.VideoCapture('5.mp4')
    fmdetect=FaceMeshDetector()

    while True:
        
        ret, img=cap.read()
        img=cv2.resize(img, (800,500))
        lst, img=fmdetect.findFaceMesh(img)
        print(lst)
        cv2.imshow('video',img)
        if cv2.waitKey(1)==ord('s'):
            break
    cap.release()
    cv2.destroyAllWindows()

if __name__=="__main__":
    main()

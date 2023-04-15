import cv2
import mediapipe as mp
# img=cv2.imread('lena.jpg',1)
# print([i for  i in dir(mp.solutions.face_detection().process(img)) ])
class FaceDetector():
    def __init__(self,  min_detection_conf=1, model_sel=0):
        self.min_detection_conf=min_detection_conf
        self.model_sel=model_sel
        self.mpFaceDetection=mp.solutions.face_detection
        self.face_detection=self.mpFaceDetection.FaceDetection(1)
        
    def findFaces(self, img, draw=True):
        lst=[]
        rgb=cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        self.res=self.face_detection.process(rgb)
        h, w, c=img.shape
        if self.res.detections:
            
            for facdml in self.res.detections:
                xc=facdml.location_data.relative_bounding_box.xmin
                yc=facdml.location_data.relative_bounding_box.ymin
                wid=facdml.location_data.relative_bounding_box.width
                hi=facdml.location_data.relative_bounding_box.height

                bbox=int(xc*w), int(yc*h),int(wid*w), int(hi*h)
                img=self.fancyDraw(img, bbox)
                # cv2.rectangle(img, bbox, (255, 255, 255), 2)
                cv2.putText(img, str(int(float(facdml.score[0])*100))+'%', (bbox[0], bbox[1]-20), cv2.FONT_HERSHEY_COMPLEX_SMALL, 1, (0,344,0), 1)
                lst.append([bbox,facdml.score[0]])
        return lst, img
    
    def fancyDraw(self, img, cordi, l=10, t=2):
        x, y, w, h=cordi
        
        x1, y1=x+w, y+h

        cv2.line(img, (x, y), (x+l, y), (255, 0, 255), t)
        cv2.line(img, (x,y), (x, y+l), (255, 0, 255), t)

        cv2.line(img, (x1, y), (x1-l, y), (255, 0, 255), t)
        cv2.line(img, (x1,y), (x1, y+l), (255, 0, 255), t)

        cv2.line(img, (x, y1), (x+l, y1), (255, 0, 255), t)
        cv2.line(img, (x,y1), (x, y1-l), (255, 0, 255), t)

        cv2.line(img, (x1, y1), (x1-l, y1), (255, 0, 255), t)
        cv2.line(img, (x1,y1), (x1, y1-l), (255, 0, 255), t)

        return img



def main():
    cap = cv2.VideoCapture('1.mp4')
    fdetect=FaceDetector()
    while True:
        ret, img=cap.read()
        img=cv2.resize(img, (800,500))
        lst, img=fdetect.findFaces(img)
        print(lst[0])
        cv2.imshow('video',img)
        if cv2.waitKey(1)==ord('s'):
            break
    cap.release()
    cv2.destroyAllWindows()

if __name__=="__main__":
    main()
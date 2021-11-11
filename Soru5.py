# ilk balığı tespit eden ancak diğerlerini tespit edemeyen uygulama
import cv2
import numpy as np

def getContours(img, imgContour):
    contours, hierarchy = cv2.findContours(img, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)    
    
    for cnt in contours:
        area= cv2.contourArea(cnt)
        if area > 10000:
            cv2.drawContours(imgContour, cnt, -1, (0,0,255),3)

fish = cv2.VideoCapture("sarıbalık1.mp4")

if (fish.isOpened()== False):
  print("Error opening video stream or file")

while fish.isOpened():
    ret,frame= fish.read()
    imgContour= frame.copy()
    if ret==1:
        
        hsv_fish = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
        
        lower = (28, 63, 85)
        upper = (137,255,190)
        
        mask = cv2.inRange(hsv_fish, lower, upper)
        result = cv2.bitwise_and(frame, frame, mask=mask)
        
        kernel=np.ones((5,5))
 
        imgDil= cv2.dilate(mask,kernel, iterations=2)        
        
        getContours(imgDil,imgContour)
        
        cv2.imshow("Video",imgContour)
        
        if cv2.waitKey(30) & 0xFF== ord('q'):
            break        
    else:
        break       
    
fish.release()
cv2.destroyAllWindows()  



 







# kaplumbağa tespit eden ve alanını yazdıran uygulama
import cv2
import numpy as np

#kontur çizen fonksiyon
def getContours(img, imgContour):
    contours, hierarchy = cv2.findContours(img, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)       
    for cnt in contours:
        area= cv2.contourArea(cnt)
        if area > 30000:
            cv2.drawContours(imgContour, cnt, -1, (0,0,255),3)
            cv2.putText(imgContour, "Area: "+str(area),(0,100),cv2.FONT_HERSHEY_SIMPLEX,1,(0,0,255),2)
   
    
turtle = cv2.VideoCapture("kaplumbaga1.mp4")

if (turtle.isOpened()== False):
  print("Error opening video stream or file")

while turtle.isOpened():
    ret,frame= turtle.read()
    
    #kontur çizebilmek için değişkene kopya görüntüyü atadım
    imgContour= frame.copy()
    if ret==1:        
    
        hsv_fish = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
        
        #alt ve üst hsv değerleri maskeleme için seçilir.
        lower = (0, 0, 0)
        upper = (179,182,166)
        
        mask = cv2.inRange(hsv_fish, lower, upper)
        result = cv2.bitwise_and(frame, frame, mask=mask)
        
        #dilation işlemi, görüntüdeki eksik kısımları tamamlaması için yapılır.
        kernel=np.ones((3,3)) 
        imgDil= cv2.dilate(mask,kernel, iterations=4)        
        
        getContours(imgDil,imgContour)              
        
        cv2.imshow("Video",imgContour)      
        
        if cv2.waitKey(30) & 0xFF== ord('q'):
            break        
    else:
        break       
    
#video dosyasının kapanmasını garanti altına alır.
turtle.release()
cv2.destroyAllWindows()  



 







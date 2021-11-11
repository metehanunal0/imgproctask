import cv2 
import numpy as np

#trackbar için boş fonksiyon
def empty(a):
    pass

#bulunan kontur alanı 40000 üzerindeyse çizdiren fonksiyon
def getContours(img, imgContour):
    contours, hierarchy = cv2.findContours(img, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)    
    
    for cnt in contours:
        area= cv2.contourArea(cnt)
        if area > 40000:
            cv2.drawContours(imgContour, cnt, -1, (0,0,255),3)
            cv2.putText(imgContour, "Area: "+str(area),(0,100),cv2.FONT_HERSHEY_SIMPLEX,1,(0,0,255),2)




cap= cv2.VideoCapture('denizanası1.mp4')

#eğer dosya açılamıyorsa hata vermesi için
if (cap.isOpened()== False):
  print("Error opening video stream or file")

#pencere ve trackbar ayarlamaları
cv2.namedWindow('Parameters', cv2.WINDOW_NORMAL)
cv2.resizeWindow("Parameters",200,200)
cv2.createTrackbar("Threshold1", "Parameters", 17, 255, empty)
cv2.createTrackbar("Threshold2", "Parameters", 2, 255, empty)

while cap.isOpened():     
    ret,frame=cap.read()    
    
    imgContour= frame.copy()
    if ret==True:        
        frame_gray= cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)  
        blur= cv2.GaussianBlur(frame_gray, (3,3),0)
        
        #canny edge için threshhold ayarlamaları
        th1= cv2.getTrackbarPos("Threshold1", "Parameters")
        th2= cv2.getTrackbarPos("Threshold2", "Parameters")
        imgCanny= cv2.Canny(blur, th1, th2)
        
        kernel= np.ones((5,5))
        imgDil=cv2.dilate(imgCanny,kernel,iterations=1)
        
        getContours(imgDil,imgContour)
        
        cv2.imshow("Video",imgContour)
        if cv2.waitKey(30) & 0xFF== ord('q'):
            break        
    else:
        break       
    
cap.release()
cv2.destroyAllWindows()    


import cv2
import numpy as np

fish = cv2.imread("resim1.jpg")

hsv_fish = cv2.cvtColor(fish, cv2.COLOR_BGR2HSV)

light_orange = (1, 172, 125)
dark_orange = (61,255,255)

mask = cv2.inRange(hsv_fish, light_orange, dark_orange)
result = cv2.bitwise_and(fish, fish, mask=mask)

light_white = (100, 0, 218)
dark_white = (142, 180, 255)

mask_white = cv2.inRange(hsv_fish, light_white, dark_white)
result_white = cv2.bitwise_and(fish, fish, mask=mask_white)

final_mask = mask + mask_white
final_result = cv2.bitwise_and(fish, fish, mask=final_mask)

kernel=np.ones((5,5),np.uint8)
 
opening= cv2.morphologyEx(final_mask,cv2.MORPH_OPEN,kernel,iterations=4)
ret, thresh= cv2.threshold(opening, 127,255,cv2.THRESH_BINARY)

contours, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)
cv2.drawContours(final_result, contours, -1, (0,255,0),3)

cv2.imshow("Mask", thresh)
cv2.imshow("WithContour", final_result)
cv2.waitKey(0)
cv2.destroyAllWindows()




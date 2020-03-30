import numpy as np

import matplotlib.pyplot as plt

import cv2

###########
###FUNC####
###########

def draw_circle(event,x,y,flags,param):
    
    #if event == cv2.EVENT_LBUTTONDOWN:
    #    cv2.circle(img,(x,y),100,(0,255,0), 2)
      
    #elif event ==cv2.EVENT_RBUTTONDOWN:
    if event ==cv2.EVENT_RBUTTONDOWN:

        cv2.circle(img,(x,y),100,(0,0,255), 2)
        

cv2.namedWindow(winname='my_drawing')

cv2.setMouseCallback('my_drawing', draw_circle)

#############################
##showing img with open cv###
#############################

img = cv2.imread('../DATA/dog_backpack.jpg')

while True:
    
        cv2.imshow('my_drawing',img)
        
        if cv2.waitKey(20) & 0xFF == 27:
            break
        
cv2.destroyAllWindows()
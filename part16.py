import numpy as np
import matplotlib.pyplot as plt
%matplotlib inline
import cv2

###FUNC###
###########

def draw_circle(event,x,y,flags,param):
    
    if event == cv2.EVENT
    
    pass

cv2.namedWindow(winname='my_drawing')

cv2.setMouseCallBack('my_drawing', draw_circle)


##showing img with open cv

img =- np.zeros((512,512,3), np.int8)

while True:
    
        cv2.imshow('my_drawing',img)
        
        if cv2.waitKey(20) & 0xFF == 27
        break
        
cv2.destroyAllwindows()
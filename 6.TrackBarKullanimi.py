# -*- coding: utf-8 -*-
"""
Created on Thu Jul  8 19:38:25 2021

@author: OSMAN MURAT HAŞLAK
"""

import cv2
import numpy as np 

img = np.zeros((512,512,3),np.uint8)

def nothing(x):
    pass


cv2.namedWindow("Resim")
cv2.createTrackbar("R","Resim",0, 255, nothing)
cv2.createTrackbar("G","Resim",0, 255, nothing)
cv2.createTrackbar("B","Resim",0, 255, nothing)
cv2.createTrackbar("ON/OFF","Resim",0,1,nothing)

while(1):
    cv2.imshow("Resim",img)
    
    if cv2.waitKey(1) & 0xFF==27:
        break
    switch = cv2.getTrackbarPos("ON/OFF","Resim")
    r = cv2.getTrackbarPos("R","Resim")
    g = cv2.getTrackbarPos("G","Resim")
    b = cv2.getTrackbarPos("B","Resim")

    if switch:    
        img[:] = [b,g,r]
    else:
        img[:] = 0
        

cv2.destroyAllWindows()


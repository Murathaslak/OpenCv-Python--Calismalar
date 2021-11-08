# -*- coding: utf-8 -*-
"""
Created on Tue Jul 27 14:22:20 2021

@author: OSMAN MURAT HAŞLAK
"""

import cv2

url = "http://192.168.0.26:8080/video"

cam = cv2.VideoCapture(url)

while cam.isOpen():
    ret, frame = cam.read()
    
    if not ret:
        print("Kameradan görüntü okunmadı")
        
    cv2.imshow("Görüntü",frame)
    
    if cv2.waitKey(1) == ord("q"):
        break
    
cv2.destroyAllWindows()
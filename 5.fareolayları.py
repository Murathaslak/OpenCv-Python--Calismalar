# -*- coding: utf-8 -*-
"""
Created on Thu Jul  8 16:37:31 2021

@author: OSMAN MURAT HAŞLAK
"""

import cv2
import numpy as np

# ===========LAZIM OLANI ARAR=================================================
# for i in dir(cv2):
#     if "EVENT" in i:
#         print (i)
# =============================================================================

cizim = False
mod = False
xi,yi = -1,-1

def draw(event,x,y,flags,param):
    global cizim 
    global xi,yi,mod
    
    if event == cv2.EVENT_LBUTTONDOWN:
        xi,yi = x,y
        cizim = True
        
    elif  event == cv2.EVENT_MOUSEMOVE:
        if cizim == True:
            if mod:
                cv2.circle(img,(xi,yi),10,(100,50,0),-1)
            else:
                cv2.rectangle(img,(xi,yi),(x,y),(0,0,255),-1)
        else:
            pass
        
    elif  event == cv2.EVENT_LBUTTONUP:
        cizim = False
    
# ==================ÇİFT TIKLAMAYLA DAİRE ÇİZİMİ================================================
#     #print(x,y) #farenin ekran kordinatlarını gösteriyor
#     if event == cv2.EVENT_LBUTTONDBLCLK:
#         cv2.circle(img,(x,y),50,(255,0,0),-1)
#     pass 
# =============================================================================

img = np.ones((512,512,3),np.uint8)
cv2.namedWindow("Paint")
cv2.setMouseCallback("Paint",draw)
while(1):
    cv2.imshow("Paint",img)
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break
    if cv2.waitKey(1) & 0xFF == ord("m"):
        mod = not mod        
cv2.destroyAllWindows()
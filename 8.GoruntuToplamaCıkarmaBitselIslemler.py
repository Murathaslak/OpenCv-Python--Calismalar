# -*- coding: utf-8 -*-
"""
Created on Wed Jul 14 19:58:34 2021

@author: OSMAN MURAT HAŞLAK
"""

import cv2
import numpy as np

img1 = cv2.imread("Resim/ben.jpg")
img2 = cv2.imread("Resim/eller.jpg")
x,y,z = img2.shape
roi = img1[0:x,0:y]
img2_gray = cv2.cvtColor(img2,cv2.COLOR_BGR2GRAY)
ret, mask = cv2.threshold(img2_gray,10,255,cv2.THRESH_BINARY)
mask_inv = cv2.bitwise_not(mask)
img2_bg = cv2.bitwise_and(roi,roi,mask=mask_inv)
img1_fg = cv2.bitwise_and(img2,img2,mask = mask)
toplam = cv2.add(img2_bg,img1_fg)
img1[0:x,0:y] = toplam

cv2.imshow("resim1",img2_bg)
cv2.imshow("resim2",toplam)
cv2.waitKey(0)
cv2.destroyAllWindows()

# ====================AĞIRLIKLI TOPLAMA================================================
# img1 = cv2.imread("Resim/ben.jpg")
# img2 = cv2.imread("Resim/eller.jpg")
# toplam = cv2.addWeighted(img1,0.7,img2,0.3,0)
# cv2.imshow("Resim",toplam)
# cv2.waitKey(0)
# cv2.destroyAllWindows()
# 
# =============================================================================

# ===================PİKSEL TOPLAMA==========================================
# x = np.uint8([250])
# y = np.uint8([10])
# sonuc = x+y
# sonuc2 = cv2.add(x,y)
# =============================================================================

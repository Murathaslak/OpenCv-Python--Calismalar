# -*- coding: utf-8 -*-
"""
Created on Wed Jul 14 15:01:08 2021

@author: OSMAN MURAT HAŞLAK
"""

import cv2
from matplotlib import pyplot as plt

BLUE = [255,0,0]

img1 = cv2.imread("Resim/eller.jpg")


replicate = cv2.copyMakeBorder(img1,1000,1000,1000,1000,cv2.BORDER_REPLICATE)
reflect = cv2.copyMakeBorder(img1,100,100,200,100,cv2.BORDER_REFLECT)
reflect101 = cv2.copyMakeBorder(img1,100,100,200,100,cv2.BORDER_REFLECT101)
wrap = cv2.copyMakeBorder(img1,10,10,20,10,cv2.BORDER_WRAP)
constant = cv2.copyMakeBorder(img1,10,10,20,10,cv2.BORDER_CONSTANT,value=BLUE)

plt.subplot(231)
plt.imshow(img1,"gray")
plt.title("Original")

plt.subplot(232)
plt.imshow(replicate,"gray")
plt.title("Replicate")

plt.subplot(233)
plt.imshow(reflect,"gray")
plt.title("Reflect")

plt.subplot(234)
plt.imshow(reflect101,"gray")
plt.title("Reflect_101")

plt.subplot(235)
plt.imshow(wrap,"gray")
plt.title("Wrap")

plt.subplot(236)
plt.imshow(constant,"gray")
plt.title("Constant")

plt.show()


# ==============KIRPMA İŞLEMİ========================================
# resim = cv2.imread("Resim/ben.jpg")
# kirp = resim[100:400,100:400]
# resim[100:400,200:500] = kirp
# plt.subplot(121)
# plt.imshow(resim)
# plt.subplot(122)
# plt.imshow(kirp)
# plt.show()
# =============================================================================



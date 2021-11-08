# -*- coding: utf-8 -*-
"""
Created on Mon Jul  5 12:55:29 2021

@author: OSMAN MURAT HAŞLAK
"""

import cv2
from matplotlib import pyplot as plt

resim = cv2.imread("ben.jpg",0)

cv2.namedWindow("resim",cv2.WINDOW_NORMAL)
cv2.imshow("resim",resim)
cv2.imshow("resim penceresi",resim)

plt.imshow(resim,cmap="gray")
plt.show()

k = cv2.waitKey(0)

if k == 27:
    print("ESC tuşuna basıldı")

elif k == ord("q"):
    print("q tuşuna basıldı, resim kayıt edildi.")
    cv2.imwrite("bengri.jpg",resim)

#cv2.destroyWindow("resim penceresi")
cv2.destroyAllWindows()
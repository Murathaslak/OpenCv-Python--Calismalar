# -*- coding: utf-8 -*-
"""
Created on Wed Jul  7 02:44:06 2021

@author: OSMAN MURAT HAŞLAK
"""

import cv2
import numpy as np #matris kütüphanesi

sifir = np.zeros([300,300])
bir = np.ones([300,300])

cv2.imshow("sifir",sifir)
cv2.imshow("bir",bir)

cv2.namedWindow("sifir",cv2.WINDOW_NORMAL)
cv2.namedWindow("bir",cv2.WINDOW_NORMAL)



cv2.waitKey(0)
cv2.destroyAllWindows()
# -*- coding: utf-8 -*-
"""
Created on Wed Jul  7 03:08:18 2021

@author: OSMAN MURAT HAŞLAK
"""

import cv2
cam = cv2.VideoCapture(0)
fourrc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter("arabalar.avi",fourrc,30.0,(640,480))

while cam.isOpened():
    ret, frame = cam.read()
    if not ret:
        print("Kamera çalışmıyor.")
        break
    out.write(frame)
    cv2.imshow("Kamera",frame)
    if cv2.waitKey(1) == ord("q"):
        print("Videodan çıkıldı")
        break
    
cam.release()
out.release()
cv2.destroyAllWindows()

# ====================VİDEO GÖRÜNTÜLEME================================================
# cam = cv2.VideoCapture("Video/video.avi")
# 
# while cam.isOpened():
#     
#     ret, frame = cam.read()
#     frame = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
#     
#     
#     if not ret:
#         print("Kameradan görüntü okunamıyor.")
#         break
#     
#     cv2.imshow("Goruntu",frame)
#     
#     if cv2.waitKey(1) & 0xFF == ord("q"):
#         print("Video Kapatildi.")
#         break
# 
# cam.release()
# cv2.destroyAllWindows()
# 
# =============================================================================

# ================KAMERADAN GÖRÜNTÜ ALMA=============================================
# cam = cv2.VideoCapture(0)
# 
# print(cam.get(3))
# print(cam.get(4))
# 
# cam.set(3,320)
# cam.set(4,240)
# 
# print(cam.get(3))
# print(cam.get(4))
# 
# 
# if not cam.isOpened():
#     print("Kamera tanınmadı")
#     exit()
# 
# while True:
#     ret, frame = cam.read()
#     frame = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
#     
#     
#     if not ret:
#         print("Kameradan görüntü okunamıyor")
#         break
#     
#     cv2.imshow("Kamera",frame)
#     if cv2.waitKey(1) == ord("q"):
#         print("Görüntü sonlandırıldı.")
#         break
#     
# cam.release()
# cv2.destroyAllWindows()
# =============================================================================

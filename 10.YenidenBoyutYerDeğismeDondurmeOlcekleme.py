# -*- coding: utf-8 -*-
"""
Created on Sun Jul 18 14:07:37 2021

@author: OSMAN MURAT HAŞLAK
"""

import cv2
import numpy as np

# ===================KIRPMA=========================================
# eller = cv2.imread("Resim/kitap.jpg")
# 
# print(eller.shape)
# rows,cols = eller.shape[:2]
# 
# click_count = 0
# a = []
# 
# dst_point = np.float32([
#     [0,0],
#     [cols-1,0],
#     [0,rows-1],
#     [cols-1,rows-1]])
# cv2.namedWindow("img",cv2.WINDOW_NORMAL)
# cv2.namedWindow("output",cv2.WINDOW_NORMAL)
# 
# 
# def draw(event,x,y,flags,param):
#     global click_count,a
#     if click_count <4:
#         if event == cv2.EVENT_LBUTTONDBLCLK:
#             print(click_count)
#             print(x,y)
#             click_count +=1
#             a.append((x,y))
#     else:
#         src = np.float32([
#             [a[0][0],a[0][1]],
#             [a[1][0],a[1][1]],
#             [a[2][0],a[2][1]],
#             [a[3][0],a[3][1]]])
#         
#         click_count = 0
#         a = []
#         
#         
#         M = cv2.getPerspectiveTransform(src,dst_point)
#         img_output = cv2.warpPerspective(eller,M,(cols,rows))
#         cv2.imshow("output",img_output)
#     pass
# 
# cv2.setMouseCallback("img",draw)
# 
# while(1):
#     cv2.imshow("img",eller)
#     if cv2.waitKey(1) == ord("q"):
#         break
# cv2.destroyAllWindows()
# =============================================================================

# ========================PROJECTİVE TRANSFORMATİON==================================
# eller = cv2.imread("Resim/eller.jpg")
# 
# rows,cols = eller.shape[:2]
# 
# src_point = np.float32([
#     [100,50],
#     [355,60],
#     [99,292],
#     [400,280]])
# 
# dst_point = np.float32([
#     [0,0],
#     [cols-1,0],
#     [0,rows-1],
#     [cols-1,rows-1]])
# 
# projective_matrix = cv2.getPerspectiveTransform(src_point,dst_point)
# img_output = cv2.warpPerspective(eller,projective_matrix,(cols,rows))
# 
# cv2.imshow("img_output",img_output)
# cv2.imshow("eller",eller)
# cv2.waitKey()
# cv2.destroyAllWindows()
# =============================================================================

# =========================AFFINE TRANSFORMATİON========================================
# eller = cv2.imread("Resim/eller.jpg")
# rows,cols = eller.shape[:2]
# 
# src_point = np.float32([
#     [0,0],
#     [cols-1,0],
#     [0,rows-1]])
# 
# dst_point = np.float32([
#     [0,0],
#     [int(0.6*(cols-1)),0],
#     [int(0.4*(cols-1)),rows-1]])
# 
# affine_matrix = cv2.getAffineTransform(src_point,dst_point)
# 
# imt_output = cv2.warpAffine(eller,affine_matrix,(cols,rows))
# 
# cv2.imshow("imt_output",imt_output)
# cv2.imshow("eller",eller)
# cv2.waitKey()
# cv2.destroyAllWindows()
# =============================================================================

# ===========================DÖNDÜRME===================================
# eller = cv2.imread("Resim/eller.jpg")
# rows,cols = eller.shape[:2]
# ration_matrix = cv2.getRotationMatrix2D((cols/2,rows/2),30,0.7)
# img_rotation = cv2.warpAffine(eller,ration_matrix,(cols,rows))
# cv2.imshow("img_rotation",img_rotation)
# cv2.imshow("eller",eller)
# cv2.waitKey()
# cv2.destroyAllWindows()
# =============================================================================

# ==============================YER DEĞİŞTİRME============================
# eller = cv2.imread("Resim/eller.jpg")
# rows,cols = eller.shape[:2]
# translation_matrix = np.float32([
#     [1,0,25],
#     [0,1,25]]
# img_translation = cv2.warpAffine(eller, translation_matrix,(cols+50,rows+50))
# cv2.imshow("img_translation",img_translation)
# cv2.imshow("eller",eller)
# cv2.waitKey()
# cv2.destroyAllWindows()
# =============================================================================

# ====================GÖRÜNTÜYÜ YENİDEN BOYUTLANDIRMA====================================
# eller = cv2.imread("Resim/eller.jpg")
# print(eller.shape)
# #res = cv2.resize(eller,(300,300))
# res = cv2.resize(eller,None,fx=1.4,fy=1)
# cv2.imshow("eller",eller)
# cv2.imshow("res",res)
# cv2.waitKey()
# cv2.destroyAllWindows()
# =============================================================================

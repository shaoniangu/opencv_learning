# -*-coding:utf-8-*-
# __Author__=Youzhi Gu
# Learn Python at Zhejiang University


import cv2
import numpy as np

img = cv2.imread('chess.jpg')
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
gray = np.float32(gray)
dst = cv2.cornerHarris(gray,2,23,0.04)
img[dst > 0.03 * dst.max()] = [0,0,255]
while(True):
    cv2.imshow('corners',img)
    if cv2.waitKey(int(1000/12)) & 0xff == ord('q'):
        break
cv2.destroyAllWindows()
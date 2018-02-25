# -*-coding:utf-8-*-
# __Author__=Youzhi Gu
# Learn Python at Zhejiang University


import cv2
import sys
import numpy as np

img = cv2.imread('chess.jpg')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

surf = cv2.xfeatures2d.SURF_create()
keypoints, descriptor = surf.detectAndCompute(gray,None)

img = cv2.drawKeypoints(imge=img, outImage=img, keypoints=keypoints,
                        flags=4, color=(51,163,236))

cv2.imshow('SURF', img)
while(True):
    cv2.imshow('corners', img)
    if cv2.waitKey(int(1000/12)) & 0xff == ord('q'):
        break
cv2.destroyAllWindows()

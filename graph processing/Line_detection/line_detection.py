# -*-coding:utf-8-*-
# __Author__=Youzhi Gu
# Learn Python at Zhejiang University


import cv2
import numpy as np

img = cv2.imread('lines.jpg')
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
cv2.imshow('gray',gray)
edges = cv2.Canny(gray,50,150)
cv2.imshow('canny_detection',edges)
minLineLength = 120
maxLineGap = 5

lines = cv2.HoughLinesP(edges,1,np.pi/180,118)

for x1,y1,x2,y2 in lines[0]:
    cv2.line(img,(x1,y1),(x2,y2),(0,255,0),2)

cv2.imshow('lines',img)
cv2.waitKey()
cv2.destroyAllWindows()

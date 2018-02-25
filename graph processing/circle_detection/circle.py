# -*-coding:utf-8-*-
# __Author__=Youzhi Gu
# Learn Python at Zhejiang University

import cv2
import numpy as np

planets = cv2.imread('planet.jpg')
gray = cv2.cvtColor(planets, cv2.COLOR_BGR2GRAY)
cv2.imshow('gray',gray)
img = cv2.medianBlur(gray,5)
cv2.imshow('gray_blur',img)
cimg = cv2.cvtColor(img,cv2.COLOR_GRAY2BGR)
cv2.imshow('color_blur',img)

circles = cv2.HoughCircles(img,cv2.HOUGH_GRADIENT,1,80,param1=80,param2=50,minRadius=0,maxRadius=0)
circles = np.uint16(np.around(circles))

for i in circles[0,:]:
    cv2.circle(planets,(i[0],i[1]),i[2],(0,255,0),2)
    cv2.circle(planets,(i[0],i[1]),2,(0,0,255),3)

cv2.imwrite('planets_circles.jpg',planets)
cv2.imshow('HoughCircles',planets)
cv2.waitKey()
cv2.destroyAllWindows()
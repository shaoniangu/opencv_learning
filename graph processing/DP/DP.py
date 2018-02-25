# -*-coding:utf-8-*-
# __Author__=Youzhi Gu
# Learn Python at Zhejiang University


import cv2
import numpy as np

img = cv2.pyrDown(cv2.imread('logo.jpg'),cv2.IMREAD_UNCHANGED)
ret, thresh = cv2.threshold(cv2.cvtColor(img.copy(),cv2.COLOR_BGR2GRAY),10,255,cv2.THRESH_BINARY)
cv2.imshow('thresh',thresh)

image, contours, hier = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
length = cv2.arcLength(contours[0], True)
epsilon = 0.01 * length
approx = cv2.approxPolyDP(contours[0],epsilon,True)
hull = cv2.convexHull(contours[0])

img2 = np.zeros((img.shape[0],img.shape[1]),dtype= np.uint8)
cv2.drawContours(img2,approx,-1,(255,0,0),1)
#cv2.drawContours(img2,contours,-1,(255,0,0),1)
cv2.imshow('contours',img2)
cv2.waitKey()
cv2.destroyAllWindows()

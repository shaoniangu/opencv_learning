# -*-coding:utf-8-*-
# __Author__=Youzhi Gu
# Learn Python at Zhejiang University


import  numpy as np
import cv2
from matplotlib import pyplot as plt

img1 = cv2.imread('2.png',cv2.IMREAD_GRAYSCALE)
img2 = cv2.imread('1.jpg',cv2.IMREAD_GRAYSCALE)

orb = cv2.ORB_create()
kp1,des1 = orb.detectAndCompute(img1,None)
kp2,des2 = orb.detectAndCompute(img2,None)
bf = cv2.BFMatcher(cv2.NORM_HAMMING,crossCheck = True)
matches = bf.knnMatch(des1,des2,k=2)
img3 = cv2.drawMatchesKnn(img1,kp1,img2,kp2,matches,img2,flags=2)
plt.imshow(img3)
plt.show()
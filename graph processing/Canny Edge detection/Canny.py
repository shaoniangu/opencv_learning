# -*-coding:utf-8-*-
# __Author__=Youzhi Gu
# Learn Python at Zhejiang University


import cv2
import numpy as np

img = cv2.imread('The statue of liberty.jpg',0)
edge_detected = cv2.Canny(img,100,200)
cv2.imwrite('Canny.jpg', edge_detected)
cv2.imshow('Canny edge detection', edge_detected)
cv2.waitKey()
cv2.destroyAllWindows()

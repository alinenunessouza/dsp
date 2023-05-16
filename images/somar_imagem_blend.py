# -*- coding: utf-8 -*-
"""
Created on Tue May 14 15:32:48 2019

@author: jeans
"""

import cv2

img1 = cv2.imread('lena.png')
img2 = cv2.imread('lena.png')

dst = cv2.addWeighted(img1, 0.7, img2, 0.3, 0)

cv2.imshow('dst',dst)
#cv2.waitKey(0)
#cv2.destroyAllWindows()
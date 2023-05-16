# -*- coding: utf-8 -*-
"""
Created on Mon May 13 19:47:58 2019

@author: jeans
"""

import numpy as np
import cv2

im = cv2.imread('13.png')
imgray = cv2.cvtColor(im,cv2.COLOR_BGR2GRAY)
ret,thresh = cv2.threshold(imgray,127,255,0)
image, contours, hierarchy = cv2.findContours(thresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)

img = cv2.drawContours(im, contours, -1, (0,255,0), 3)

cv2.imshow('Contornos',img)
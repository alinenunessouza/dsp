# -*- coding: utf-8 -*-
"""
Created on Tue Nov  6 20:00:35 2018

@author: Jean Schmith
"""
#Codigo para deslocar a imagem. Neste caso está deslocando para (100,50).

import numpy as np
import cv2

#Com o parametro '0' já lê a imagem em escala de cinza
img = cv2.imread('lena.jpg',0)
rows,cols = img.shape

M = np.float32([[1,0,100],[0,1,50]])
im_dst = cv2.warpAffine(img,M,(cols,rows))

cv2.imshow('img',im_dst)
cv2.waitKey(0)
cv2.destroyAllWindows()

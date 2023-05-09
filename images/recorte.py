# -*- coding: utf-8 -*-
"""
Created on Wed Nov  7 17:36:24 2018

@author: Jean Schmith
"""

import cv2
import numpy as np

img = cv2.imread("lena.jpg",0)

b,g,r = cv2.split(img)

#modelo clássico para escala de cinza
img_g = np.uint8(0.299*r + 0.587*g + 0.114*b)

#Monta o retangulo para ser o alvo do corte.
y=50
x=50
h=100
w=100

crop_img = img[y:y+h, x:x+w]
cv2.imshow("cropped", crop_img)
cv2.imshow("gray", img_g)
cv2.waitKey(0)
#cv2.destroyAllWindows()
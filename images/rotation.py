# -*- coding: utf-8 -*-
"""
Created on Tue Nov  6 20:11:18 2018

@author: Jean Schmith
"""
import numpy as np
import cv2

#Com o parametro '0' já lê a imagem em escala de cinza
img = cv2.imread('lena.jpg',0)
rows,cols = img.shape

# cols-1 e rows-1 são os limites das coordenadas. 
#Os dois primeiros parametros são o centro da imagem, ou o centro de rotação.
#O terceiro parâmetro é o angulo de rotação. O ultimo parametro é o fator de
#escala.
M = cv2.getRotationMatrix2D(((cols-1)/2.0,(rows-1)/2.0),90,1)
im_dst = cv2.warpAffine(img,M,(cols,rows))

cv2.imshow('img',im_dst)
cv2.waitKey(0)
#cv2.destroyAllWindows()
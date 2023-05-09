# -*- coding: utf-8 -*-
"""
Created on Tue Nov  6 19:39:17 2018

@author: Jean Schmith
"""

#Código para alterar a escala de uma imagem. Neste caso deixa com o dobro do tamanho.

import numpy as np
import cv2

#Ler imagem
img = cv2.imread('lena.jpg')

#Converte em escala de cinza
im_gray_image = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

#Aumenta a imagem para o dobro do tamanho
height, width = im_gray_image.shape[:2]
im_resize = cv2.resize(im_gray_image,(2*width, 2*height), interpolation = cv2.INTER_CUBIC)

#Mostra imagem
cv2.imshow('image',im_resize)

cv2.waitKey(0)
#cv2.destroyAllWindows()


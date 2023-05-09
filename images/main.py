# -*- coding: utf-8 -*-
"""
Created on Wed Nov  7 17:40:23 2018

@author: Jean Schmith
"""

import cv2
import numpy as np

im = cv2.imread('messi5.jpg')

#para acessar um pixel da imagem
px = im[100,100]
print(px)

#para acessar apenas o valor do pixel na camada azul (BGR)
blue = im[100,100,0]
print(blue)

#para acessar apenas o valor do pixel na camada verde
green = im[100,100,1]
print(green)

#para acessar apenas o valor do pixel na camada vermelha
red = im[100,100,2]
print(red)

#para alterar o valor de um pixel
im[100,100] = [255,255,255]
print(im[100,100])

#para acessar as propriedades da imagem (px, py, camadas)
print(im.shape)
# 1 camada -> escala em cinza
# 3 camadas -> colorido

#total de pixels px*py*3
print(im.size)

#tamanho de cada pixel, resolução
print(im.dtype)

#copiar e colar
ball = im[280:340, 330:390]
im[273:333, 100:160] = ball

#separar as camadas
b,g,r = cv2.split(im)

#e juntar novamente
im = cv2.merge((b,g,r))

#mostrar a imagem
cv2.imshow("Messi", im)
cv2.waitKey(0)
#cv2.destroyAllWindows()
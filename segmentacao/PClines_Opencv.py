# -*- coding: utf-8 -*-
"""
Created on Wed Oct 28 17:06:43 2020

@author: jeans
"""

import cv2
import numpy as np
from pclines import PCLines
from pclines import utils

image = cv2.imread("test.png", 0)

cv2.imshow("Input", image)

edges = cv2.Canny(image,100,200)
r,c = np.nonzero(edges > 0.5)
x = np.array([c,r],"i").T
weights = edges[r,c]
weights.shape

edges = cv2.bitwise_not(edges)

cv2.imshow("Edges", edges)

h,w = image.shape[:2]
bbox=(0,0,w,h)
d = 1024

# Create new accumulator
P = PCLines(bbox, d)

# Insert observations
P.insert(x, weights)

# Find local maxima
p, w = P.find_peaks(min_dist=10, prominence=1.3, t=0.1)

h = P.inverse(p)

X,Y = utils.line_segments_from_homogeneous(h, bbox)

color = (0,0,255)
thickness = 2
img_color = cv2.cvtColor(image, cv2.COLOR_GRAY2BGR)
for i in range(0,len(X)):
    img_color = cv2.line(img_color, (int(X[i][0]),int(Y[i][0])), (int(X[i][1]),int(Y[i][1])), color, thickness)

cv2.imshow("Saida", img_color)
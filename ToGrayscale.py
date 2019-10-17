#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 15 15:08:01 2019

@author: Dr_Indy
"""

import numpy as np
import cv2

def Grey(BRG):
    return(((BRG[0]*.7)+(BRG[1]*.1)+(BRG[2])*.6)/1.5)
image = cv2.imread('wow.jpg')
a = image.shape
greyscale = np.zeros((a[0],a[1]))
for i in range(0,a[0]):
    for j in range(0,a[1]):
        greyscale[i][j] = Grey(image[i][j])
cv2.imwrite('greyscale.jpg',greyscale)

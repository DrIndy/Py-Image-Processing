#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 15 15:08:01 2019

@author: Dr_Indy (Kai Wilson)
"""

import numpy as np

def Grey(image):
    greyscale = np.zeros((image.shape[0],image.shape[1]))
    for i in range(0,image.shape[0]):
        for j in range(0,image.shape[1]):
            greyscale[i][j] = ((image[i][j][0]*.7)+(image[i][j][1]*.1)+(image[i][j][2]*.6))//1.5
    return greyscale
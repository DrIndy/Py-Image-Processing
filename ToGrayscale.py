#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 15 15:08:01 2019

@author: Dr_Indy (Kai Wilson)
"""

import numpy as np

def Grey(image): #Begins definition for the function to turn an image to grey scale
    greyscale = np.zeros((image.shape[0],image.shape[1])) #Finds the shape of the array
    for i in range(0,image.shape[0]): #Loops through each row in the array
        for j in range(0,image.shape[1]): #Loops through each pixel in the row
            greyscale[i][j] = ((image[i][j][0]*.7)+(image[i][j][1]*.1)+(image[i][j][2]*.6))//1.5 #Takes a weighted average of the each color in the selected pixel to make it grayscale
    return greyscale #Returns the final value

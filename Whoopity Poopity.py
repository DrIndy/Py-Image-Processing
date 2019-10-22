#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''
===============================================================================
ENGR 133 Program Description 
	replace this text with your program description as a comment

Assignment Information
	Assignment:     e.g. Py1_ACT Task 1
	Author:         Name, login@purdue.edu
	Team ID:        ###-## (e.g. 001-14 for section 1 team 14)
	
Contributor:    Name, login@purdue [repeat for each]
	My contributor(s) helped me:	
	[ ] understand the assignment expectations without
		telling me how they will approach it.
	[ ] understand different ways to think about a solution
		without helping me plan my solution.
	[ ] think through the meaning of a specific error or
		bug present in my code without looking at my code.
	Note that if you helped somebody else with their code, you
	have to list that person as a contributor here as well.
===============================================================================
'''
import cv2
import numpy as np

def rot(img):
   nwImg = np.ndarray((img.shape[1],img.shape[0],img.shape[2]))
   for i in range(0, img.shape[0]):
       for j in range(0, img.shape[1]):
           nwImg[img.shape[1]-j-1][i] = img[i][j]
   return nwImg

def mirr(img):
    mirrim = np.ndarray((img.shape[1],img.shape[0],img.shape[2]))
    for i in range(0, img.shape[0]):
        for j in range(0, img.shape[1]):
            mirrim[img.shape[-1]][j] = img[i][j]

img = input("WHAT IMAGE DO YOU WISH TO DISTORT? ")
final = input("WHAT IS THE NEW NAME OF THINE CREATION WITH EXTENTION? ")
Degree = int(input("HOW FAR DO YOU WISH TO ROTATE THINE IMAGE IN DEGREES? "))
image = cv2.imread(img, 1)

if Degree == 90: image = rot(image)
elif Degree == 180: image = rot(rot(image))
elif Degree == 270: image = rot(rot(rot(image)))
else: pass


cv2.imwrite(final, image)
    

    
            
    
    
    

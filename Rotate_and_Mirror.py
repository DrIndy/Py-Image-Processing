#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''
===============================================================================
ENGR 133 Program Description 
	replace this text with your program description as a comment

Assignment Information
	Assignment:     Python Project
	Author:         Chase Weinstein, cweinste@purdue.edu
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
   nwImg = np.ndarray((img.shape[1],img.shape[0],img.shape[2])) #makes new image array
   for i in range(0, img.shape[0]): #i is the column of the array
       for j in range(0, img.shape[1]): #j is the row of the array
           nwImg[-j-1][i] = img[i][j] #trasposes the pixel into the new image
   return nwImg

def mirr(img):
   nwImg = np.ndarray(img.shape) #makes new image array
   for i in range(0, img.shape[0]): #i is the column of the array
       for j in range(0, img.shape[1]): #j is the row of the array
           nwImg[-i-1][j] = img[i][j] #trasposes the pixel into the new image
   return nwImg

'''
img = input("WHAT IMAGE DO YOU WISH TO DISTORT? ")
final = input("WHAT IS THE NEW NAME OF THINE CREATION WITH EXTENTION? ")
Distortion = input("DO YOU WISH TO MIRROR OR ROTATE YOUR IMAGE? ").lower()
image = cv2.imread(img, 1) #reads the image

if Distortion == "rotate": #checks to see if the user wants to rotate or mirror and this runs if it is mirrored
    Degree = int(input("HOW FAR DO YOU WISH TO ROTATE THINE IMAGE IN DEGREES? "))
    if Degree == 90: image = rot(image) #rotates the image 90 degrees
    elif Degree == 180: image = rot(rot(image)) #rotates the image 180 degrees
    elif Degree == 270: image = rot(rot(rot(image))) #rotates the image 270 degrees
    
elif Distortion == "mirror":
    image = mirr(image) #runs the mirror function

else:
    print("THIS COMMAND IS NOT RECOGNIZED") #runs if anything else is inputed for distortion
cv2.imwrite(final, image) #writes the new image
'''

    
            
    
    
    

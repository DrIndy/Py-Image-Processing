#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''
===============================================================================
ENGR 133 Program Description 
	Can take in an array of an image and rotate or mirror the image

Assignment Information
	Assignment:     Python Project
	Author:         Chase Weinstein, cweinste@purdue.edu
	Team ID:        004-01 (e.g. 001-14 for section 1 team 14)
	
Contributor:    
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

    

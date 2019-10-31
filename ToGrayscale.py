#!/usr/bin/env python3
'''
===============================================================================
ENGR 133 Program Description 
	Immage Processing, Greyscale

Assignment Information
	Assignment:     Python Project
	Author:         Kai Wilson, wils1064@purdue.edu
	Team ID:        004-01 (e.g. 001-14 for section 1 team 14)
	
Contributor:    
	My contributor(s) helped me:	
	[] understand the assignment expectations without
		telling me how they will approach it.
	[] understand different ways to think about a solution
		without helping me plan my solution.
	[] think through the meaning of a specific error or
		bug present in my code without looking at my code.
	Note that if you helped somebody else with their code, you
	have to list that person as a contributor here as well.
===============================================================================
'''

import numpy as np

def Grey(image): #Begins definition for the function to turn an image to grey scale
    greyscale = np.zeros((image.shape[0],image.shape[1])) #Finds the shape of the array
    for i in range(0,image.shape[0]): #Loops through each row in the array
        for j in range(0,image.shape[1]): #Loops through each pixel in the row
            greyscale[i][j] = ((image[i][j][0]*.11)+(image[i][j][1]*.59)+(image[i][j][2]*.3))  #Takes a weighted average of the each color in the selected pixel to make it grayscale
    return greyscale #Returns the final value

'''
===============================================================================
ACADEMIC INTEGRITY STATEMENT
    I have not used source code obtained from any other unauthorized
    source, either modified or unmodified. Neither have I provided
    access to my code to another. The project I am submitting
    is my own original work.
===============================================================================
'''

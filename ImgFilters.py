#!/usr/bin/env python3

'''
===============================================================================
ENGR 133 Program Description 
	Immage Processing, filters

Assignment Information
	Assignment:     Py1_ACT Check for Understanding
	Author:         Matthew Glimcher, mglimche@purdue.edu
	Team ID:        004-01 (e.g. 001-14 for section 1 team 14)
	
Contributor:    Name, login@purdue [repeat for each]
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

def ImgFltr(img, fltr = [4,9,4,9,36,9,4,9,4]):
    nwImg = np.ndarray(img.shape) # Create the new image to copy into
    b = np.ndarray((9,2)) # Create the aray of pixels to be evaluated
    smfltr = sum(fltr)
    if smfltr == 0: smfltr = 1
    for i in range(0,img.shape[0]): # Itterate through every pixel
        for j in range(0, img.shape[1]):
            try: # Copy the square around the current pixel
                b[0:3][0] = img[i-1:i+1][j-1]
                b[4:6][0] = img[i-1:i+1][j]
                b[7:9][0] = img[i-1:i+1][j+1]
            except: # fill in "Manualy" if it hits an edge
                for x in range(0,3):
                    for y in range(0,3):
                        try:    b[3*x+y][0] = img[x+i-1][y+j-1]
                        except: b[3*x+y][0] = img[i][j] # pads teh edge by copying the current pixel into the edges
            b[:,1] = fltr # add the filter weights to the aray of pixels
            s = 0
            for k in b: s += k[0]*k[1] # Multiply the pixels by the weights and sum them
            nwImg[i][j] = s//smfltr # divide by the filter sum and put the value in the new image
    return nwImg


'''
Horizontal Derivative = [-1,-2,-1,0,0,0,1,2,1]
Vertical Derivative   = [-1,0,1,-2,0,2,1,0,1]
Sharpen               = [0,-1,0,-1,5,-1,0,-1,0]

===============================================================================
ACADEMIC INTEGRITY STATEMENT
    I have not used source code obtained from any other unauthorized
    source, either modified or unmodified. Neither have I provided
    access to my code to another. The project I am submitting
    is my own original work.
===============================================================================
'''
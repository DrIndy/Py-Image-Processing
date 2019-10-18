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

def square(img, a):
    #pulls out the square around 
    b = np.ndarray((9))
    try:
        b[0:3] = img[a[0]-1:a[0]+1][a[0]-1]
        b[4:6] = img[a[0]-1:a[0]+1][a[0]]
        b[7:9] = img[a[0]-1:a[0]+1][a[0]+1]
    except:
        for i in range(0,3):
            for j in range(0,3):
                try:    b[3*i+j] = img[i+a[0]-1][j+a[1]-1]
                except: b[3*i+j] = img[a[0]][a[1]]
    return b

def ImgFltr(img, fltr = [4,9,4,9,36,9,4,9,4]):
    nwImg = np.ndarray(img.shape)
    b = np.ndarray((9,2))
    for i in range(0,img.shape[0]):
        for j in range(0, img.shape[1]):
            b[:,0], b[:,1] = square(img, (i,j)), fltr
            s = 0
            for k in b: s += k[0]*k[1]
            nwImg[i][j] = s//88
    return nwImg

def ColorFltr(img, fltr = [4,9,4,9,36,9,4,9,4]):
    img[:,:,0] = ImgFltr(img[:,:,0], fltr)
    try:
        img[:,:,1] = ImgFltr(img[:,:,1], fltr)
        img[:,:,2] = ImgFltr(img[:,:,2], fltr)
    except: pass
    return img

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
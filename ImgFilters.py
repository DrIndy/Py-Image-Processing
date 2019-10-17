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

def GausSmooth(img):
    nwImg = np.ndarray(img.shape)
    b = np.ndarray((9,2))
    for i in range(0,img.shape[0]):
        for j in range(0, img.shape[1]):
            b[:,0], b[:,1] = square(img, (i,j)), [4,9,4,9,36,9,4,9,4]
            s = 0
            for k in b: s += k[0]*k[1]
            nwImg[i][j] = s//88
    return nwImg

def colorGausSmooth(img):
    img[:,:,0] = GausSmooth(img[:,:,0])
    img[:,:,1] = GausSmooth(img[:,:,1])
    img[:,:,2] = GausSmooth(img[:,:,2])
    return img

def HorizDeriv(img):
    nwImg = np.ndarray(img.shape)
    b = np.ndarray((9,2))
    for i in range(0,img.shape[0]):
        for j in range(0, img.shape[1]):
            b[:,0], b[:,1] = square(img, (i,j)), [-1,-2,-1,0,0,0,1,2,1]
            s = 0
            for k in b: s += k[0]*k[1]
            nwImg[i][j] = s
    return nwImg

def colorHorizDeriv(img):
    img[:,:,0] = HorizDeriv(img[:,:,0])
    img[:,:,1] = HorizDeriv(img[:,:,1])
    img[:,:,2] = HorizDeriv(img[:,:,2])
    return img

def VertDeriv(img):
    nwImg = np.ndarray(img.shape)
    b = np.ndarray((9,2))
    for i in range(0,img.shape[0]):
        for j in range(0, img.shape[1]):
            b[:,0], b[:,1] = square(img, (i,j)), [-1,0,1,-2,0,2,1,0,1]
            s = 0
            for k in b: s += k[0]*k[1]
            nwImg[i][j] = s
    return nwImg

def colorVertDeriv(img):
    img[:,:,0] = VertDeriv(img[:,:,0])
    img[:,:,1] = VertDeriv(img[:,:,1])
    img[:,:,2] = VertDeriv(img[:,:,2])
    return img

def Sharp(img):
    nwImg = np.ndarray(img.shape)
    b = np.ndarray((9,2))
    for i in range(0,img.shape[0]):
        for j in range(0, img.shape[1]):
            b[:,0], b[:,1] = square(img, (i,j)), [0,-1,0,-1,5,-1,0,-1,0]
            s = 0
            for k in b: s += k[0]*k[1]
            nwImg[i][j] = s
    return nwImg

def colorSharp(img):
    img[:,:,0] = Sharp(img[:,:,0])
    img[:,:,1] = Sharp(img[:,:,1])
    img[:,:,2] = Sharp(img[:,:,2])
    return img

'''
===============================================================================
ACADEMIC INTEGRITY STATEMENT
    I have not used source code obtained from any other unauthorized
    source, either modified or unmodified. Neither have I provided
    access to my code to another. The project I am submitting
    is my own original work.
===============================================================================
'''
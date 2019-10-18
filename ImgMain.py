#!/usr/bin/env python3

'''
===============================================================================
ENGR 133 Program Description 
	Immage Processing Main Menu

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
from ImgFilters import ImgFltr
from ToGrayscale import Grey
from numpy import ndarray
import cv2

choice = 1
while True:
    if choice == 1: 
        img = cv2.imread(input("Enter the file name of the image to be procesed:\n"),1)
        if type(img) != ndarray: 
            print("\nError: File Does Not Exist\n")
            continue
    elif choice == 2:
        img = Grey(img)
        print("\nImage Conveted to Greyscale\n")
    elif choice == 3:
        theta = int(input("How many Degrees counterclockwise should the image be rotated?\n"))
        for i in range(0,round(theta/90)%4):
            pass 
            #impliment Rotation Here
    elif choice == 4:
        pass
    	#impliment Mirroring here
    elif choice == 5:
        f = int(input("Would you like to:\n1)Smooth\n2)Sharpen\n3)Take Vertical Derivative\n4)Horizontal Derivative\n"))
        if f == 1: fltr = [4,9,4,9,36,9,4,9,4]
        elif f == 2: fltr = [-1,-2,-1,0,0,0,1,2,1]
        elif f == 3: fltr = [-1,0,1,-2,0,2,1,0,1]
        elif f == 4: fltr = [0,-1,0,-1,5,-1,0,-1,0]
        else: continue
        try:
            img[:,:,0] = ImgFltr(img[:,:,0], fltr)
            img[:,:,1] = ImgFltr(img[:,:,1], fltr)
            img[:,:,2] = ImgFltr(img[:,:,2], fltr)
        except: img = ImgFltr(img, fltr)
        print("\nImage Filtered\n")
    elif choice == 6:
        try:
            cv2.imwrite(input("Enter The file name for the new image:\n"), img)
            break
        except: 
            print("\nError: Invalid File Name")
            if input("End program anyway? ([y/n]) ") == "y": break
            continue
    if choice <= 6:
        print("What do you want to do with the image?")
        print("1) Open from file \n2) Convert to Graysacle \n3) Rotate \n4) Mirror \n5) Filter \n6) Write to File")
    else: print("\nPlease enter a number from 1-6")
    while True:
        try: 
            choice = int(input())
            break
        except: print("\nPlease enter a number.")

'''
===============================================================================
ACADEMIC INTEGRITY STATEMENT
    I have not used source code obtained from any other unauthorized
    source, either modified or unmodified. Neither have I provided
    access to my code to another. The project I am submitting
    is my own original work.
===============================================================================
'''

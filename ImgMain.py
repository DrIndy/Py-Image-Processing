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
import ImgFilters as fltr
from ToGreyscale import Grey
import cv2

choice = 1
while True:
    if choice == 1: 
        try: img = cv2.imread(input("Enter the file name of the image to be procesed:\n"),1)
        except: 
            print("\nError: File Does Not Exist\n")
            continue
    elif choice == 2:
	img = Grey(img)
	print("\nImage Conveted to Greyscale\n")
    elif choice == 3:
        if img.shape[2] == 1: img = fltr.GausSmooth(img)
        else: img = fltr.colorGausSmooth(img)
	print("\nImage Smoothed\n")
    else:
	try:
		cv2.imwrite(input("Enter The file name for the new image:\n"), img)
        	break
	except: 
		print("\nError: Invalid File Name\n")
		continue
    print("What do you want to do with the image?")
    choice = int(input("1) Open from file \n2) Rotate \n3) Smooth \n5) Write to file\n"))


'''
===============================================================================
ACADEMIC INTEGRITY STATEMENT
    I have not used source code obtained from any other unauthorized
    source, either modified or unmodified. Neither have I provided
    access to my code to another. The project I am submitting
    is my own original work.
===============================================================================
'''

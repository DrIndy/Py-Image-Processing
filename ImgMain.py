#!/usr/bin/env python3

'''
===============================================================================
ENGR 133 Program Description 
	Immage Processing Main Menu

Assignment Information
	Assignment:     Python Project
	Author:         Matthew Glimcher, mglimche@purdue.edu
	Team ID:        004-01 (e.g. 001-14 for section 1 team 14)
	
Contributor:    Kai Wilson, login@purdue
                Chase Weinstien, login@purdue.edu
	My contributor(s) helped me:
	[x] understand the assignment expectations without
		telling me how they will approach it.
	[x] understand different ways to think about a solution
		without helping me plan my solution.
	[x] think through the meaning of a specific error or
		bug present in my code without looking at my code.
	Note that if you helped somebody else with their code, you
	have to list that person as a contributor here as well.
===============================================================================
'''
from ImgFilters import ImgFltr # File by Mattew Glimcher
from ToGrayscale import Grey # File by Kai Wilson
from Rotate_and_Mirror import rot, mirr # File by Chase Weinstine
from numpy import ndarray

import cv2

choice = 1 #makes sure that chosing an immage is the first part of the program
while True: #Loops thorugh the menu for multiple opperations until the image is writen to a file
    if choice == 1: # Pick an Image
        img = cv2.imread(input("Enter the file name of the image to be processed:\n"),1)
        if type(img) != ndarray: #check to make sure you actualy got an immage
            print("\nError: File Does Not Exist")
            if input("End program? ([y/n]) ") == "y": break
            continue # go back to the top and try again
    elif choice == 2: # Convert to Greyscale, nothing fancy here
        img = Grey(img)
        print("\nImage Conveted to Grayscale\n") # confirms the image was converted to greyscale
    elif choice == 3: # Rotates the image
        print("How many degrees counterclockwise should the image be rotated?\n")
        while True:
            try:
                r = round(int(input())/90)%4 # Take an input in degrees and records the numbe of 90 degree rotations required
                break
            except: print("\nPlease enter a number:")
        #takes a rotation value and rounds in case you hit a nearby key by accident
        if r == 1: img = rot(img)
        elif r == 2: img = rot(rot(img))
        elif r == 3: img = rot(rot(rot(img)))
        print(f"\nImage Rotated {r*90} degrees\n") # Tells you how far the image was rotated as confirmation
    elif choice == 4: #Mirrors the Image Verticaly
        img = mirr(img)
        print("\nImage Mirrored\n") # Confirms the Image was Mirrored
    elif choice == 5: #Filters the Image
        print("Would you like to:\n1)Smooth\n2)Sharpen\n3)Take Vertical Derivative\n4)Horizontal Derivative")
        while True:
            try:
                f = int(input())
                break
            except: print("\nPlease enter a number")
        if f == 1: fltr = [4,9,4,9,36,9,4,9,4] # Gausian Smoothing Filter
        elif f == 2: fltr = [0,-1,0,-1,12,-1,0,-1,0] # Sharpening Filter
        elif f == 3: fltr = [-1,0,1,-2,0,2,1,0,1] # Vertical Derivative Filter
        elif f == 4: fltr = [-1,-2,-1,0,0,0,1,2,1] # Horizontal Derivative Filter
        else: 
            print("\nPlease enter a number from 1-4")
            continue # Go back to the top and try again
        try: # Try filtering a color image, throws an error it its greyscale becasue grayscale is only 2 dimentional
            img[:,:,0] = ImgFltr(img[:,:,0], fltr) # Blue Layer
            img[:,:,1] = ImgFltr(img[:,:,1], fltr) # Green Layer
            img[:,:,2] = ImgFltr(img[:,:,2], fltr) # Red Layer
        except: img = ImgFltr(img, fltr) # if its greyscale, do this instead
        print("\nImage Filtered\n") # Confirms the Image was Filtered
    elif choice == 6: # write the image to a file
        try:
            cv2.imwrite(input("Enter The file name for the new image:\n"), img)
            break # Ends the program if the image writes sucessfuly
        except: 
            print("\nError: Invalid File Name") # yells at you if the file name is invalid
            if input("End program anyway? ([y/n]) ") == "y": break # Does exactly what it says
            continue # Go back to the top and try again
    if choice <= 6: # asks you what you want to do next if you previous choice was valid
        print("What do you want to do with the image?")
        print("1) Open from file \n2) Convert to Graysacle \n3) Rotate \n4) Mirror \n5) Filter \n6) Write to File")
    else: 
        if input("End program? ([y/n]) ") == "y": break
        print("\nPlease enter a number from 1-6")
    while True:
        try: 
            choice = int(input()) # takes in the user's choice
            break # breaks out of the input loop if the user gives a number
        except: print("\nPlease enter a number.") # yells at you if you don't give it a number

'''
===============================================================================
ACADEMIC INTEGRITY STATEMENT
    I have not used source code obtained from any other unauthorized
    source, either modified or unmodified. Neither have I provided
    access to my code to another. The project I am submitting
    is my own original work.
===============================================================================
'''

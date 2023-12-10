# -*- coding: utf-8 -*-
"""
Created on Sun Dec  3 17:05:49 2023

@author: saoba
"""
import numpy as np
import random as ran
from opencv-python import cv2
from PIL import Image

 
path = r'C:/Users/saoba/OneDrive/Desktop/New folder/image1.jpg'
image = cv2.imread(path) 
image1 = Image.open(path)
print (image1.width)
print (image1.height)

m = ran.randint(1,50)

s1, s2= 100 , 150
e1, e2= 300+s1+m ,100+s2+2*m
# Creating a black screen image using numpy.zeros function 
Img = np.zeros((400, 400, 3), dtype='uint8') 
# Start coordinate, here (100, 100). It represents the top left corner of image 
start_point = (s1, s2) 
# End coordinate, here (450, 450). It represents the bottom right corner of the image according to resolution 
end_point = (e1, e2) 
# White color in BGR 
color = (0, 0, 255) 
# Line thickness of 9 px 
thickness = 5
# Using cv2.line() method to draw a diagonal green line with thickness of 9 px 
image = cv2.line(image, start_point, end_point, color, thickness) 
# Display the image 
cv2.imshow('Drawing_Line', image) 
cv2.waitKey(0) 
cv2.destroyAllWindows() 

 

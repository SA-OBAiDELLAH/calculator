
import streamlit as st
import numpy as np
import math as m

import PIL as pil
import cv2 
from PIL import Image
st.write ("""# Syndromic Craniosynostosis""")

#st.sidebar.header('input')
col1, col2= st.columns([1,3])
#angle1=st.sidebar.number_input("X",value=float())
#angle2=st.sidebar.number_input("X",value=float())
#angle3=st.sidebar.number_input("X",value=float())
#angle4=st.sidebar.number_input("X",value=float())
#angle5=st.sidebar.number_input("X",value=float())
#angle6=st.sidebar.number_input("X",value=float())

col1.subheader('Input')
#col1.write('Right Canal')
SN=col1.number_input("SN",value=float(0))
SBa=col1.number_input("SBa",value=float(0))


#col1.write('Right Canal')
#H_OS_L=col1.number_input("H.OS.L",value=float())
#Perimeter_L=col1.number_input("Perimeter.L",value=float())
#Q3=col1.number_input("Q3",value=float())

def NBa():
    y=-1.554+1.021*SN+.753*SBa
   
    return y

def ZMR_ZML():
    y=5.762+0.920*NBa()
    
    return y

col2.subheader(' The probability of Diagnosis',)
col2.write("###### ZMR-ZML")
col2.write(ZMR_ZML())

s1, s2 = 100, 150

e1, e2 = s1+ZMR_ZML() , s2+ZMR_ZML()
 

path = r'C:/Users/saoba/OneDrive/Desktop/New folder/image1.jpg'
image = cv2.imread(path) 
image1 = Image.open(path)
print (image1.width)
print (image1.height)

# Creating a black screen image using numpy.zeros function 
Img = np.zeros((400, 400, 3), dtype='uint8') 
# Start coordinate, here (100, 100). It represents the top left corner of image 
start_point = (100, 100) 
# End coordinate, here (450, 450). It represents the bottom right corner of the image according to resolution 
end_point = (400, 280) 
# White color in BGR 
color = (255, 0, 0) 
# Line thickness of 9 px 
thickness = 5
# Using cv2.line() method to draw a diagonal green line with thickness of 9 px 
image1 = cv2.line(image, start_point, end_point, color, thickness) 
# Display the image 
#cv2.imshow('Drawing_Line', image) 
cv2.waitKey(0) 
cv2.destroyAllWindows()

img = pil.Image.open('image.jpg')
img1 = pil.Image.open('image1.jpg')

#path = r'C:/Users/saoba/OneDrive/Desktop/New folder/image1.jpg'
#image = cv2.imread(path) 

#col2.image(img, caption='CT Scan for Skull')
col2.image(image1, caption='CT Scan for Skull')




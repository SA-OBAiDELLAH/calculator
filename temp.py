import streamlit as st
import numpy as np
import math as m
import PIL as pil 
import cv2 
#from PIL import Image
st.write ("""# Syndromic Craniosynostosis""")
#st.sidebar.header('input')
col1, col2= st.columns([1,3])

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
myimage = cv2.imread(path) 

start_point = (100, 100) 
# End coordinate, here (450, 450). It represents the bottom right corner of the image according to resolution 
end_point = (400, 280) 
# White color in BGR 
color = (255, 0, 0) 
# Line thickness of 9 px 
thickness = 5
# Using cv2.line() method to draw a diagonal green line with thickness of 9 px 
myimage = cv2.line(myimage, start_point, end_point, color, thickness)

#col2.image(img, caption='CT Scan for Skull')
col2.image(myimage, caption='CT Scan for Skull')
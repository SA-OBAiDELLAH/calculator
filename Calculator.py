import streamlit as st
import numpy as np
import math as m
import PIL as pil 
import cv2 
#from PIL import Image
st.write ("""# Syndromic Craniosynostosis""")
#st.sidebar.header('input')
col1, col2= st.columns([1,3])

def fNBa(X,Y):
    y=-1.554+1.021*X+.753*Y
    return y

def ZMR_ZML(Z):
    y=5.762+0.920*Z   
    return y

col1.subheader('Input')
SN=5 #col1.number_input("SN",value=None)
SBa=col1.number_input("SBa",value=None)

if SN==None and SBa==None :
    NBa=col1.number_input("NBa",value=None)

ZML_ZMR=col1.number_input("ZML-ZMR",value=None)

if SN==None and SBa==None and NBa==None or ZML_ZMR==None :
 col2.markdown( "### :red[Please Enter the Patient's Measurments]")
elif SN!=None and SBa!=None and ZML_ZMR!=None :
    
    col1.write("NBa")
    col1.write(fNBa(SN,SBa))

    col2.subheader(' The Diagnosis',)
    col2.write("###### Expected ZMR-ZML")
    col2.write(ZMR_ZML(fNBa(SN,SBa)))
    col2.write("The Volume of Movment is")
    col2.write(ZMR_ZML(fNBa(SN,SBa))-ZML_ZMR)

    s1, s2 = 100, 150
    e1, e2 = s1+ZMR_ZML(fNBa(SN,SBa)) , s2+ZMR_ZML(fNBa(SN,SBa))
    
    path = r'C:/Users/saoba/OneDrive/Desktop/New folder/image1.jpg'
    myimage = cv2.imread(path) 
    image1 = cv2.imread(path)

    start_point = (100, 100) 
    # End coordinate, here (450, 450). It represents the bottom right corner of the image according to resolution 
    end_point = (400, 280) 
    # White color in BGR 
    color = (255, 0, 0) 
    # Line thickness of 9 px 
    thickness = 5
    # Using cv2.line() method to draw a diagonal green line with thickness of 9 px 
    myimage = cv2.line(myimage, start_point, end_point, color, thickness)

    if ZMR_ZML(fNBa(SN,SBa)) < 4.35 :
        col2.image(image1, caption='CT Scan for Skull')
    elif ZMR_ZML(fNBa(SN,SBa)) > 4.35 :
        col2.image(myimage, caption='CT Scan for Skull')
elif ZML_ZMR!=None and NBa!=None :
    col2.subheader(' The Diagnosis',)
    col2.write("###### Expected ZMR-ZML")
    col2.write(ZMR_ZML(NBa))
    col2.write("The Volume of Movment is")
    col2.write(ZMR_ZML(NBa)-ZML_ZMR)

    s1, s2 = 100, 150
    e1, e2 = s1+ZMR_ZML(NBa) , s2+ZMR_ZML(NBa)
    
    path = r'C:/Users/saoba/OneDrive/Desktop/New folder/image1.jpg'
    myimage = cv2.imread(path) 
    image1 = cv2.imread(path)

    start_point = (100, 100) 
    # End coordinate, here (450, 450). It represents the bottom right corner of the image according to resolution 
    end_point = (400, 280) 
    # White color in BGR 
    color = (255, 0, 0) 
    # Line thickness of 9 px 
    thickness = 5
    # Using cv2.line() method to draw a diagonal green line with thickness of 9 px 
    myimage = cv2.line(myimage, start_point, end_point, color, thickness)

    if ZMR_ZML(NBa) < 4.35 :
        col2.image(image1, caption='CT Scan for Skull')
    elif ZMR_ZML(NBa) > 4.35 :
        col2.image(myimage, caption='CT Scan for Skull')

# -*- coding: utf-8 -*-
"""
Created on Sun May 11 15:52:05 2025

@author: Anushka
"""

import cv2
import matplotlib.pyplot as plt
import os

ip="C:\Python_related\Image_Processing\RadheKrishna'.jpg"
op="C:\Python_related\Image_Processing\OpenCV"


#Read image
#Loads the image into memory as a NumPy array (in BGR format by default in OpenCV)
image=cv2.imread(ip)


#Show img
#Converts BGR image (OpenCV format) to RGB (Matplotlib format)
image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

plt.imshow(image_rgb)
plt.title("Original Image")
plt.axis('off')
plt.show()

#Save img with new name
cv2.imwrite(os.path.join(op,"new_img.jpg"),image)

#Resize image
resized_img=cv2.resize(image,(300,300))
cv2.imwrite(os.path.join(op,"resized.jpg"),resized_img)

#Flip image

#Horizontally(1)
flip_img=cv2.flip(image,1)
cv2.imwrite(os.path.join(op,"flipH.jpg"),flip_img)
#Verticall(0)
flip_img1=cv2.flip(image,0)
cv2.imwrite(os.path.join(op,"flipV.jpg"),flip_img1)
#Both(-1)
flip_img2=cv2.flip(image,-1)
cv2.imwrite(os.path.join(op,"flipBoth.jpg"),flip_img2)


#Crop img

crop=image[0:1000,0:1920] #[y1:y2,x1:x2]
cv2.imwrite(os.path.join(op,"crop.jpg"),crop)

#Grayscale
gray_img=cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
cv2.imwrite(os.path.join(op,"gray.jpg"),gray_img)

#Enhance
alpha=1.5 #contrast factor
beta=0    #brightness
enhanced_image = cv2.convertScaleAbs(image, alpha=alpha, beta=beta)

cv2.imwrite(os.path.join(op,"easy_enhanced_image.jpg"), enhanced_image)
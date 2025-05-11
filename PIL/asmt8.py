# -*- coding: utf-8 -*-
"""
Created on Sun May 11 11:42:44 2025

@author: Anushka
"""

#Image Processing using PIL

# =============================================================================
# Image: Main class from Pillow used to open, manipulate, and save images.
# 
# ImageEnhance: Module to adjust properties like contrast, brightness, sharpness, etc.
# 
# os: commonly used for file paths or directory operations.
# =============================================================================
from PIL import Image,ImageEnhance
import os
ip="C:\Python_related\Image_Processing\RadheKrishna'.jpg"
op="C:\Python_related\Image_Processing\PIL"
#Read an image

image=Image.open(ip)

# Display an image
image.show()
 
 
 #Save img
 #os.path.join(): safely joins directory and file names into a valid file path
image.save(os.path.join(op,"RK.jpg"))


#Resize img
#width * height (can we do it with pixels)

resized_img=image.resize((600,300))
resized_img.save(os.path.join(op,"resized1.jpg"))


#Flip img

flip_img=image.transpose(Image.FLIP_LEFT_RIGHT)
flip_img.save(os.path.join(op,"flipH.jpg"))

flip_img1=image.transpose(Image.FLIP_TOP_BOTTOM)
flip_img1.save(os.path.join(op,"flipv.jpg"))

flip_img2=flip_img.transpose(Image.FLIP_TOP_BOTTOM)
flip_img2.save(os.path.join(op,"FLIPHV.jpg"))

#Crop img

crop_box=(0,0,1920,1000) #Origin is at top left corner (left,top,right,bottom) in pixels
cropped_img=image.crop(crop_box)
cropped_img.save(os.path.join(op,"cropImg.jpg"))

#Gray img
#L --> Luminance
g_img=image.convert("L")
g_img.save(os.path.join(op,"Gray.jpg"))

#Enhance contrast
enhancer=ImageEnhance.Contrast(image)
enhance_img=enhancer.enhance(1.5)
enhance_img.save(os.path.join(op,"EnhancedImg.jpg"))
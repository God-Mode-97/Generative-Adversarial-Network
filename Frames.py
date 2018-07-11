# -*- coding: utf-8 -*-
"""
Created on Mon Jun 25 01:41:28 2018

@author: AKASH
"""
#from skimage.color import rgb2gray
#from skimage.io import imread, imsave
#from skimage.filters import threshold_otsu
#from skimage import img_as_uint
import cv2
#import glob

#for filename in glob.glob(r"C:/Users/AKASH/Display/*.jpg"):
for i in range(0, 1419):
    image = cv2.imread('frame%d.jpg' % i )
    image = cv2.cvtColor( image, cv2.COLOR_RGB2GRAY )
    j = i + 11239
    cv2.imwrite( "grey%d.png" % j, image )
    
import cv2

#get current working directory for faster traversal in files
import os
cwd = os.getcwd()

# custom local implementation of cv2_imshow (show an image until any key is pressed)
def local_cv2_imshow(window_name, image):
    cv2.imshow(window_name, image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

# open and show an image
image = cv2.imread(cwd + '/images/elon_musk_tesla.png')
local_cv2_imshow('My Image', image)

# resize the image
(iH, iW) = image.shape[:2]
resized = cv2.resize(image, (100, 100), interpolation=cv2.INTER_AREA)
local_cv2_imshow('Resized Image', resized)

# resize the image while keeping same aspect ratio
ratio = 250.0 / iW
dimension = (250, int(iH * ratio))
resized_with_ratio = cv2.resize(image, dimension, interpolation=cv2.INTER_AREA) 
local_cv2_imshow("Resized with correct aspect ratio", resized_with_ratio)
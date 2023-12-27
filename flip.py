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
image = cv2.imread(cwd + '/images/pytorch.png')
local_cv2_imshow('My Image', image)

# flip horizontally 
h_flip = cv2.flip(image, 1)
local_cv2_imshow('My Image horizontally flipped', h_flip)

# flip vertically
v_flip = cv2.flip(image, 0)
local_cv2_imshow('My Image vertically flipped', v_flip)

# flip on both axes
hv_flip = cv2.flip(image, -1)
local_cv2_imshow('My Image horizontally & vertically flipped', hv_flip)
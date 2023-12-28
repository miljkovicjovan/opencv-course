import cv2
import numpy as np

#get current working directory for faster traversal in files
import os
cwd = os.getcwd()

# custom local implementation of cv2_imshow (show an image until any key is pressed)
def local_cv2_imshow(window_name, image):
    cv2.imshow(window_name, image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

# open and show an image
image = cv2.imread(cwd + '/images/univerzitet_singidunum.jpg')
local_cv2_imshow('My Image', image)

# height, with
(iH, iW) = image.shape[:2]

# center of X and Y
cX, cY = (iW // 2, iH // 2)

# rotate image 90 degrees counter clockwise from the center
M = cv2.getRotationMatrix2D(center=(cX,cY), angle=90, scale=1.0)
rotateImage = cv2.warpAffine(image, M, (iW, iH))
local_cv2_imshow("Rotated image", rotateImage)


# function to properly rotate the image without cropping the image
def rotate_image(image, angle):

    # get the dimension of the image
    (iH, iW) = image.shape[:2]
    (cX, cY) = (iW // 2, iH // 2)

    # get the rotation matrix and then extract the sine and cosine values
    M = cv2.getRotationMatrix2D(center=(cX, cY), angle=-angle, scale=1.0)
    cosine = np.abs(M[0, 0])
    sine = np.abs(M[0,1])

    # compute the new image size
    new_width = int((iH * sine) + (iW * cosine))
    new_height = int((iH * cosine) + (iW * sine))

    # locate the translation that moves the image to the center 
    # and update it within the rotation matrix
    M[0, 2] += (new_width / 2) - cX
    M[1, 2] += (new_height / 2) - cY

    # perform the proper rotation of the image
    image = cv2.warpAffine(image, M, (new_width, new_height))
    return image

rotatedImage = rotate_image(image, 50)     
local_cv2_imshow("Correct rotation without cropping the image", rotatedImage)
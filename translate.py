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
image = cv2.imread(cwd + '/images/elon_musk_tesla.png')
local_cv2_imshow('My Image', image)

# create the translation matrix
M = np.float32([
    [1, 0, 150],
    [0, 1, 50]
])

# translate the image
(iH, iW) = image.shape[:2]
shifted = cv2.warpAffine(image, M, (iW, iH))
local_cv2_imshow('Shifted Image', shifted)
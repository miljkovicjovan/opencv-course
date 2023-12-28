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
image = cv2.imread(cwd + '/images/char_a.png')
local_cv2_imshow('My Image', image)

(iH, iW) = image.shape[:2]

interpolation_methods = [
    ['cv2. INTER_NEAREST', cv2.INTER_NEAREST], 
    ['cv2. INTER_LINEAR', cv2.INTER_LINEAR], 
    ['cv2. INTER_AREA', cv2.INTER_AREA],
    ['cv2. INTER_CUBUIC', cv2.INTER_CUBIC], 
    ['cv2. INTER_LANCZOS4', cv2.INTER_LANCZOS4]
]

# resize image function
def resize_image(image, width=None, height=None, inter=cv2.INTER_AREA):
    if width is None and height is None:
        return image
    
    dimension = None
    (h, w) = image.shape[:2]

    if height is not None:
        ratio = height / float(h)
        dimension = (int(w * ratio), height)
    else:
        ratio = width / float(w)
        dimension = (width, int(h * ratio))

    resized_image = cv2.resize(image, dimension, interpolation=inter)
    return resized_image

for (inter_name, method) in interpolation_methods:
    resizeImage = resize_image(image, width=iW*7, inter=method)
    local_cv2_imshow(f"Image resized using {inter_name} interpolation", resizeImage)
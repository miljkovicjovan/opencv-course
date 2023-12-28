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
image = cv2.imread(cwd + '/images-2/messi.png')
local_cv2_imshow('My Image', image)

list_kernel_size = [(3, 3), (5, 5), (7, 7), (9, 9), (21, 21), (33, 33)]

# Average Blur (best image: coins.png) 
def average_blur():
    for (kernelX, kernelY) in list_kernel_size:
        blur = cv2.blur(image, (kernelX,kernelY))
        local_cv2_imshow('blurred', blur)
#average_blur()

# Gaussian Blur (best image: coins.png) 
def gaussian_blur():
    for (kernelX, kernelY) in list_kernel_size:
        blur = cv2.GaussianBlur(image, (kernelX, kernelY), 0)
        local_cv2_imshow('blurred', blur)
#gaussian_blur()

# Median Blur (best image: magazine.jpg) 
def median_blur():
    for (kernelSize) in [3, 5, 9, 15]:
        blur = cv2.medianBlur(image, kernelSize)
        local_cv2_imshow('blurred', blur)
#median_blur()
        
# Biratelar filter
bilateralParams = [
    (11, 7, 7),
    (11, 21, 7), 
    (11, 41, 21),
    (11, 61, 39)
]

# Bilateral Blur
# Biratelar filter
bilateralParams = [
    (11, 7, 7),
    (11, 21, 7), 
    (11, 41, 21),
    (11, 61, 39)
]

def bilateral_blur():
    for (diameter, sigmaColor, sigmaSpace) in bilateralParams:
        blur = cv2.bilateralFilter(image, d=diameter, sigmaColor=sigmaColor, sigmaSpace=sigmaSpace)
        local_cv2_imshow("blurred", blur)
bilateral_blur()
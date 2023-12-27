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

# each pixel
print(image)

# height, with, no of channel
(iH, iW, iC) = image.shape[:3]

print(f"Height: {iH} pixels")
print(f"Width: {iW} pixels")
print(f"Number of channel: {iC}")

# accessing the center pixel of the image
(cX, cY) = (iW // 2, iH // 2)
print(f"Center pixel: {image[cY, cX]}")
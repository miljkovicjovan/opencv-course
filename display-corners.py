import cv2

#get current working directory for faster traversal in files
import os
cwd = os.getcwd()

# custom local implementation of cv2_imshow (show an image until any key is pressed)
def local_cv2_imshow(window_name, image):
    cv2.imshow(window_name, image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

# load the image
image = cv2.imread(cwd + '/images/psp.jpg')

# getting the center pixel of the image
(iH, iW) = image.shape[:2]
(cX, cY) = (iW // 2, iH // 2)

# top left corner of the image
local_cv2_imshow("Image top left", image[0:cY, 0:cX])

# top right corner of the image
local_cv2_imshow("Image top left", image[0:cY, cX:])

# bottom left corner of the image
local_cv2_imshow("Image top left", image[cY:, 0:cX])

# bottom right corner of the image
local_cv2_imshow("Image top left", image[cY:, cX:])
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

# overwrite bottom right corner and turn it all black
image[cY:iH, cX:iW] = 0
local_cv2_imshow("Image with blacked out bottom right corner", image)

# overwrite bottom right corner and turn it all red
image[cY:iH, cX:iW] = [0, 0, 255]
local_cv2_imshow("Image with blacked out bottom right corner", image)

# freestyle :)
image[cY:iH, cX:iW] = [45, 54, 34]
image[0:cY, 0:cX] = [255,23,43]
local_cv2_imshow("Image with blacked out bottom right corner", image)
import cv2
from matplotlib import pyplot as plt

#get current working directory for faster traversal in files
import os
cwd = os.getcwd()

# custom local implementation of cv2_imshow (show an image until any key is pressed)
def local_cv2_imshow(window_name, image):
    cv2.imshow(window_name, image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

# open and show an image
image = cv2.imread(cwd + '/images/rgb_circles.png')
local_cv2_imshow('My Image', image)

# split channels
(b, g, r) = cv2.split(image)

# display blue channel
plt.imshow(g)
plt.show()
import cv2

#get current working directory for faster traversal in files
import os
cwd = os.getcwd()

# custom local implementation of cv2_imshow (show an image until any key is pressed)
def local_cv2_imshow(window_name, image):
    cv2.imshow(window_name, image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

# load an image
image = cv2.imread(cwd + '/images/5-people.jpg')
print(image.shape)
local_cv2_imshow('all people', image)
local_cv2_imshow('first person', image[:, :360])
local_cv2_imshow('second person', image[:, 360:540])
local_cv2_imshow('third person', image[:, 540:740])
local_cv2_imshow('fourth person', image[:300, 740:])
local_cv2_imshow('fifth person', image[180:, 740:])
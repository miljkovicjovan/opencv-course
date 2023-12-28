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

def all_examples_on_shapes():
    # draw a square
    square = np.zeros((200, 200), dtype='uint8')
    cv2.rectangle(square, (15, 15), (185, 185), 255, -1)
    local_cv2_imshow("my square", square)

    # draw a circle
    circle = np.zeros((200, 200), dtype='uint8')
    cv2.circle(circle, (100, 100), 95, 255, -1)
    local_cv2_imshow("my circle", circle)

    # bitwise AND
    bitwiseAnd = cv2.bitwise_and(square, circle)
    local_cv2_imshow("Bitwise AND on square and circle", bitwiseAnd)

    # bitwise OR
    bitwiseOr = cv2.bitwise_or(square, circle)
    local_cv2_imshow("Bitwise OR on square and circle", bitwiseOr)

    # bitwise XOR
    bitwiseXor = cv2.bitwise_xor(square, circle)
    local_cv2_imshow("Bitwise XOR on square and circle", bitwiseXor)

    # bitwise NOT
    bitwiseNot = cv2.bitwise_not(circle)
    local_cv2_imshow("Bitwise NOT on square and circle", bitwiseNot)

# TO SHOW ALL EXAMPLES UNCOMMENT LINE BELOW
#all_examples_on_shapes()

# open and show an image
image = cv2.imread(cwd + '/images/elon_musk_tesla.png')
local_cv2_imshow('My Image', image)

rectangularMask = np.zeros(image.shape[:2], dtype='uint8')
cv2.rectangle(rectangularMask, (65, 1), (256, 537), 255, -1)
local_cv2_imshow("rectangular mask", rectangularMask)

bodyMasked = cv2.bitwise_and(image, image, mask=rectangularMask)
local_cv2_imshow("elon masked", bodyMasked)
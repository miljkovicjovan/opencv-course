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
image = cv2.imread(cwd + '/images/elon_musk_tesla.png')

# draw a rectangle over Elon
cv2.rectangle(image, (65, 1), (265, 537), (0, 255, 0), 2)

# draw a rectangle over the Tesla
cv2.rectangle(image, (227, 212), (825, 430), (0, 0, 255), 2)

# writing labels on the image
image = cv2.putText(image, 'X CEO', (269, 20), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 255, 0))
image = cv2.putText(image, 'X CEO\'s car', (680, 200), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 0, 255))

# drawing circles
cv2.circle(image, (146, 38), 5, (0, 255, 0), 2)
cv2.circle(image, (164, 36), 5, (0, 255, 0), 2)
cv2.circle(image, (156, 60), 10, (0, 255, 0), 2)

local_cv2_imshow("Image", image)


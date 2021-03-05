'''
PART A - 90 degree counterclockwise image display
'''
import sys
import cv2

image = cv2.imread(cv2.samples.findFile('CAT_Kitten_img_07.jpg'))
#image = cv2.imread(cv2.samples.findFile('/Users/jigyasasingh/Desktop/CSCI 731/assign 1/Kitten_in_02.jpg'))
if image is None:
    sys.exit('file not found')
else:
    rotated_image = cv2.rotate(image, cv2.ROTATE_90_COUNTERCLOCKWISE)
    cv2.imshow('Rotated Image', rotated_image)
cv2.waitKey(0)
cv2.destroyAllWindows()

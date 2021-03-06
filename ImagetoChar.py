import cv2
from numpy import asarray
from PIL import Image
'''Written By Evan Pfeffer'''
'''This works best with simple pictures without a lot of excess lines'''

regular_image_path = input("Please input file path for jpg photo: ")
outline = input("Please input value to substitute outline: ")
not_outline = input("Please input value to substitute everything beside the outline: ")

img = cv2.imread(regular_image_path)
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
edged = cv2.Canny(gray, 30, 200)
cv2.waitKey(0)
contours, hierarchy = cv2.findContours(edged,
                                       cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
black_contour = cv2.drawContours(img, contours, -1, (0, 255, 0), 3)
cv2.imwrite('test_outline2.jpg', edged)
img = Image.open('test_outline2.jpg')
array1 = asarray(img)

start = 0
for i in range(0, len(array1), 5):
    start2 = 0
    Output = ''
    for x in range(0, len(array1[i]), 5):
        chunk5x5 = array1[start:i+1, start2:x+1]
        chunk5x5 = chunk5x5.flatten()
        if len(chunk5x5) != 0 and sum(chunk5x5) >= 255:
            Output += str(outline)
        else:
            Output += str(not_outline)
        start2 = x
    start = i
    print(Output)


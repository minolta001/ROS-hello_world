import cv2
import numpy as np
import csv

# read image
img = cv2.imread('Umass.png')
tmp = img[::-1,:,:]
img = tmp

# convert to grayscale
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

# threshold and invert so hexagon is white on black background
thresh = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY+cv2.THRESH_OTSU)[1]
thresh = 255 - thresh

# get contours
result = np.zeros_like(img)
contours = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
contours = contours[0] if len(contours) == 2 else contours[1]
cntr = contours[0]
cv2.drawContours(result, [cntr], 0, (255,255,255), 1)

# print number of points along contour
print('number of points: ',len(cntr))

# list contour points
#for pt in cntr:

with open('result_flip.csv', 'w', newline='') as file:
    header = ['x', 'y']
    writer = csv.DictWriter(file, fieldnames=header)
    writer.writeheader()
    for pt in cntr:
        writer.writerow({'x':pt[0,0],
               'y':pt[0,1]
        })

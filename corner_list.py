import cv2
import numpy as np
import csv
from matplotlib import pyplot as plt

importedImage = 'Umass.png'
img = cv2.imread(importedImage)
tmp = cv2.flip(img, 0)
img = tmp

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

corners = cv2.goodFeaturesToTrack(gray, 27, 0.01, 10)
corners = np.int0(corners)

for i in corners:
    x, y = i.ravel()
    cv2.circle(img, (x, y), 4, 200, -1)

with open('result_corner.csv', 'w', newline='') as file:
    header = ['x', 'y']
    writer = csv.DictWriter(file, fieldnames=header)
    writer.writeheader()
    for corner in corners:
        writer.writerow({'x':corner[0,0],
               'y':corner[0,1]
        })

plt.figure(figsize=(10,10))
plt.imshow(img)
plt.show()
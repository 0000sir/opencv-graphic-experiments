import cv2
import numpy as np
import random

img = cv2.imread('../road.jpg') # As default, cv reads image as BGR colors
#img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB) # convert to RGB colors
cv2.imshow('img', img)

height, width = img.shape[:2]

img0 = np.zeros((height, width, 3), np.uint8)

for i in range(0, 300):
  x = random.randint(1, width-1)
  color = random.randint(0, 2)
  for y in range(0, height-1):
    p = img[y, x]
    img0[y,x][color] = p[color]

cv2.imshow('img-0', img0)

cv2.waitKey(0)
cv2.destroyAllWindows()
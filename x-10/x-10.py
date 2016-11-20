import cv2
import numpy as np

img = cv2.imread('../road.jpg')
cv2.imshow('img', img)


height, width = img.shape[:2]

img0 = np.zeros((height, width, 3), np.uint8)

for x in range(0, width-1):
  for y in range(0, height-1):
    if(x%2 == 0):
      img0[y, x] = img[y, x+1]
    else:
      img0[y, x] = img[y, x-1]

cv2.imshow('img-0', img0)

print img[100,0]
print img0[100,1]

cv2.waitKey(0)
cv2.destroyAllWindows()
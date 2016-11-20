import cv2
import numpy as np

img = cv2.imread('../road.jpg') # As default, cv reads image as BGR colors
#img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB) # convert to RGB colors
cv2.imshow('img', img)

height, width = img.shape[:2]

img0 = np.zeros((height, width, 3), np.uint8)

for y in range(0, height-1):
  x = 0
  while(x < width-3): 
    p1 = img[y, x]
    p2 = img[y, x+1]
    p3 = img[y, x+2]
    r1, g1, b1 = p1[2], p1[1], p1[0]
    r2, g2, b2 = p2[2], p2[1], p2[0]
    r3, g3, b3 = p3[2], p3[1], p3[0]
    # set as BGR
    img0[y, x] = [b1, g2, r3]
    img0[y, x+1] = [b3, g1, r2]
    img0[y, x+2] = [b2, g3, r1]
    x+=3

print img[100,0]
print img[100,1]
print img[100,2]

print img0[100, 0]
print img0[100, 1]
print img0[100, 2]


cv2.imshow('img-0', img0)

cv2.waitKey(0)
cv2.destroyAllWindows()
import cv2
import numpy as np

img = cv2.imread('../people.jpg') # As default, cv reads image as BGR colors
#img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB) # convert to RGB colors
cv2.imshow('img', img)

height, width = img.shape[:2]

img0 = np.zeros((height, width, 3), np.uint8)

red_pixels = []
green_pixels = []
blue_pixels = []

for y in range(0, height-1):
  for x in range(0, width-1): 
    p1 = img[y, x]
    #r1, g1, b1 = p1[2], p1[1], p1[0]
    red_pixels.append(p1[2])
    green_pixels.append(p1[1])
    blue_pixels.append(p1[0])

red_pixels.sort()
green_pixels.sort()
blue_pixels.sort()

for y in range(0, height-1):
  for x in range(0, width-1):
    img0[y,x] = [blue_pixels.pop(0), green_pixels.pop(0), red_pixels.pop(0)]

print img[100,0]
print img[100,1]
print img[100,2]

print img0[100, 0]
print img0[100, 1]
print img0[100, 2]

cv2.imwrite('img0.jpg', img0)
cv2.imshow('img-0', img0)

cv2.waitKey(0)
cv2.destroyAllWindows()
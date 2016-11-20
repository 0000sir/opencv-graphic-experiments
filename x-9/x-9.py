import cv2
import numpy as np

img = cv2.imread('../road.jpg')
#img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
cv2.imshow('img', img)
height, width = img.shape[:2]

img0 = np.zeros((height, width, 3), np.uint8)

for x in range(0, width-1):
  for y in range(0, height-1):
    point = img[y, x]
    minist = min(point)
    b0, g0, r0 = point[0],point[1], point[2]
    r0 = r0 <= minist and r0 or 0
    g0 = g0 <= minist and g0 or 0
    b0 = b0 <= minist and b0 or 0
    img0[y, x] = [b0, g0 ,r0]

print img[100,100]
print img0[100,100]
    
cv2.imshow('img-0', img0)

cv2.waitKey(0)
cv2.destroyAllWindows()
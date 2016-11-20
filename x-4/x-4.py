import cv2
import numpy as np

img = cv2.imread('images/img1.jpg')
#img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
cv2.imshow('img', img)
#img[100,100] = [0, 0, 0]
height, width = img.shape[:2]

img0 = np.zeros((height, width, 3), np.uint8)
img1 = np.zeros((height, width, 3), np.uint8)

for x in range(0, height-1):
  for y in range(0, width-1):
    point = img[x, y]
    r0 = point[2]%2==0 and point[2] or 0
    g0 = point[1]%2==0 and point[1] or 0
    b0 = point[0]%2==0 and point[0] or 0
    r1 = point[2]%2==1 and point[2] or 0
    g1 = point[1]%2==1 and point[1] or 0
    b1 = point[0]%2==1 and point[0] or 0
    img0[x,y] = [g0, r0, b0]
    img1[x,y] = [g1, r1, b1]

print img0[100,100]
print img1[100,100]
    
cv2.imshow('img-0', img0)
cv2.imshow('img-1', img1)

img3 = np.zeros((100,100,3), np.uint8)
img3[:, 0:0.5*100] = img0[100,100]
img3[:,0.5*100:100] = img1[100,100]

cv2.imshow('img-3', img3)

cv2.waitKey(0)
cv2.destroyAllWindows()

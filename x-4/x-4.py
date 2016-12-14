import cv2
import numpy as np

def separate_frame(frame, width, height):
  odd_frame = np.zeros((height, width, 3), np.uint8)
  even_frame = np.zeros((height,width, 3), np.uint8)
  for x in range(0, height-1):
    for y in range(0, width-1):
      point = frame[x, y]
      r0 = point[2]%2==0 and point[2] or 0
      g0 = point[1]%2==0 and point[1] or 0
      b0 = point[0]%2==0 and point[0] or 0
      r1 = point[2]%2==1 and point[2] or 0
      g1 = point[1]%2==1 and point[1] or 0
      b1 = point[0]%2==1 and point[0] or 0
      even_frame[x,y] = [g0, r0, b0]
      odd_frame[x,y] = [g1, r1, b1]
  return (odd_frame, even_frame)

img = cv2.imread('../people.jpg')
#cv2.imshow('img', img)
height, width = img.shape[:2]

img0,img1 = separate_frame(img, width, height)

cv2.imshow('img-0', img0)
cv2.imshow('img-1', img1)

cv2.waitKey(0)
cv2.destroyAllWindows()

import cv2
import numpy as np

img = cv2.imread('../road.jpg') # As default, cv reads image as BGR colors
#img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB) # convert to RGB colors
cv2.imshow('img', img)

height, width = img.shape[:2]

img0 = np.zeros((height, width, 3), np.uint8)

red_pixels = img[:,:,2]
green_pixels = img[:,:,1]
blue_pixels = img[:,:,0]

red_pixels.shape = -1
green_pixels.shape = -1
blue_pixels.shape = -1

red_pixels = np.sort(red_pixels)
green_pixels = np.sort(green_pixels)
blue_pixels = np.sort(blue_pixels)

red_pixels.shape = height, width
green_pixels.shape = height, width
blue_pixels.shape = height, width

img0[:,:,2] = red_pixels
img0[:,:,1] =  green_pixels
img0[:,:,0] = blue_pixels

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

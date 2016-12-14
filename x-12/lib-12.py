import cv2
import numpy as np

def sort_frame(img, width, height):
  red_pixels = img[:,:,2]
  green_pixels = img[:,:,1]
  blue_pixels = img[:,:,0]
  red_pixels.shape = -1
  green_pixels.shape = -1
  blue_pixels.shape = -1
  red_pixels = np.sort(red_pixels)[::-1]
  green_pixels = np.sort(green_pixels)[::-1]
  blue_pixels = np.sort(blue_pixels)[::-1]
  red_pixels.shape = height, width
  green_pixels.shape = height, width
  blue_pixels.shape = height, width
  img0 = np.zeros((height, width, 3), np.uint8)
  img0[:,:,2] = red_pixels
  img0[:,:,1] = green_pixels
  img0[:,:,0] = blue_pixels
  return img0

img = cv2.imread('../people.jpg')
height, width = img.shape[:2]

img0 = sort_frame(img, width, height)

cv2.imwrite('ii.jpg', img0)


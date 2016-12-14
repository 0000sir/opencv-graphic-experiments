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
  img0[:,:,1] =  green_pixels
  img0[:,:,0] = blue_pixels
  return img0


video = cv2.VideoCapture("./X-12.mov")

width = int(video.get(cv2.cv.CV_CAP_PROP_FRAME_WIDTH))
height = int(video.get(cv2.cv.CV_CAP_PROP_FRAME_HEIGHT))
frames = int(video.get(cv2.cv.CV_CAP_PROP_FRAME_COUNT))
fps = video.get(cv2.cv.CV_CAP_PROP_FPS)

#out_video  = np.zeros((frames, height, width, 3), np.uint8)
out_frame = np.zeros((height, width, 3), np.uint8)

writer = cv2.VideoWriter("out.avi", cv2.cv.CV_FOURCC('M', 'J', 'P', 'G'), fps, (int(width), int(height)))

while True:
  idx = video.get(cv2.cv.CV_CAP_PROP_POS_FRAMES)
  ret, frame = video.read()
  if not ret:
    break
  out_frame = sort_frame(frame, width, height)
  #out_video[int(idx),:,:,:] = sort_frame(frame, width, height)
  writer.write(out_frame)
	
video.release()



#for i in range(int(idx+1)):
#  writer.write(out_video[i])

writer.release()


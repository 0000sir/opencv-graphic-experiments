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


video = cv2.VideoCapture("./x-4.mov")
width = int(video.get(cv2.cv.CV_CAP_PROP_FRAME_WIDTH))
height = int(video.get(cv2.cv.CV_CAP_PROP_FRAME_HEIGHT))
frames = int(video.get(cv2.cv.CV_CAP_PROP_FRAME_COUNT))
fps = video.get(cv2.cv.CV_CAP_PROP_FPS)

out_frame = np.zeros((height, width, 3), np.uint8)

writer_odd = cv2.VideoWriter("out-odd.avi", cv2.cv.CV_FOURCC('M', 'J', 'P', 'G'), fps, (int(width), int(height)))
writer_even = cv2.VideoWriter("out-even.avi", cv2.cv.CV_FOURCC('M', 'J', 'P', 'G'), fps, (int(width), int(height)))

while True:
  idx = video.get(cv2.cv.CV_CAP_PROP_POS_FRAMES)
  ret, frame = video.read()
  if not ret:
    break
  odd_frame, even_frame = separate_frame(frame, width, height)
  writer_odd.write(odd_frame)
  writer_even.write(even_frame)

video.release()
writer.release()


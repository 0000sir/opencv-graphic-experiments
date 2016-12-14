import cv2
import numpy as np

video = cv2.VideoCapture("../lake-with-boat.mov")

width = video.get(cv2.cv.CV_CAP_PROP_FRAME_WIDTH)
height = video.get(cv2.cv.CV_CAP_PROP_FRAME_HEIGHT)
frames = video.get(cv2.cv.CV_CAP_PROP_FRAME_COUNT)
fps = video.get(cv2.cv.CV_CAP_PROP_FPS)

out_video  = np.zeros((frames, height, width, 3), np.uint8)

while True:
  idx = video.get(cv2.cv.CV_CAP_PROP_POS_FRAMES)
  ret, frame = video.read()
  if not ret:
    break
  
  out_video[idx,:,:,:] = frame

video.release()

for x in range(int(height)):
  for y in range(int(width)):
    for c in range(3):
      t = out_video[:,x,y,c]
      out_video[:,x,y,c] = np.sort(t)


writer = cv2.VideoWriter("out.avi", cv2.cv.CV_FOURCC('M', 'J', 'P', 'G'), fps, (int(width), int(height)))

for i in range(int(idx+1)):
  writer.write(out_video[i])

writer.release()

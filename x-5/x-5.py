import cv2
import cv2.cv as cv
import numpy as np

vidcap = cv2.VideoCapture('v1.mp4')
vidcap.set(cv.CV_CAP_PROP_POS_MSEC,60000)
success0, frame_current = vidcap.read()
vidcap.set(cv.CV_CAP_PROP_POS_MSEC,63000)
success1, frame_future = vidcap.read()
vidcap.set(cv.CV_CAP_PROP_POS_MSEC,67000)
success2, frame_far_future = vidcap.read()

height, width = frame_current.shape[:2]
img0 = np.zeros((height, width, 3), np.uint8)

for y in range(0, height-1):
  for x in range(0, width-1):
    img0[y, x] = [frame_current[y, x][0], frame_future[y, x][1], frame_far_future[y, x][2]]

#cv2.imshow("20sec",img0)
#cv2.waitKey()
cv2.imwrite("90_93_97.jpg", img0)
cv2.destroyAllWindows()
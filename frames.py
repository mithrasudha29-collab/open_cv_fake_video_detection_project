import cv2 as cv
import numpy as np
import os
capture=cv.VideoCapture(r"C:\Users\mithr\Downloads\5871756-hd_1080_1920_30fps.mp4")
if not capture.isOpened():
    print("Video not opened ")
    exit()
#no of frames
total_frames=int(capture.get(cv.CAP_PROP_FRAME_COUNT))
#get evenly spaced frames
frame_indices=[]
for i in range(10):
    frame_indices.append(int(i*total_frames/10))
os.makedirs(r"M:\ML-PC\output",exist_ok=True)
for i,frame_number in enumerate(frame_indices):
    capture.set(cv.CAP_PROP_POS_FRAMES,frame_number)
    ret,frame=capture.read()
    if ret:
        cat=os.path.join(r"M:\ML-PC\output",f"frame_{i:02d}.jpg")#save as jpg
        cv.imwrite(cat,frame)
capture.release()
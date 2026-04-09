import cv2 as cv
import numpy as np
import os
frame_files=sorted(os.listdir(r"M:\ML-PC\output"))
img=cv.imread(r"M:\ML-PC\output\frame_02.jpg")
#resizing iamge
resized=cv.resize(img,(224,224))
#converting bgr to rgb as ml modes can learn
rgb_image=cv.cvtColor(resized,cv.COLOR_BGR2RGB)
#normalization
normalized=rgb_image/255.0
#tensor
tensor=np.transpose(normalized,(2,0,1))
tensor=np.float32(tensor)
tensors=[]
tensors.append(tensor)
batch=np.stack(tensors,axis=0)

cv.imshow("normalized",normalized)
cv.waitKey(0)
cv.destroyAllWindows()
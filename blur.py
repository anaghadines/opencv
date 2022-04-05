# import cv2
# import numpy as np
#
# image=cv2.imread("train.jpg",0)
# matrix=np.ones((5,5),np.float32)/25
# new_image=cv2.filter2D(image,-1,matrix)
# cv2.imshow("image",image)
# cv2.imshow("newimage",new_image)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

import cv2
import numpy as np
image=cv2.imread("train.jpg",1)
blur=cv2.blur(image,(5,5))
gaussian_blur=cv2.GaussianBlur(image,(5,5),0)
cv2.imshow('image',image)
cv2.imshow('blur',blur)
cv2.imshow('gaussian',gaussian_blur)
cv2.waitKey(0)
cv2.destroyAllWindows()
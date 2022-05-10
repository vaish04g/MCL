import cv2
import numpy as np

image = cv2.imread("flowerdrop.jpg")
cv2.imshow("binary_image",image)

# kernel = np.ones((3,3),np.float32)/9
# processed_img = cv2.filter2D(image, -1, kernel)

# line 7,8
# OR
processed_img = cv2.blur(image, (5,5))

cv2.imshow("processed_image", processed_img)
cv2.waitKey(0)

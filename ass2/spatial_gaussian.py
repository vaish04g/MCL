import cv2

img = cv2.imread("flowerdrop.jpg")

processed_img = cv2.GaussianBlur(img,(5,5),0)

cv2.imshow("original",img)
cv2.imshow("gaussian_img",processed_img)

cv2.waitKey(0)


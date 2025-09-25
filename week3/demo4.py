import cv2
import matplotlib.pyplot as plt
image = cv2.imread('./practice9.png')
gray_img = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

cv2.imshow('original img', gray_img)
cv2.waitKey(0)

ret, thresh = cv2.threshold(gray_img, 64, 255, cv2.THRESH_BINARY)
cv2.imshow("thresholed image: 64", thresh)
cv2.waitKey(0)

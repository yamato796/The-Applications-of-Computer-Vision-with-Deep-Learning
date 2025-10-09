import cv2
import matplotlib.pyplot as plt
import numpy as np
image = cv2.imread('./sudoku.png')

gray_img = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

cv2.imshow('original img', gray_img)
cv2.waitKey(0)

ret, thresh = cv2.threshold(gray_img, 128, 255, cv2.THRESH_BINARY)
#cv2.imshow("thresholed image: 128", thresh)
#cv2.waitKey(0)


ret, thresh = cv2.threshold(gray_img, 64, 255, cv2.THRESH_BINARY)
#cv2.imshow("thresholed image: 64", thresh)
#cv2.waitKey(0)

img_info = image.shape
height = img_info[0]
width = img_info[1]
dst = np.zeros((height,width,1), np.uint8)

for i in range(0,height):
    for j in range(0,width):
        dst[i][j] = 255 - thresh[i][j]
cv2.imwrite('./dst.png', dst)
cv2.imshow('inverted image', dst)
cv2.waitKey(0)

ret, adv_thresh = cv2.threshold(gray_img, 0, 255, cv2.THRESH_BINARY+cv2.THRESH_OTSU)
cv2.imshow("adaptive thresholed image", adv_thresh)
cv2.waitKey(0)



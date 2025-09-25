import cv2
import matplotlib.pyplot as plt
image = cv2.imread('./lenna.png')

cv2.imshow('original image', image)
cv2.waitKey(0)
 

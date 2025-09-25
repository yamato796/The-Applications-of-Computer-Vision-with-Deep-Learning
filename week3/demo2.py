import cv2
import matplotlib.pyplot as plt
image = cv2.imread('./road.jpg')

low = 10
high = 100
edges = cv2.Canny(image,low,high)

cv2.imshow("Canny edge", edges)
cv2.waitKey(0)

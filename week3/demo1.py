import cv2
import matplotlib.pyplot as plt
image = cv2.imread('./lenna.png')

def show_with_matplotlib(color_img, title, pos):
    #Convert BGR to RGB
    img_RGB = color_img[:, :, ::-1]
    ax = plt.subplot(1, 4, pos)
    plt.imshow(img_RGB)
    plt.title(title)
    plt.axis('off')

#cv2.imshow('original image', image)
#cv2.waitKey(0)

plt.figure(figsize=(10, 4))
plt.suptitle("Sobel operator and cv2.addWeighted() to show the output", fontsize=14, fontweight='bold')

image_filtered = cv2.GaussianBlur(image, (7, 7), 5)

cv2.imshow("Gaussian filtered", image_filtered)
cv2.waitKey(0)

gray_image = cv2.cvtColor(image_filtered, cv2.COLOR_BGR2GRAY)

# Sobel X 與 Y
gradient_x = cv2.Sobel(gray_image, cv2.CV_16S, 1, 0, 3)
gradient_y = cv2.Sobel(gray_image, cv2.CV_16S, 0, 1, 3)

# 取絕對值
abs_gradient_x = cv2.convertScaleAbs(gradient_x)
abs_gradient_y = cv2.convertScaleAbs(gradient_y)

# 合併 X 與 Y
sobel_image = cv2.addWeighted(abs_gradient_x, 0.5, abs_gradient_y, 0.5, 0)

# 使用 OpenCV 顯示
cv2.imshow("Abs Gradient x", abs_gradient_x)
cv2.waitKey(0)
cv2.imshow("Abs Gradient y", abs_gradient_y)
cv2.waitKey(0)
cv2.imshow("sobel image", sobel_image)
cv2.waitKey(0)

# 使用 matplotlib 顯示結果
show_with_matplotlib(image, "Image", 1)
show_with_matplotlib(cv2.cvtColor(abs_gradient_x, cv2.COLOR_GRAY2BGR),"Gradient X", 2)
show_with_matplotlib(cv2.cvtColor(abs_gradient_y, cv2.COLOR_GRAY2BGR),"Gradient Y", 3)
show_with_matplotlib(cv2.cvtColor(sobel_image, cv2.COLOR_GRAY2BGR),"Sobel combined", 4)
plt.show()

cv2.destroyAllWindows()


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

image_filtered = cv2.GaussianBlur(image, (3, 3), 0)

cv2.imshow("Gaussian filtered", image_filtered)
cv2.waitKey(0)

 

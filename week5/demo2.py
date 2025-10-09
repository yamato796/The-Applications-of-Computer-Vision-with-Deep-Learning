from tensorflow.keras.datasets import mnist
from tensorflow.keras import models
from tensorflow.keras import layers
import matplotlib.pyplot as plt

(train_images, train_labels), (test_images, test_labels) = mnist.load_data()

print(train_images.ndim)
print(train_images.shape)
print(train_images.dtype)

for i in range(0,9):
    digit = train_images[i]
    plt.imshow(digit, cmap=plt.cm.binary)
    plt.show()

my_slice = train_images[10:100]
print(my_slice.shape)

my_slice = train_images[10:100, :, :]
print(my_slice.shape)

my_slice = train_images[10:100, 0:28, 0:28]
print(my_slice.shape)

batch = train_images[:128]
print(batch.shape)
batch = train_images[128:256]
print(batch.shape)






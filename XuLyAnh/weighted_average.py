import numpy as np
from PIL import Image

def weighted_average_filter(image_array):
    kernel = np.array([[1, 2, 1],
                       [2, 4, 2],
                       [1, 2, 1]]) / 16

    result = np.zeros_like(image_array)

    for i in range(1, image_array.shape[0] - 1):
        for j in range(1, image_array.shape[1] - 1):
            region = image_array[i-1:i+2, j-1:j+2]
            result[i, j] = np.sum(region * kernel)

    return result[1:-1, 1:-1]  

img = Image.open('sky.jpg')
img_array = np.array(img, dtype=np.float32)

filtered_img = weighted_average_filter(img_array)

filtered_image = Image.fromarray(filtered_img.astype(np.uint8))
filtered_image.show()

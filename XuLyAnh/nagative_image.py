import numpy as np
from PIL import Image

img = Image.open('sky.jpg')

arr = np.array(img)
negative = 255 - arr
negative_img = Image.fromarray(negative)

negative_img.show()
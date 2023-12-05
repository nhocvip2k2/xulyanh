import numpy as np
from PIL import Image

def apply_logarithm(image_array, c=1):
    
    result = c * np.log(1 + image_array)

    
    result = (255 / np.max(result)) * result

    return result.astype(np.uint8)


img_path = 'sky.jpg'
img = Image.open(img_path).convert('L')
img_array = np.array(img, dtype=np.float32)


processed_img = apply_logarithm(img_array)

original_image = Image.fromarray(img_array.astype(np.uint8))
processed_image = Image.fromarray(processed_img)

original_image.show(title='Original Image')
processed_image.show(title='Logarithmic Processed Image')

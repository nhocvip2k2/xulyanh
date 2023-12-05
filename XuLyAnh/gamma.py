import numpy as np
from PIL import Image

def apply_gamma_correction(image_array, gamma=1):
    
    normalized_image = image_array / 255.0
    
    corrected_image = np.power(normalized_image, gamma)
    
    
    corrected_image = (corrected_image * 255).astype(np.uint8)

    return corrected_image


img_path = 'sky.jpg'
img = Image.open(img_path).convert('L')
img_array = np.array(img, dtype=np.float32)


gamma_value = 1.5  
processed_img = apply_gamma_correction(img_array, gamma=gamma_value)


original_image = Image.fromarray(img_array.astype(np.uint8))
processed_image = Image.fromarray(processed_img)

original_image.show(title='Original Image')
processed_image.show(title=f'Gamma Processed Image (Gamma = {gamma_value})')

import cv2
from matplotlib import pyplot as plt

def otsu_thresholding(image):
   
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    
    _, thresholded_image = cv2.threshold(gray_image, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)

    return thresholded_image

# Đọc ảnh đầu vào
img_path = 'sky.jpg'
img = cv2.imread(img_path)

# Áp dụng phân ngưỡng Otsu
otsu_img = otsu_thresholding(img)

# Hiển thị ảnh gốc và ảnh đã xử lý bằng phương pháp Otsu
plt.subplot(121), plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB)), plt.title('Original Image')
plt.subplot(122), plt.imshow(otsu_img, cmap='gray'), plt.title('Otsu Thresholding')
plt.show()

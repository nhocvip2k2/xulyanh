import cv2
import numpy as np
from matplotlib import pyplot as plt

def laplacian_filter(image):
    # Chuyển đổi ảnh sang ảnh xám
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Áp dụng bộ lọc Laplacian
    laplacian_result = cv2.Laplacian(gray_image, cv2.CV_64F)

    # Chuyển đổi kết quả về giá trị tuyệt đối và kiểu uint8 để hiển thị
    laplacian_result = np.abs(laplacian_result).astype(np.uint8)

    return laplacian_result

# Đọc ảnh đầu vào
img_path = 'sky.jpg'
img = cv2.imread(img_path)

# Áp dụng bộ lọc Laplacian
laplacian_img = laplacian_filter(img)

# Hiển thị ảnh gốc và ảnh đã xử lý bằng bộ lọc Laplacian
plt.subplot(121), plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB)), plt.title('Original Image')
plt.subplot(122), plt.imshow(laplacian_img, cmap='gray'), plt.title('Laplacian Filter')
plt.show()

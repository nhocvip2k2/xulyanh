import cv2
from matplotlib import pyplot as plt

def histogram_equalization(image):
    # Chuyển đổi ảnh sang ảnh xám
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Áp dụng cân bằng histogram
    equalized_image = cv2.equalizeHist(gray_image)

    return equalized_image

# Đọc ảnh đầu vào
img_path = 'sky.jpg'
img = cv2.imread(img_path)

# Áp dụng cân bằng histogram
equalized_img = histogram_equalization(img)

# Hiển thị ảnh gốc và ảnh đã xử lý bằng cân bằng histogram
plt.subplot(121), plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB)), plt.title('Original Image')
plt.subplot(122), plt.imshow(equalized_img, cmap='gray'), plt.title('Histogram Equalization')
plt.show()

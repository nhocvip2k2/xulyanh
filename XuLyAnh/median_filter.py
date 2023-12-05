import cv2
from matplotlib import pyplot as plt

def median_filter(image, kernel_size):
    # Áp dụng bộ lọc trung bình
    median_filtered_image = cv2.medianBlur(image, kernel_size)

    return median_filtered_image

# Đọc ảnh đầu vào
img_path = 'sky.jpg'
img = cv2.imread(img_path)

# Áp dụng bộ lọc trung bình với kernel size là 5x5 (có thể điều chỉnh kích thước kernel)
median_filtered_img = median_filter(img, kernel_size=5)

# Hiển thị ảnh gốc và ảnh đã xử lý bằng bộ lọc trung bình
plt.subplot(121), plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB)), plt.title('Original Image')
plt.subplot(122), plt.imshow(cv2.cvtColor(median_filtered_img, cv2.COLOR_BGR2RGB)), plt.title('Median Filter')
plt.show()

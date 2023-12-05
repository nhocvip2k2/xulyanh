import cv2
from matplotlib import pyplot as plt

def auto_white_balance(image):
    result = cv2.xphoto.createSimpleWB()
    balanced_image = result.balanceWhite(image)

    return balanced_image

# Đọc ảnh đầu vào
img_path = 'sky.jpg'
img = cv2.imread(img_path)

# Áp dụng cân bằng màu tự động
balanced_img = auto_white_balance(img)

# Hiển thị ảnh gốc và ảnh đã cân bằng màu
plt.subplot(121), plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB)), plt.title('Original Image')
plt.subplot(122), plt.imshow(cv2.cvtColor(balanced_img, cv2.COLOR_BGR2RGB)), plt.title('Balanced Image')
plt.show()

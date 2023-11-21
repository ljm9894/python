import cv2
import numpy as np
from matplotlib import pyplot as plt

input_image = cv2.imread('C:\\Users\\b0107\\python\\20231120\\work\\s2-5.png', cv2.IMREAD_GRAYSCALE)

f = np.fft.fft2(input_image)
fshift = np.fft.fftshift(f)
magnitude_spectrum = 20 * np.log(np.abs(fshift))

plt.subplot(221), plt.imshow(input_image, cmap='gray')
plt.title('Input Image'), plt.xticks([]), plt.yticks([])

plt.subplot(222), plt.imshow(magnitude_spectrum, cmap='gray')
plt.title('Fourier Transform'), plt.xticks([]), plt.yticks([])


rows, cols = input_image.shape
crow, ccol = rows // 2, cols // 2

mask = np.ones((rows, cols), np.uint8)
r = 30
center = [crow, ccol]
x, y = np.ogrid[:rows, :cols]
mask_area = (x - center[0]) ** 2 + (y - center[1]) ** 2 <= r*r
mask[mask_area] = 0

fshift_filtered = fshift * mask
magnitude_spectrum_filtered = 20 * np.log(np.abs(fshift_filtered))

plt.subplot(223), plt.imshow(magnitude_spectrum, cmap='gray')
plt.title('Fourier Transform'), plt.xticks([]), plt.yticks([])

plt.subplot(224), plt.imshow(magnitude_spectrum_filtered, cmap='gray')
plt.title('Filtered Fourier Transform'), plt.xticks([]), plt.yticks([])


f_filtered = np.fft.ifftshift(fshift_filtered)
img_back = np.fft.ifft2(f_filtered)
img_back = np.abs(img_back)

plt.imshow(img_back, cmap='gray')
plt.title('Filtered Image'), plt.xticks([]), plt.yticks([])
plt.show()
cv2.imwrite('filtered_image.png', img_back)

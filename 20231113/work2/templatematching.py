
import cv2
import numpy as np
from matplotlib import pyplot as plt

input_image = cv2.imread('C:\\Users\\b0107\\python\\20231113\\img\\s1-5.png', cv2.IMREAD_GRAYSCALE)

template_image = cv2.imread('C:\\Users\\b0107\\python\\20231113\\img\\s1-5_template.png', cv2.IMREAD_GRAYSCALE)

result = cv2.matchTemplate(input_image, template_image, cv2.TM_CCOEFF_NORMED)
min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)

h, w = template_image.shape
pts1 = np.float32([max_loc, (max_loc[0] + w, max_loc[1]), (max_loc[0], max_loc[1] + h), (max_loc[0] + w, max_loc[1] + h)])
pts2 = np.float32([[0, 0], [w, 0], [0, h], [w, h]])

matrix = cv2.getPerspectiveTransform(pts1, pts2)
perspective_transformed_image = cv2.warpPerspective(input_image, matrix, (w, h))
plt.subplot(131), plt.imshow(input_image, cmap='gray')
plt.title('Input Image'), plt.xticks([]), plt.yticks([])

plt.subplot(132), plt.imshow(result, cmap='gray')
plt.title('Template Matching Result'), plt.xticks([]), plt.yticks([])

plt.subplot(133), plt.imshow(perspective_transformed_image, cmap='gray')
plt.title('Perspective Transformation Result'), plt.xticks([]), plt.yticks([])

plt.show()
cv2.imwrite('perspective_transformed_image.png', perspective_transformed_image)

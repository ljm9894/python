import cv2
import numpy as np
image = cv2.imread("C:\\Users\\DGSW\\Desktop\\python\\img\\smufcat.jpg")

height, width, _ = image.shape

gray_image = np.zeros((height, width), dtype=np.uint8)
for y in range(int(height/2),height):
    for x in range(int(width/2), width):
        blue,green, red = image[y,x]
        gray_value = int((red + green + blue)/3)
        gray_image[y,x] = gray_value
cv2.imwrite('그레이이미지.png', gray_image)

cv2.imshow('Gray Image', gray_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
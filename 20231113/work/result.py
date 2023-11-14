

import numpy as np
import cv2
from matplotlib import pyplot as plt

path = "C:\\Users\\b0107\\python\\20231113\\work\\s2-4.png"
img = cv2.imread(path,0)
cv2.imshow('after',img)

a = np.zeros((256,),dtype=np.float16)
b = np.zeros((256,),dtype=np.float16)

height,width=img.shape

for i in range(width):
    for j in range(height):
        g = img[j,i]
        a[g] = a[g]+1
 


tmp = 1.0/(height*width)
b = np.zeros((256,),dtype=np.float16)

for i in range(256):
    for j in range(i+1):
        b[i] += a[j] * tmp;
    b[i] = round(b[i] * 255);
b=b.astype(np.uint8)

for i in range(width):
    for j in range(height):
        g = img[j,i]
        img[j,i]= b[g]

hist_original = cv2.calcHist([img], [0], None, [256], [0, 256])

plt.plot(hist_original)
plt.title('Original Histogram')
plt.xticks([])
plt.yticks([])


hist_equalized = cv2.calcHist([img], [0], None, [256], [0, 256])

plt.plot(hist_equalized)
plt.title('Equalized Histogram')
plt.xticks([])
plt.yticks([])
plt.show()

cv2.imshow('before',img)
cv2.waitKey(0)
cv2.destroyAllWindows()
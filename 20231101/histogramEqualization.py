import cv2
import numpy as np
from matplotlib import pyplot as plt

def histogram_equalization():
    img = cv2.imread("C:\\Users\\b0107\\python\img\\smufcat.jpg", 0)
    eqhist = cv2.equalizeHist(img)

    hist1 = cv2.calcHist([img],[0], None, [256], [0,256])
    hist2 = cv2.calcHist([eqhist], [0], None, [256], [0,256])

    plt.subplot(221), plt.imshow(img, 'gray')
    plt.title('Original'), plt.xticks([]), plt.yticks([])

    plt.subplot(222), plt.imshow(eqhist, 'gray')
    plt.title('Histogram Equlization'), plt.xticks([]), plt.yticks([])
    
    plt.subplot(223), plt.plot(hist1), plt.xlim([0,256])
    plt.subplot(224), plt.plot(hist2) ,plt.xlim([0,256])

    plt.show()

histogram_equalization()
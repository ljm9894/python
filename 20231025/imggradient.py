import cv2
import numpy as np
from matplotlib import pyplot as plt

def image_gradient():
    img = cv2.imread("C:\\Users\\b0107\\python\img\\smufcat.jpg")
    laplacian = cv2.Laplacian(img, cv2.CV_8U)
    sobelx = cv2.Sobel(img, cv2.CV_8U, 1, 0, ksize = 3)
    sobely = cv2.Sobel(img, cv2.CV_8U,0,1, ksize=3)
    sobelxy = cv2.Sobel(sobelx, cv2.CV_8U,0,1, ksize=3)
    canny = cv2.Canny(img,30,70)
    images = [ img, laplacian, sobelx, sobely,sobelxy, canny]

    titles = ["Original", 'Laplacian', 'Sobel_x', 'Sobel_y', 'Sobel_xy','Canny']

    for i in range(6):
        plt.subplot(2,3,i+1), plt.imshow(images[i]), plt.title([titles[i]])
        plt.xticks([]), plt.yticks([])
    # for i in range(3):
    #     plt.subplot(2,3,i+4), plt.imshow(images[i+2]),plt.title([titles[i+2]])
    #     plt.xticks([]),plt.yticks([])
    plt.show()

image_gradient();
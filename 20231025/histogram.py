import cv2
import numpy as np
from matplotlib import pyplot as plt

def histogram():
    img1 = cv2.imread("C:\\Users\\b0107\\python\img\\smufcat.jpg")
    img2 = cv2.imread("C:\\Users\\b0107\\python\img\\smufcat.jpg")

    img1_gray = cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY)
    img2_gray = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)

    def cvt(i) : 
        b,g,r = cv2.split(i)
        i = cv2.merge([r,g,b])
        return i
    img1 = cvt(img1)
    img2 = cvt(img2)

    hist1 = cv2.calcHist([img1_gray], [0], None, [256], [0,256])
    hist2 = cv2.calcHist([img2_gray],[0],None, [256],[0,256])
    
    plt.subplot(221), plt.imshow(img1), plt.title('Image_A'), plt.xticks([]), plt.yticks([])
    plt.subplot(222), plt.imshow(img2), plt.title('Image_B'), plt.xticks([]), plt.yticks([])
    plt.subplot(223), plt.plot(hist1), plt.xlim([0,256])
    plt.subplot(224), plt.plot(hist2), plt.xlim([0,256]) 

    plt.show()
histogram()
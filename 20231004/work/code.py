import cv2
import numpy as np
from matplotlib import pyplot as plt

def thresholding():
    img = cv2.imread('C:\\Users\\b0107\\python\img\\smufcat.jpg', cv2.IMREAD_GRAYSCALE)
    th_max = 255
    resize_img = cv2.resize(img,(500,500))
    cv2.imshow('input', resize_img);

    ret_1, thresh = cv2.threshold(resize_img, 110, th_max, cv2.THRESH_BINARY)
   
    cv2.imshow('result', thresh)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    

thresholding()
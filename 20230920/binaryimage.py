import cv2
import numpy as np

def image_binary():
    img = cv2.imread('C:\\Users\\b0107\\img.jpg', cv2.IMREAD_COLOR)

    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    ret, dst = cv2.threshold(gray, 150,255, cv2.THRESH_BINARY)

    cv2.imshow('JetsonNano_Original', img)
    cv2.imshow('JetSonNano_Binary', dst)
    cv2.imshow('JetSonNano_Gray', gray)

    cv2.waitKey(0)
    cv2.destroyAllWindows()
image_binary()
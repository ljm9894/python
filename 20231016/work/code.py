import cv2
import matplotlib.pyplot as plt
def gray_img():
    img = cv2.imread("C:\\Users\\b0107\\python\img\\smufcat.jpg")
    color_img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    gray_img = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

    cv2.imshow('color', color_img)
    #cv2.imshow('before',img)
    cv2.imshow('after',gray_img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

gray_img()
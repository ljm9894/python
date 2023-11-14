import cv2
import numpy as np
from matplotlib import pyplot as plt

def template_matching():
    img = cv2.imread("C:\\Users\\b0107\\python\\20231113\\img\\s1-5.png",0)
    img2 = img.copy()
    template = cv2.imread("C:\\Users\\b0107\\python\\20231113\\img\\s1-5_template.png",0)
    w, h = template.shape[::-1]
    methods = ['cv2.TM_CCOEFF_NORMED']

    for meth in methods:
        img = img2.copy()
        method = eval(meth)
        res = cv2.matchTemplate(img , template, method)
        min_val, max_val, min_loc, max_loc= cv2.minMaxLoc(res)
        if method in [cv2.TM_SQDIFF, cv2.TM_SQDIFF_NORMED]:
            top_left = min_loc
        else : 
            top_left = max_loc
        bottom_right = (top_left[0]+w, top_left[1]+h)
        cv2.rectangle(img, top_left, bottom_right, 255, 30)

        plt.subplot(121), plt.title('Template'), plt.imshow(res,cmap='gray'), plt.yticks([]), plt.xticks([])
        plt.subplot(122), plt.imshow(img, cmap='gray')
        plt.show()
template_matching()
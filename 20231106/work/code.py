import cv2
import numpy as np
from matplotlib import pyplot as plt

def histogram():
    img = cv2.imread('C:\\Users\\b0107\\python\\20231106\\work\\s2-3.png')
    
    h1, w1 , _ = img.shape

    b,g,r = cv2.split(img)

    hist_test = np.zeros((256))

    for y in range(h1):
        for x in range(w1):
            i = b[y,x]
            hist_test[i] = hist_test[i]+1
    
    cv2.imshow("img",b)
    plt.plot(hist_test), plt.xlim([0,256])
    
    plt.show()
    cv2.waitKey(0)
    cv2.destroyAllWindows()
histogram()
import cv2
import numpy as np

def rectangle():
    img = np.zeros((512, 512, 3), np.uint8)
    img.fill(255)
    img = cv2.rectangle(img, (100,150), (500,300), (0,255,0),5)
    cv2.imshow('JetsonNano_Rectangle',img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

rectangle()

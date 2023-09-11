import cv2
import numpy as np

def circle():
    img = np.zeros((512, 512, 3), np.uint8)
    img.fill(255)
    img = cv2.circle(img, (300,200), 100, (0,255, 0) ,2)
    cv2.imshow('JetsonNano_Circle', img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

circle()
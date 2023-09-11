import cv2
import numpy as np
def ellipse():
    img = np.zeros((512,512,3), np.uint8)
    img.fill(255)
    img = cv2.ellipse(img, (256,256), (100,25), 0,0,270,(0,255,0),-1)

    cv2.imshow('JetsonNano_Ellipse',img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

ellipse()
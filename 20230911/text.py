import cv2
import numpy as np

def text() :
    img = np.zeros((512,512,1), np.uint8)
    img.fill(255)
    img = cv2.putText(img, 'Hello', (100,150), cv2.FONT_HERSHEY_PLAIN,6,(0,180,256),5)
    img2 = cv2.rectangle(img, (100,150), (500,300), (0,255,0),5)
    cv2.imshow('JetsonNano_PutTExt', img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

text()
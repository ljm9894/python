import cv2
import numpy as np

def hough_transform():
    img = cv2.imread("C:\\Users\\b0107\\python\\20231113\\img\\s1-5.png")
    img_original = img.copy()
    
    gray =cv2.cvtColor(img , cv2.COLOR_BGR2GRAY)
    edges = cv2.Canny(gray,50,150,apertureSize=3)
    lines = cv2.HoughLines(edges, 0.5,np.pi/180/250)

    for i in range(len(lines)):
        for rho, theta in lines[i]:
            a = np.cos(theta)
            b = np.sin(theta)
            x0 = a*rho
            y0=b*rho
            x1 = int(x0+2000*(-b))
            y1 = int(y0+2000*(a))
            x2 =int(x0-2000*(-b))
            y2 = int(y0-2000*(a))
            cv2.line(img,(x1,y1),(x2,y2),(51,102,255),5)

    cv2.imshow('JetsonNano_Original', img_original)
    cv2.imshow('JetsonNano_Edge', img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
hough_transform
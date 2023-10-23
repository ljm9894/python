import cv2
import numpy as np

def transform():
    img = cv2.imread("C:\\Users\\b0107\\python\img\\smufcat.jpg", cv2.IMREAD_COLOR)
    
    rows, cols = img.shape[:2]

    point1 = (int(cols*(1/4)), int(rows*(1/4)))
    point2 = (int(cols*(3/4)), int(rows*(1/4)))
    point3 = (int(cols*(1/4)), int(rows*(3/4)))

    out_point1 = (int(cols*(1/4)), int(rows*(3/8)))
    out_point2 = (int(cols*(3/4)), int(rows*(1/8)))
    out_point3 = (int(cols*(1/4)), int(rows*(7/8)))

    img_points = img.copy()
    cv2.circle(img_points, point1, 5, (0,0,255), -1)
    cv2.circle(img_points, point2, 5, (0,0,255), -1)
    cv2.circle(img_points, point3, 5, (0,0,255), -1)

    pts1 = np.float32([point1, point2, point3])
    pts2 = np.float32([out_point1, out_point2, out_point3])

    M = cv2.getAffineTransform(pts1, pts2)
    output_img = cv2.warpAffine(img, M,(rows,cols))

    cv2.imshow('Input Img', img_points)
    cv2.imshow('Output Img', output_img)

    cv2.waitKey(0)
    cv2.destroyAllWindows()

transform()
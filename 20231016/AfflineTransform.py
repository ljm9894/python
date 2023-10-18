import cv2
import numpy as np
from matplotlib import pyplot as plt

def image_affine_transformation():
    r_img = cv2.imread("C:\\Users\\b0107\\python\img\\smufcat.jpg", cv2.IMREAD_COLOR)
    img = cv2.resize(r_img,(500,500))
    rows,cols = img.shape[:2]
    
    pts1 = np.float32([[140,100], [360,100], [140,300]])
    pts2 = np.float32([[140,280], [360,170], [140,480]])

    cv2.circle(img, (140,100) ,10, (255,0,0) , -1)
    cv2.circle(img , (360, 100) , 10, (0,255,0), -1)
    cv2.circle(img, (140,300), 10 , (0,0,255), -1)

    M = cv2.getAffineTransform(pts1,pts2)
    dst = cv2.warpAffine(img, M , (cols, rows))

    fig = plt.figure()
    # fig.canvas.set_window_title("JetsonNano_Affine_transform")
    plt.subplot(121), plt.imshow(img), plt.title('IMAGE')
    plt.subplot(122), plt.imshow(dst), plt.title('AFFINE')
    plt.show()
image_affine_transformation()
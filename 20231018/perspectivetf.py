import cv2
import numpy as np
from matplotlib import pyplot as plt

def image_persective_transformation():
    img = cv2.imread("C:\\Users\\b0107\\python\img\\smufcat.jpg", cv2.IMREAD_COLOR)
    img = cv2.resize(img, (640,480))
    b,g,r = cv2.split(img)
    img = cv2.merge([r,g,b])

    pts1 = np.float32([[468, 200], [540, 180], [470,375], [540,425]])
    pts2 = np.float32([[10,10], [1000,10], [10, 1000], [1000, 1000]])

    cv2.circle(img,(468,200), 10, (255,0,0), -1)
    cv2.circle(img, (540,180), 10 , (0, 255,0) , -1)
    cv2.circle(img, (470,375), 10 , (0, 0,255) , -1)
    cv2.circle(img, (540,425), 10 , (255, 255,0) , -1)

    M = cv2.getPerspectiveTransform(pts1, pts2)
    dst = cv2.warpPerspective(img , M,(1010,1010))

    fig = plt.figure()
    # fig.canvas.set_window_title("JetsonNano_Perspective_transform")
    plt.subplot(121), plt.imshow(img), plt.title('IMAGE')
    plt.subplot(122), plt.imshow(dst), plt.title('PERSPECTIVE')

    plt.show()
image_persective_transformation()
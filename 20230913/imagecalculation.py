import cv2
import numpy as np

def bitwise_operation():
    img_1 = cv2.imread('C:\\Users\\b0107\\img.jpg')
    img_1 = cv2.resize(img_1, (256, 256))
    img_2 = cv2.imread('C:\\Users\\b0107\\img2.jpg')
    img_2 = cv2.resize(img_2, (512, 512))
    point = (512 - 140, 20)

    cv2.imshow('JetsonNano_Original', img_1)
    rows, cols, channels = img_1.shape
    roi = img_2[0:rows, 0:cols]

    img2gray = cv2.cvtColor(img_1, cv2.COLOR_BGR2GRAY)  # BGR에서 그레이 스케일로 변경
    cv2.imshow('JetsonNano_Gray', img2gray)
    ret, mask = cv2.threshold(img2gray, 100, 255, cv2.THRESH_BINARY)
    mask_inv = cv2.bitwise_not(mask)
    cv2.imshow('JetsonNano_Mask', mask)

    # 데이터 타입 일치시키기
    img_1_fg = cv2.bitwise_and(img_1, img_1, mask=mask.astype(np.uint8))
    img_2_bg = cv2.bitwise_and(roi, roi, mask=mask_inv.astype(np.uint8))
    dst = cv2.add(img_1_fg, img_2_bg)
    img_2[0:rows, 0:cols] = dst
    cv2.imshow('JetsonNano_Result', img_2)

    cv2.waitKey(0)
    cv2.destroyAllWindows()

bitwise_operation()

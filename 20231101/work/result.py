import cv2
import numpy as np

def morphologycalTransformation():
    input = cv2.imread('C:\\Users\\b0107\\python\\20231101\\img\\s1-4.png', cv2.IMREAD_GRAYSCALE)
    kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (5,5))
    morphology_result = cv2.morphologyEx(input, cv2.MORPH_OPEN, kernel)
    ret, binary_image = cv2.threshold(morphology_result, 1, 255, cv2.THRESH_BINARY)
    contours, _ = cv2.findContours(binary_image, cv2.RETR_CCOMP, cv2.CHAIN_APPROX_NONE)
    output = cv2.cvtColor(input, cv2.COLOR_GRAY2BGR)
    
    for i, contour in enumerate(contours):
        cv2.drawContours(output, [contour], -1, (0, 0, 255), 2)
        M = cv2.moments(contour)
        if M["m00"] != 0:
            cX = int(M["m10"] / M["m00"])
            cY = int(M["m01"] / M["m00"])
            cv2.putText(output, str(i + 1), (cX, cY), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 0), 1)

    cv2.imshow('Input Image', input)
    cv2.imshow('Output Image', output)

    cv2.imwrite('output_image.png', output)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

morphologycalTransformation()

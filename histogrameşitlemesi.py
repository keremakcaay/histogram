import cv2
import numpy as np


image = cv2.imread("lowcontrast.jpg", 0)

equalized_image = cv2.equalizeHist(image)


cv2.imshow("lowcontrast", image )
cv2.imshow("highcontrast", equalized_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
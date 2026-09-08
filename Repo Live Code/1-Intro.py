#load foto
import cv2

image = cv2.imread("1.png")

cv2.imshow("Foto", image)

cv2.waitKey(0)
cv2.destroyAllWindows()

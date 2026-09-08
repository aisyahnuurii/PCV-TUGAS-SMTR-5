import cv2

image = cv2.imread("B:/ITS/smtr 5/PCV/Tugas/Repo Live Code/1.png")

cv2.imshow("Foto", image)

cv2.waitKey(0)
cv2.destroyAllWindows()
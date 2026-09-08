#load foto
import cv2

image = cv2.imread("1.png")

cv2.imshow("Foto", image)

cv2.waitKey(0)
cv2.destroyAllWindows()


#filter bgr
import cv2

image = cv2.imread("1.png")
[h, w, c] = image.shape

for i in range(h):
    for j in range(w):
        image[i][j][0] = 0 #kalau dihilangkan, warna biru muncul
        image[i][j][1] = 0 #kalau dihilangkan, warna hijau muncul
        image[i][j][2] = 0 #kalau dihilangkan, warna merah muncul
        
cv2.imshow("Foto", image)
cv2.waitKey(0)
cv2.destroyAllWindows()


#webcam
import cv2

camera = cv2.VideoCapture(0)

while True:
    ok, frame = camera.read()
    if not ok: 
        break
    
    cv2.imshow("Camera", frame)

    if cv2.waitKey(1) == 27: #esc
        break

camera.release()
cv2.destroyAllWindows()


#webcam filter merah
import cv2

camera = cv2.VideoCapture(0)

while True:
    ok, image = camera.read()

    [h, w, c] = image.shape

    for i in range(h):
        for j in range(w):
            image[i][j][0] = 0
            image[i][j][1] = 0

    cv2.imshow("Filter Merah", image)

    if cv2.waitKey(1) == 27:
        break

camera.release()
cv2.destroyAllWindows()


#webcam filter hijau
import cv2

camera = cv2.VideoCapture(0)

while True:
    ok, image = camera.read()

    [h, w, c] = image.shape

    for i in range(h):
        for j in range(w):
            image[i][j][0] = 0
            image[i][j][2] = 0

    cv2.imshow("Filter Hijau", image)

    if cv2.waitKey(1) == 27:
        break

camera.release()
cv2.destroyAllWindows()

#webcam filter biru
import cv2

camera = cv2.VideoCapture(0)

while True:
    ok, image = camera.read()

    [h, w, c] = image.shape

    for i in range(h):
        for j in range(w):
            image[i][j][1] = 0
            image[i][j][2] = 0

    cv2.imshow("Filter Biru", image)

    if cv2.waitKey(1) == 27:
        break

camera.release()
cv2.destroyAllWindows()

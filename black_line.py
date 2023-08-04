import cv2

image = cv2.imread("monaliza.jpg", 0)

height, width = image.shape

for i in range(236):
    if i <= 200:
        for j in range(200-i, 236-i):
            image[i, j] = 0
    else:
        for j in range(0, 236-i):
            image[i, j] = 0


cv2.imshow("", image)
cv2.imwrite("black_line_pic.jpg", image)
cv2.waitKey()

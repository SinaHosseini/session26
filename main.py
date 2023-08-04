import cv2


my_image = cv2.imread("monaliza.jpg")
my_image2 = cv2.cvtColor(my_image, cv2.COLOR_BGR2GRAY)

# print(my_image.shape)

cv2.imshow("", my_image2)
cv2.waitKey()
cv2.imwrite("monaliza_gray.jpg", my_image2)

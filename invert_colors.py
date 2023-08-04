import cv2

image = cv2.imread("1.jpg")
image_2 = cv2.imread("2.jpg")

inverted = cv2.bitwise_not(image)
inverted_2 = cv2.bitwise_not(image_2)

cv2.imwrite("inverted_1.jpg", inverted)
cv2.imwrite("inverted_2.jpg", inverted_2)

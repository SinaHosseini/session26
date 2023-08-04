import cv2

image = cv2.imread("3.jpg")

h, w = image.shape[:2]
center = (w//2, h//2)

M = cv2.getRotationMatrix2D(center, 180, 1)

rotate_img = cv2.warpAffine(image, M, (w, h))

cv2.imwrite("rotate_img.jpg", rotate_img)

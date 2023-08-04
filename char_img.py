import cv2
import numpy as np

board = np.zeros((200, 200))
board[0:200, 0:200] = 255

board[20:25, 80:133] = 0
board[20:70, 80:85] = 0
board[70:75, 80:130] = 0
board[70:120, 128:133] = 0
board[117:122, 80:133] = 0


cv2.imshow("", board)
cv2.imwrite("char_img.jpg", board)
cv2.waitKey()

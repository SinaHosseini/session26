import cv2
import numpy

size = 64
board = numpy.zeros((size*8, size*8))

for row in range(8):
    for cell in range(8):
        board[row*size:(row+1)*size, cell*size:(cell+1)
              * size] = ((row+cell) % 2)*255

cv2.imshow("chess_board", board)
cv2.imwrite("chess_board.jpg", board)
cv2.waitKey()

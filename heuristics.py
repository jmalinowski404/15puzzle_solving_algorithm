from constants import *

import numpy as np

def hamming(board, solved_board):
    board_to_solve = np.array(board)
    s_board = np.array(solved_board)

    return np.sum(board_to_solve != s_board)

def manhattanBetweenPoints(a, b):
    distance = abs(a[0] - b[0]) + abs(a[1] - b[1])
    return distance 

def manhattanTotal(board_to_solve, solved_board):
    h_score = 0

    rows, cols = board_to_solve.shape

    for r in range(rows):
        for c in range(cols):
            if board_to_solve[r][c] != solved_board[r][c]:
                h_score += manhattanBetweenPoints(np.argwhere(board_to_solve == board_to_solve[r][c])[0], np.argwhere(solved_board == board_to_solve[r][c])[0])

    return h_score
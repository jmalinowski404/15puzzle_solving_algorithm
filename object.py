import numpy as np
from constants import *

class Node:
    def __init__(self, board, parent=None, move=None):
        self.board = board
        self.children = []
        self.parent = parent
        self.move = move

        if parent:
            self.depth = parent.depth + 1
        else:
            self.depth = 0

        zero_pos = np.argwhere(self.board == 0)[0]
        self.zero_row = zero_pos[0]
        self.zero_col = zero_pos[1]

    def getNeighbor(self, move):
        rows, cols = self.board.shape
        r, c = MOVES[move]
        new_row = self.zero_row + r
        new_col = self.zero_col + c

        if 0 <= new_row < rows and 0 <= new_col < cols:
            new_board = self.board.copy()
            new_board[self.zero_row][self.zero_col] = new_board[new_row][new_col]
            new_board[new_row][new_col] = 0
            return Node(new_board, self, move)
        
        return None

    def getPath(self):
        path = []
        node = self

        while node.move is not None:
            path.append(node.move)
            node = node.parent
        return list(reversed(path))
    
    def isSolved(self, SOLVED_BOARD=SOLVED_PUZZLE):
        return np.array_equal(self.board, SOLVED_BOARD)
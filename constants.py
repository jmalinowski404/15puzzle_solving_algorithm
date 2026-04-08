import numpy as np

SOLVED_PUZZLE = np.array([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 0]])
SHUFFLED_ARRAY = np.array([[1, 0, 3, 4], [5, 2, 6, 8], [9, 10, 7, 11], [13, 14, 15, 12]])
MOVES = {
    'L': (0, -1),
    'R': (0, 1),
    'U': (-1, 0),
    'D': (1, 0)
}
MAX_DEPTH = 7
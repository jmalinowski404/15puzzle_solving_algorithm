import numpy as np
import sys

from algorithms import bfs, dfs, astr
from object import Node
from constants import *
from heuristics import *

if __name__ == "__main__":
    args = sys.argv[1:]

    algorithm = args[0]
    order = args[1]
    file_to_solve = open(args[2])
    solution_file = args[3]
    stats_file = args[4]

    rows, cols = map(int, file_to_solve.readline().split())
    
    board = []
    s_board = []
    for r in range(rows):
        row = list(map(int, file_to_solve.readline().split()))
        board.append(row)

        s_row = []
        for c in range(cols):
            value = (r * cols) + c + 1

            if value == rows * cols:
                value = 0
                s_row.append(value)
            else:
                s_row.append(value)

        s_board.append(s_row)

    board_to_solve = np.array(board)
    solved_board = np.array(s_board)

    result = [];

    if algorithm.lower() == "bfs":
        result = bfs(board_to_solve, order)
    
    if algorithm.lower() == "dfs":
        result = dfs(board_to_solve, order)

    if algorithm.lower() == "astr":
        result = astr(board_to_solve, solved_board, order)

    path, vis_count, processed_count, max_depth, time_taken = result

    with open(solution_file, 'w') as file:
        file.write(str(len(path)) + "\n")
        for char in path:
            file.write(char + " ")

    with open(stats_file, 'w') as file:
        file.write(str(len(path)) + "\n")
        file.write(str(vis_count) + "\n")
        file.write(str(processed_count) + "\n")
        file.write(str(max_depth) + "\n")
        file.write(str(f"{time_taken * 1000:.3f}"))

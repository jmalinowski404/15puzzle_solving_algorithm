from object import Node
from constants import *
from heuristics import *

import time
import heapq

def bfs(board_to_solve, order='LRUD'):
    start = time.perf_counter()
    root = Node(board_to_solve)
    
    if root.isSolved():
        return root.getPath()
    
    queue = [root]
    visited = {tuple(root.board.flat)}
    counter = 0
    max_depth = 0

    while queue:
        current = queue.pop(0)
        counter += 1

        for move in order:
            child = current.getNeighbor(move)

            if child is None:
                continue

            if child.depth > max_depth:
                max_depth = child.depth
                
            board_tuple = tuple(child.board.flat)
            if board_tuple not in visited:
                visited.add(board_tuple)
                current.children.append(child)
                queue.append(child)
                
                if child.isSolved():
                    koniec = time.perf_counter()

                    path = child.getPath()
                    vis_count = len(visited)
                    time_taken = koniec - start

                    return [path, vis_count, counter, max_depth, time_taken]
        
    return -1

def dfs(board_to_solve, order='RLUD', max_depth=20):
    start = time.perf_counter()
    root = Node(board_to_solve)

    if root.isSolved():
        koniec = time.perf_counter()
        return [root.getPath(), 0, 0, 0, koniec - start]
    
    stack = [root]
    visited = {tuple(root.board.flat): 0}
    counter = 0
    max_depth_stat = 0

    while stack:
        current = stack.pop()
        counter += 1

        if current.depth >= max_depth:
            max_depth_stat = max_depth 
            continue
        
        for move in order:
            child = current.getNeighbor(move)

            if child is None:
                continue

            if child.depth > max_depth_stat:
                max_depth_stat = child.depth

            if child.isSolved():
                koniec = time.perf_counter()

                path = child.getPath()
                vis_count = len(visited)
                time_taken = koniec - start

                return [path, vis_count, counter, max_depth_stat, time_taken]

            board_tuple = tuple(child.board.flat)

            if board_tuple not in visited or visited[board_tuple] > child.depth:
                visited[board_tuple] = child.depth
                stack.append(child)

    koniec = time.perf_counter()
    return ["-1", len(visited), counter, max_depth_stat, koniec - start]
            
def astr(board_to_solve, solved_board, heurisitc):
    start = time.perf_counter()
    root = Node(board_to_solve)

    if root.isSolved():
        koniec = time.perf_counter()
        return [root.getPath(), 0, 0, 0, koniec - start]

    priority_queue = []
    visited = []
    tie_breaker = 0
    counter = 0
    max_depth = 0

    heapq.heappush(priority_queue, (0, tie_breaker, root))

    while priority_queue:
        priority, _, current = heapq.heappop(priority_queue)
        counter += 1

        if current.isSolved():
            koniec = time.perf_counter()

            path = current.getPath()
            vis_count = len(visited)
            time_taken = koniec - start

            return [path, vis_count, counter, max_depth, time_taken]
        
        visited.append(current)

        for move in MOVES:
            child = current.getNeighbor(move)
            f_score = 0
            g_score = 0
            h_score = 0

            if child not in visited and child is not None:
                g_score = child.depth

                if child.depth > max_depth:
                    max_depth = child.depth

                if heurisitc == "manh":
                    h_score = manhattanTotal(child.board, solved_board)

                if heurisitc == "hamm":
                    h_score = hamming(child.board, solved_board)

                f_score = g_score + h_score

                tie_breaker += 1
                heapq.heappush(priority_queue, (f_score, tie_breaker, child))

    koniec = time.perf_counter()
    return ["-1", len(visited), counter, max_depth, koniec - start]
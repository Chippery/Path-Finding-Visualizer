from collections import deque
import pygame

def bfs(matrix, start, target):
    rows, cols = len(matrix), len(matrix[0])
    visit = {start}
    parent = {}
    q = deque([start])

    moves = [[-1,0],[1,0],[0,-1],[0,1]]

    while q:
        for i in range(len(q)):
            r, c = q.popleft()

            if r < 0 or r == rows or c < 0 or c >= cols or matrix[r][c] == 2: # Check bounds
                continue

            yield (r,c)
            
            if (r, c) == target: # If reached apple
                print("Reached Apple")
                return visit

            for dr,dc in moves: # Move to neighbors
                nr = r + dr
                nc = c + dc
                if (nr, nc) not in visit:
                    q.append((nr, nc))
                    visit.add((nr, nc))
                    parent[(r + dr, c + dc)] = (r,c)
                    print(parent)
    print("No path to apple")
    return visit
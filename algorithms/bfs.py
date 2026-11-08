from collections import deque

def bfs(matrix, start, target, parent):
    rows, cols = len(matrix), len(matrix[0])
    visit = {start}

    
    q = deque([start])

    moves = [[-1,0],[1,0],[0,-1],[0,1]]

    while q:
        for i in range(len(q)):
            r, c = q.popleft()

            if r < 0 or r >= rows or c < 0 or c >= cols or matrix[r][c] == 2: # Check bounds
                continue

            yield (r,c)
            
            if (r, c) == target: # If reached apple
                print("Reached Apple")
                return 

            for dr,dc in moves: # Move to neighbors
                nr = r + dr
                nc = c + dc
                if (nr, nc) not in visit:
                    q.append((nr, nc))
                    visit.add((nr, nc))
                    if 0 <= nr < rows and  0 <= nc < cols:
                        parent[(nr, nc)] = (r,c)
                        
    print("No path to apple")
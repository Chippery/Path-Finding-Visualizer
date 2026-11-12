from collections import deque

def bfs(matrix, start, target, parent):
    rows, cols = len(matrix), len(matrix[0])
    visit = {start}

    
    q = deque([start])

    moves = [[-1,0],[1,0],[0,-1],[0,1]]

    while q:
        for i in range(len(q)):
            r, c = q.popleft()

            yield (r,c)
            
            if (r, c) == target: # If reached apple
                print("Reached Apple")
                return 

            for dr,dc in moves: # Move to neighbors
                nr = r + dr
                nc = c + dc
                if (nr, nc) not in visit: # Not already seen
                    q.append((nr, nc))
                    visit.add((nr, nc))
                    if 0 <= nr < rows and  0 <= nc < cols: # Not - coordinates
                        parent[(nr, nc)] = (r,c)
                        
    print("No path to apple")
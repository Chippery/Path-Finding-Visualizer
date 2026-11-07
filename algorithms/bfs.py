from collections import deque

found_path = []

def find(x, parent):
    found_path.append(x)
    
    while x != (0,0):
        found_path.append(parent[x])
        x = parent[x]
    found_path.reverse()

    for cell in found_path:
        yield cell
    
    return found_path[::-1]

def bfs(matrix, start, target, parent):
    rows, cols = len(matrix), len(matrix[0])
    visit = {start}

    
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
                # print(parent)

                return find(next(reversed(parent)), parent)

            for dr,dc in moves: # Move to neighbors
                nr = r + dr
                nc = c + dc
                if (nr, nc) not in visit:
                    q.append((nr, nc))
                    visit.add((nr, nc))
                    if 0 <= nr < rows and  0 <= nc < cols:
                        parent[(nr, nc)] = (r,c)
                    # for child, previous in parent.items():
                    #     print(f"{child} <- {previous}")
    print("No path to apple")
    return visit
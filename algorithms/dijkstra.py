import heapq

def dijkstra(matrix, start, target, parent):
    rows,cols = len(matrix), len(matrix[0])

    distances = {} # ((r,c) : distance from start))

    for r in range(rows):
        for c in range(cols):
            distances[(r, c)] = float('inf') # Go through each cell -> set dist to inf cs unknown
    distances[start] = 0

    moves = [[-1,0],[1,0],[0,-1],[0,1]]

    minHeap = [[0,start]]
    while minHeap:
        distance, (r,c) = heapq.heappop(minHeap)

        yield (r,c)

        if (r, c) == target: # If reached apple
            print(f"Reached Apple with distance of: {distance}")
            return 

        for dr,dc in moves: # Move to neighbors
            nr = r + dr
            nc = c + dc

            if (0 <= nr < rows and  0 <= nc < cols # In Bounds
                and matrix[nr][nc] != 2):          # Not a Wall

                new_dist = distances[(r,c)] + 1 # Determine distance of node from start

                if new_dist < distances[(nr, nc)]: # if dist to path is < previous path set it as new dist
                    distances[(nr, nc)] = new_dist
                    parent[(nr, nc)] = (r, c)

                    heapq.heappush(minHeap, (new_dist, (nr, nc)))
    print("No path to Apple")
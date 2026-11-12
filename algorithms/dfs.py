found_path = []

def dfs_matrix(matrix, start, target, parent):
    rows, cols = len(matrix), len(matrix[0])
    visit = set()

    moves = [[-1,0],[1,0],[0,-1],[0,1]]

    def dfs(r,c):
        visit.add((r, c))
        yield (r,c)

        if (r, c) == target:
            print("Reached Apple")
            return True

        for dr, dc in moves: # Explore Neighboring Cells
            nr = r + dr
            nc = c + dc

            if (0 <= nr < rows and 0 <= nc < cols # Inbounds
                and (nr, nc) not in visit         # Not already seen
                and matrix[nr][nc] != 2):         # not a wall

                parent[(nr, nc)] = (r, c) 

                found = yield from dfs(nr, nc)

                if found:
                    return True

        return False

    yield from dfs(*start)
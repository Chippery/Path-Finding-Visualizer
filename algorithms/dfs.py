found_path = []

def dfs_matrix(matrix, start, target, parent):
    rows, cols = len(matrix), len(matrix[0])
    visit = {start}

    moves = [[-1,0],[1,0],[0,-1],[0,1]]

    def dfs(r,c):
        if r < 0 or r == rows or c < 0 or c >= cols or matrix[r][c] == 2: # Check bounds
            return False

        visit.add((r, c))
        yield (r,c)


        if (r, c) == target:
            return True

        for dr, dc in moves:
            nr = r + dr
            nc = c + dc

            if (0 <= nr < rows and 0 <= nc < cols and (nr, nc) not in visit and matrix[nr][nc] != 2): # Check Bounds and if not a wall

                parent[(nr, nc)] = (r, c)

                found = yield from dfs(nr, nc)

                if found:
                    return True

        return False

    yield from dfs(*start)
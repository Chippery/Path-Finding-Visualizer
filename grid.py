import random

def create_grid(rows, cols):
    return [[0 for _ in range(cols)] for _ in range(rows)]


def place_apple(matrix):
    rows = len(matrix)
    cols = len(matrix[0])

    apple_row = random.randrange(rows)
    apple_col = random.randrange(cols)

    while apple_row != rows - 1 and apple_col != cols - 1:
        apple_row = random.randrange(rows)
        apple_col = random.randrange(cols)

    matrix[apple_row][apple_col] = 1

    return apple_row, apple_col


def generate_walls(matrix, percent):
    rows = len(matrix)
    cols = len(matrix[0])

    wall_count = min(int(rows * cols * percent), rows * cols - 2)

    for _ in range(wall_count):
        wall_row = random.randrange(rows)
        wall_col = random.randrange(cols)

        while matrix[wall_row][wall_col] != 0:
            wall_row = random.randrange(rows)
            wall_col = random.randrange(cols)

        matrix[wall_row][wall_col] = 2

    return matrix
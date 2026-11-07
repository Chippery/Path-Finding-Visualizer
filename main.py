import pygame
from grid import create_grid, place_apple, generate_walls
from algorithms.bfs import bfs

pygame.init()
clock = pygame.time.Clock()

width, height = 900, 600
rect_w, rect_l= 50,50 # Dimensions of grid
percent = 0.25

screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Visualizer")

col = len(range(rect_w, width - rect_w, rect_w))
row = len(range(rect_l, height - rect_l, rect_l))

matrix = create_grid(row, col)
matrix[0][0] = 3 # Start Point

apple_row, apple_col = place_apple(matrix) # Set apple at random x,y pos
matrix = generate_walls(matrix, percent)
matrix[apple_row][apple_col] = 1 # 1 = Not empty

start = (0,0)
target = (apple_row,apple_col)

bfs_steps = bfs(matrix, start, target)

for r in range(row):
    for c in range(col):
        color = (255,255,255)

        if matrix[r][c] == 0:
            color = (255, 255, 255)  # Empty
        elif matrix[r][c] == 1:
            color = (255, 0, 0)      # Apple
        elif matrix[r][c] == 2:
            color = (0, 255, 0)      # Wall
        elif matrix[r][c] == 3:
            color = (0, 0, 255)      # Start

        x = (c + 1) * rect_w    # +1 Add margin
        y = (r + 1) * rect_l

        pygame.draw.rect(screen, color, (x, y, rect_w, rect_l))
        pygame.draw.rect(screen, (26, 43, 130),(x, y, rect_w, rect_l), width=1)
print(f"Apple at: ({apple_col},{apple_row})") # apple_col = x, apple_row = y

run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    step = next(bfs_steps, None)

    if step is not None:
        r, c = step

        x = (c + 1) * rect_w
        y = (r + 1) * rect_l

        pygame.draw.rect(screen, (255, 255, 0), (x, y, rect_w, rect_l))
        pygame.draw.rect(screen, (26, 43, 130), (x, y, rect_w, rect_l), width=1)

    pygame.display.flip()
    clock.tick(4)
pygame.quit()
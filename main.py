import pygame
from grid import create_grid, place_apple, generate_walls

pygame.init()

width, height = 900, 600
rect_w, rect_l= 50,50 # Dimensions of grid
percent = 0.5

screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Visualizer")

col = len(range(rect_w, width - rect_w, rect_w))
row = len(range(rect_l, height - rect_l, rect_l))

matrix = create_grid(row, col)
matrix[0][0] = 3 # Start Point

apple_row, apple_col = place_apple(matrix) # Set apple at random x,y pos

matrix = generate_walls(matrix, 0.35)

matrix[apple_row][apple_col] = 1 # 1 = Not empty

start = pygame.draw.rect(screen, (0,0,255), (rect_w, rect_l, rect_w, rect_l))
apple = pygame.draw.rect(screen, (255,0,0), ((apple_col + 1)* rect_w, (apple_row + 1) * rect_l, rect_w, rect_l))
walls = 0

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
print(matrix)

run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    pygame.display.flip()
pygame.quit()
import pygame
import random

pygame.init()

width, height = 900, 600
rect_w, rect_l= 50,50 # Dimensions of grid
percent = 0.5

screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Visualizer")

col = len(range(rect_w, width - rect_w, rect_w))
row = len(range(rect_l, height - rect_l, rect_l))

for i in range(rect_w, (width-rect_w), rect_w): # Cols, stop 1 rect before edge of window, step by rectangle width
    for j in range(rect_l, (height-rect_l), rect_l): # Rows, stop 1 rect before edge of window, step by rectangle length
        pygame.draw.rect(screen, (255,255,255), (i, j, rect_w, rect_l)) # Make bg rects -> (x, y, width, length)

matrix = [[0 for _ in range(col)] for _ in range(row)] # reference coord matrix[row][col]
apple_col, apple_row = random.randrange(col), random.randrange(row) # Set apple at random x,y pos

if random.choice([True, False]):
    apple_row = random.randrange(row)
    apple_col = col - 1  # Last column
else:
    apple_row = row - 1  # Last row
    apple_col = random.randrange(col)

matrix[apple_row][apple_col] = 1 # 1 = Not empty
print(f"Apple at: ({apple_col},{apple_row})") # apple_col = x, apple_row = y

start = pygame.draw.rect(screen, (0,0,255), (rect_w, rect_l, rect_w, rect_l))
apple = pygame.draw.rect(screen, (255,0,0), ((apple_col + 1)* rect_w, (apple_row + 1) * rect_l, rect_w, rect_l))
walls = 0

for j in range(int((row * col) * percent )): # Cover percent% of board with walls
    wall_x, wall_y = random.randrange(col), random.randrange(row)

    while (wall_x, wall_y) == (apple_col, apple_row) or (wall_x, wall_y) == (0, 0): # Change wall pos if on apple/start
        wall_x = random.randrange(col)
        wall_y = random.randrange(row)
        print("Wall landed on apple/starting point")

    pygame.draw.rect(screen, (0,255,0), ((wall_x + 1) * rect_w, (wall_y + 1) * rect_l, rect_w, rect_l))

    matrix[wall_y][wall_x] = 2

    walls += 1

for i in range(rect_w, (width-rect_w), rect_w): # Make borders after walls, apples, paths
    for j in range(rect_l, (height-rect_l), rect_l):
        pygame.draw.rect(screen, (26, 43, 130), (i, j, rect_w, rect_l), width=1) 
print(f'Number of walls: {walls}/{row*col}')

print(matrix)

run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    pygame.display.flip()
pygame.quit()
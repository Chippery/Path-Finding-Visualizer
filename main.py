import pygame
import random

pygame.init()

width, height = 900, 600
rect_w, rect_l= 50, 50

screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Visualizer")

col = len(range(rect_w, width - rect_w, rect_w))
row = len(range(rect_l, height - rect_l, rect_l))

for i in range(rect_w, (width-rect_w), rect_w): # Cols, stop 1 rect before edge of window, step by rectangle width
    for j in range(rect_l, (height-rect_l), rect_l): # Rows, stop 1 rect before edge of window, step by rectangle length
        pygame.draw.rect(screen, (255,255,255), (i, j, rect_w, rect_l))
        pygame.draw.rect(screen, (26, 43, 130), (i, j, rect_w, rect_l), width=1) # Create Rectangle -> (x, y, width, length)

matrix = [[0 for _ in range(col)] for _ in range(row)] # reference coord matrix[row][col]
apple_row, apple_col = random.randrange(row), random.randrange(col) # Set apple at random x,y pos

matrix[apple_row][apple_col] = 1 # 1 = Not empty
print(f"Apple at: ({apple_col},{apple_row})") # apple_col = x, apple_row = y

start = pygame.draw.rect(screen, (0,0,255), (rect_w, rect_l, rect_w, rect_l))
apple = pygame.draw.rect(screen, (255,0,0), ((apple_col + 1)* rect_l, (apple_row + 1) * rect_w,rect_w, rect_l)) # apple_col/row + 1 cs not starting at 0

run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    pygame.display.flip()
pygame.quit()
import pygame

pygame.init()

width, height = 900, 600

rect_w, rect_l= 50, 50

screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Visualizer")

run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    row = 0
    col = 0
    for i in range(rect_w, (width-rect_w), rect_w): # Cols, stop 1 rect before edge of window, step by rectangle width
        col += 1
        for j in range(rect_l, (height-rect_l), rect_l): # Rows, stop 1 rect before edge of window, step by rectangle length
            pygame.draw.rect(screen, (255,255,255), (i, j, rect_w, rect_l))
            pygame.draw.rect(screen, (26, 43, 130), (i, j, rect_w, rect_l), width=1) # Create Rectangle -> (x, y, width, length)
            row += 1
    row = int(row / col)
    # print(f"{col} {int(row / col)}") 

    matrix = [[0 for _ in range(col)] for _ in range(row)]

    pygame.display.flip()
print(matrix)
pygame.quit()
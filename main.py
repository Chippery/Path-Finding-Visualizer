import pygame

pygame.init()

width = 800
height = 600

rect_w = 25
rect_l = 25

screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Visualizer")

run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    for i in range(rect_w, (width-rect_w), rect_w): # Rows, stop 1 rect before edge of window, step by rectangle width
        for j in range(rect_l, (height-rect_l), rect_l): # Cols, stop 1 rect before edge of window, step by rectangle length
            pygame.draw.rect(screen, (255, 0, 0), (i, j, rect_w, rect_l), width=1) # Create Rectangle -> (x, y, width, length)

    pygame.display.flip()

pygame.quit()
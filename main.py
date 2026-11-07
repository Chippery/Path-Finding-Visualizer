import pygame

pygame.init()

width = 800
height = 600
rect_w = 50
rect_l = 50

screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Visualizer")

run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    for i in range(rect_w, (width-50), 100):
        for j in range(rect_l, (height-50), 100):
            pygame.draw.rect(screen, (255, 0, 0), (i, j, rect_w, rect_l), width=1) # Create Rectangle -> (x, y, width, length)
    # pygame.draw.rect(screen, (255, 0, 0), (150, 50, 100, 100), width=1)

    pygame.display.flip()

pygame.quit()
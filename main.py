import pygame
from grid import create_grid, place_apple, generate_walls
from algorithms.bfs import bfs, find

pygame.init()
clock = pygame.time.Clock()

width, height = 900, 600
rect_w, rect_l= 50,50 # Dimensions of grid
percent = 0.25

def draw_grid(screen, matrix):
    for r in range(len(matrix)):
        for c in range(len(matrix[0])):
            x = (c + 1) * rect_w
            y = (r + 1) * rect_l

            # Choose the color based on the cell
            if matrix[r][c] == 2:
                color = (0, 0, 0)       # Wall
            elif matrix[r][c] == 1:
                color = (255, 0, 0)     # Apple
            elif matrix[r][c] == 3:
                color = (0, 255, 255)   # Start
            else:
                color = (255, 255, 255) # Empty

            pygame.draw.rect(screen, color, (x, y, rect_w, rect_l))
            if matrix[r][c] != 2:
                pygame.draw.rect(screen, (26, 43, 130), (x, y, rect_w, rect_l), 1)

screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Visualizer")

buttons = {
    "BFS": pygame.Rect(50, 10, 100, 40),
    "DFS": pygame.Rect(160, 10, 100, 40),
    "Dijkstra": pygame.Rect(270, 10, 100, 40),
    "A*": pygame.Rect(380, 10, 100, 40)
}

font = pygame.font.SysFont(None, 25)

# Inside your game loop
for name, button in buttons.items():
    pygame.draw.rect(screen, (70, 150, 255), button)

    text = font.render(name, True, (255, 255, 255))
    text_rect = text.get_rect(center=button.center)

    screen.blit(text, text_rect)

button_rect = pygame.Rect(50, 10, 100, 25)
BUTTON_COLOR = (0, 128, 255)
HOVER_COLOR = (0, 200, 255)
font = pygame.font.SysFont(None, 25)

selected_algorithm = "BFS"

col = len(range(rect_w, width - rect_w, rect_w))
row = len(range(rect_l, height - rect_l, rect_l))

matrix = create_grid(row, col)
matrix[0][0] = 3 # Start Point

apple_row, apple_col = place_apple(matrix) # Set apple at random x,y pos
matrix = generate_walls(matrix, percent)
matrix[apple_row][apple_col] = 1 # 1 = Not empty

start = (0,0)
target = (apple_row,apple_col)
draw_grid(screen,matrix)

print(f"Apple at: ({apple_col},{apple_row})") # apple_col = x, apple_row = y

parent = {}
bfs_steps = bfs(matrix, start, target, parent)
path_steps = find(target, parent)

bfs_finished = False

run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

        # Listen for a mouse button click
        if event.type == pygame.MOUSEBUTTONDOWN:
            # event.button == 1 checks for the LEFT mouse click
            if event.button == 1:
                # Check if the mouse click happened inside our button's rectangle
                if button_rect.collidepoint(event.pos):
                    parent = {}
                    bfs_finished = False
                    path_steps = None
                    bfs_steps = bfs(matrix, start, target, parent)

                    draw_grid(screen, matrix)

    if not bfs_finished:    # Bfs searching
        step = next(bfs_steps, None)

        if step is not None:
            r, c = step

            x = (c + 1) * rect_w
            y = (r + 1) * rect_l

            pygame.draw.rect(screen, (255, 255, 0), (x, y, rect_w, rect_l))
            pygame.draw.rect(screen, (26, 43, 130), (x, y, rect_w, rect_l), width=1)
        else:
            bfs_finished = True

            if target in parent:
                path_steps = find(target, parent)
            else:
                print("No path found!")

    elif path_steps is not None:     # Make found path
        path = next(path_steps, None)

        if path is not None:
            r, c = path

            x = (c + 1) * rect_w
            y = (r + 1) * rect_l

            pygame.draw.rect(screen, (0, 255, 0), (x, y, rect_w, rect_l))
            pygame.draw.rect(screen, (26, 43, 130), (x, y, rect_w, rect_l), width=1)

    for name, button in buttons.items():    # Draw Buttons
        pygame.draw.rect(screen, (70, 150, 255), button)

        text = font.render(name, True, (255, 255, 255))
        text_rect = text.get_rect(center=button.center)

        screen.blit(text, text_rect)

    pygame.display.flip()
    clock.tick(5)
pygame.quit()
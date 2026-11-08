import pygame
from grid import create_grid, place_apple, generate_walls
from algorithms.bfs import bfs, find
from algorithms.dfs import dfs_matrix

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

def animate_search(screen, steps, finished, parent, target):
    if steps is not None and not finished: # If algorithm exists and isn't finished
        step = next(steps, None)

        if step is not None:
            r, c = step

            x = (c + 1) * rect_w
            y = (r + 1) * rect_l

            pygame.draw.rect(screen, (255, 255, 0), (x, y, rect_w, rect_l))
            pygame.draw.rect(screen, (26, 43, 130), (x, y, rect_w, rect_l), width=1)

        else:
            finished = True

            if target in parent:
                path_steps = find(target, parent)
            else:
                path_steps = None
                print("No path found!")

            return finished, path_steps

    return finished, None

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

# Steps returns generator of which cells algorithm will visit next
bfs_steps = None
dfs_steps = None
path_steps = None # Generates coordinates from start to apple of correct path

bfs_finished = True
dfs_finished = True
dijkstra_finished = False
a_star = False

parent = {}

draw_grid(screen, matrix)

run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

        # Listen for a mouse button click
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                for name, rect in buttons.items():
                    if rect.collidepoint(event.pos):
                        if name == "BFS":
                            print("Selected BFS")

                            parent = {}
                            bfs_finished = False
                            path_steps = None
                            bfs_steps = bfs(matrix, start, target, parent)
                            
                            draw_grid(screen, matrix)
                            
                        elif name == "DFS":
                            print("Selected DFS")

                            parent = {}
                            dfs_finished = False
                            bfs_finished = True
                            path_steps = None
                            dfs_steps = dfs_matrix(matrix, start, target, parent)

                            draw_grid(screen, matrix)

                        elif name == "Dijkstra":
                            print("Selected Dijkstra")
                        elif name == "A*":
                            print("Selected A*")

    if bfs_steps is not None and not bfs_finished: # Bfs Search
        bfs_finished, new_path = animate_search(screen, bfs_steps, bfs_finished, parent, target)

        if new_path is not None: # If path isn't finished
            path_steps = new_path

    elif dfs_steps is not None and not dfs_finished:
        dfs_finished, new_path = animate_search(screen, dfs_steps, dfs_finished, parent, target)

        if new_path is not None:
            path_steps = new_path

    elif path_steps is not None:    # Draw correct Path
        path = next(path_steps, None)

        if path is not None:
            r, c = path

            x = (c + 1) * rect_w
            y = (r + 1) * rect_l

            pygame.draw.rect(screen, (0, 255, 0), (x, y, rect_w, rect_l))
            pygame.draw.rect(screen, (26, 43, 130), (x, y, rect_w, rect_l), width=1)
        else:
            path_steps = None

    for name, button in buttons.items():    # Draw Buttons
        pygame.draw.rect(screen, (70, 150, 255), button)

        text = font.render(name, True, (255, 255, 255))
        text_rect = text.get_rect(center=button.center)

        screen.blit(text, text_rect)

    pygame.display.flip()
    clock.tick(5)
pygame.quit()
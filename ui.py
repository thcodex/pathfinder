import pygame
from node import make_grid
from search import search_algorithm


GREY = (126, 126, 126)
WHITE = (255, 255, 255)

pygame.display.set_caption("Pathfinder")

# Drawing the grid in our UI
def draw_grid(win, rows, width):
    gap = width // rows
    for i in range(rows):
        # Drawing horizontal lines
        pygame.draw.line(win, GREY, (0, i * gap), (width, i * gap))
        for j in range(rows):
            # Drawing vertical lines
            pygame.draw.line(win, GREY, (j * gap, 0), (j * gap, width))

# Main draw function that draws everything on the UI
def draw(win, grid, rows, width):
    win.fill(WHITE)

    for row in grid:
        for node in row:
            node.draw(win)
    
    draw_grid(win, rows, width)
    pygame.display.update()

def get_clicked_pos(pos, rows, width):
    gap = width // rows

    y, x = pos
    row = y // gap
    col = x // gap

    return row, col

def game_loop(win, width):
    ROWS = 50
    grid = make_grid(ROWS, width)

    start = None
    end = None

    run = True
    started = False

    while run:
        draw(win, grid, ROWS, width)
        # Handling events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            
            if pygame.mouse.get_pressed()[0]: # LEFT button
                pos = pygame.mouse.get_pos()
                row, col = get_clicked_pos(pos, ROWS, width)
                node = grid[row][col]

                if not start and node != end:
                    start = node
                    start.change_color("start")
                
                elif not end and node != start:
                    end = node
                    end.change_color("end")

                elif node != start and node != end:
                    node.change_color("barrier")

            elif pygame.mouse.get_pressed()[2]: # RIGHT button
                pos = pygame.mouse.get_pos()
                row, col = get_clicked_pos(pos, ROWS, width)
                node = grid[row][col]
                node.reset()

                # Handle start/end nodes if reseted
                if node == start:
                    start = None
                elif node == end:
                    end = None

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE and start and end:
                    for row in grid:
                        for node in row:
                            node.update_neighbors(grid)
                    
                    # Call A* algorithm
                    search_algorithm(lambda: draw(win, grid, ROWS, width), grid, start, end)
                
                if event.key == pygame.K_c:
                    start = None
                    end = None
                    grid = make_grid(ROWS, width)

    pygame.quit()
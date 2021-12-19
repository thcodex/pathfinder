import pygame


GREY = (126, 126, 126)
WHITE = (255, 255, 255)

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
    pass
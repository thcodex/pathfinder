import pygame


# Colors that will be used
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
PURPLE = (128, 0, 128)
ORANGE = (255, 165, 0)
TURQUOISE = (64, 224, 208)

class Node:
    """Class for every node in our visualizer"""

    def __init__(self, row, col, width, total_rows):
        self.row = row
        self.col = col
        self.width = width
        self.x = row * width
        self.y = col * width
        self.color = WHITE
        self.neighbors = []
        self.total_rows = total_rows
        
    def change_color(self, type):
        """Change color of node"""
        match type:
            case "start":
                self.color = TURQUOISE
            case "end":
                self.color = ORANGE
            case "barrier":
                self.color = BLACK
            case "closed":
                self.color = RED
            case "open":
                self.color = GREEN
            case "path":
                self.color = PURPLE

    def is_barrier(self):
        return self.color == BLACK

    def reset(self):
        self.color = WHITE

    def get_pos(self):
        return self.row, self.col

    def draw(self, win):
        pygame.draw.rect(win, self.color, (self.x, self.y, self.width, self.width))

    def update_neighbors(self, grid):
        self.neighbors = []
        
        # DOWN
        if self.row < self.total_rows - 1 and not grid[self.row + 1][self.col].is_barrier():
            self.neighbors.append(grid[self.row + 1][self.col])
        # UP
        if self.row > 0 and not grid[self.row - 1][self.col].is_barrier():
            self.neighbors.append(grid[self.row - 1][self.col])
        # RIGHT
        if self.col < self.total_rows - 1 and not grid[self.row][self.col + 1].is_barrier():
            self.neighbors.append(grid[self.row][self.col + 1])
        # LEFT
        if self.col > 0 and not grid[self.row][self.col - 1].is_barrier():
            self.neighbors.append(grid[self.row][self.col - 1])

    def __lt__(self, other):
        return False


# Creating our grid with nodes
def make_grid(rows, width):
    grid = []
    gap = width // rows

    for i in range(rows):
        grid.append([])
        for j in range(rows):
            node = Node(i, j, gap, rows)
            grid[i].append(node)

    return grid

def build_path(came_from, current, draw):
    while current in came_from:
        current = came_from[current]
        current.change_color("path")
        draw()
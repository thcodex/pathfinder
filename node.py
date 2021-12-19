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
        self.type = ""

    @property
    def type(self):
        return self.state

    @type.setter
    def type(self, value):
        self.type = value
        # setting color to whatever node type is
        match value:
            case "open":
                self.color = GREEN
            case "barrier":
                self.color = BLACK
            case "closed":
                self.color = RED
            case "start":
                self.color = ORANGE
            case "end":
                self.color = TURQUOISE
            case "path":
                self.color = PURPLE
            case _:
                self.color = WHITE

    def get_pos(self):
        return self.row, self.col

    def draw(self, win):
        pygame.draw.rect(win, self.color, (self.x, self.y, self.width, self.width))

    def update_neighbors(self, grid):
        pass

    def __lt__(self, other):
        pass
from app.ui import game_loop
import pygame


if __name__ == "__main__":
    pygame.init()
    WIDTH = 800
    win = pygame.display.set_mode((WIDTH, WIDTH))
    game_loop(win, WIDTH)
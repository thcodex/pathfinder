from app.ui import game_loop
import pygame


if __name__ == "__main__":
    pygame.init()
    win = pygame.display.set_mode((800, 800))
    game_loop(win, 800)
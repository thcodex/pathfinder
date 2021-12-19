""" This module implement the search algorithm for this pathfinder """
from queue import PriorityQueue
import pygame
from .node import build_path


# Defining heuristic function
def h(p1, p2):
    # Manhattan distance: sum for i in N |v1[i] - v2[i]|
    return sum(abs(v1 - v2) for v1, v2 in zip(p1, p2))


def search_algorithm(draw, grid, start, end):
    """Implementation of A* algorithm"""
    count = 0
    open_set = PriorityQueue()
    open_set.put((0, count, start))
    came_from = {}
    g_score = {node: float("inf") for row in grid for node in row}
    g_score[start] = 0
    f_score = {node: float("inf") for row in grid for node in row}
    f_score[start] = h(start.get_pos(), end.get_pos())

    open_set_hash = {start}

    while not open_set.empty():
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

        current = open_set.get()[2]
        open_set_hash.remove(current)

        if current == end:
            # make path
            build_path(came_from, end, draw)
            end.change_color("end")
            start.change_color("start")
            return True

        for neighbor in current.neighbors:
            temp_g_score = g_score[current] + 1

            if temp_g_score < g_score[neighbor]:
                came_from[neighbor] = current
                g_score[neighbor] = temp_g_score
                f_score[neighbor] = temp_g_score + h(neighbor.get_pos(), end.get_pos())
                if neighbor not in open_set_hash:
                    count += 1
                    open_set.put((f_score[neighbor], count, neighbor))
                    open_set_hash.add(neighbor)
                    neighbor.change_color("open")
        
        draw()

        if current != start:
            current.change_color("closed")
    
    return False
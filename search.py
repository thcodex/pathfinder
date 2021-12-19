""" This module implement the search algorithm for this pathfinder """

# Defining heuristic function
def h(p1, p2):
    # Manhattan distance: sum for i in N |v1[i] - v2[i]|
    return sum(abs(v1 - v2) for v1, v2 in zip(p1, p2))


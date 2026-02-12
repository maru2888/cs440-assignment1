# Part 2: repeated forward A* loop
from algorithms.astar import astar
from env.grid import FREE


def repeated_forward_astar(start, goal, grid, tie_mode):
    """
    For Part 2 we assume full grid knowledge (no sensing yet).
    Replanning still works fine.
    """

    current = start
    total_expanded = 0

    while current != goal:
        path, expanded = astar(current, goal, grid, tie_mode=tie_mode)
        total_expanded += expanded

        if path is None:
            return None, total_expanded

        # move one step along path
        if len(path) > 1:
            current = path[1]
        else:
            break

    return True, total_expanded

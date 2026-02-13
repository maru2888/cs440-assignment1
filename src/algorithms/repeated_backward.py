# Part 3: repeated backward A* loop
from algorithms.astar import astar

def repeated_backward_astar(start, goal, grid, tie_mode="larger_g"):
    current = start
    total_expanded = 0

    while current != goal:
        path, expanded = astar(goal, current, grid, tie_mode=tie_mode)
        total_expanded += expanded

        if path is None:
            return None, total_expanded

        path = list(reversed(path))

        # move one step toward the goal
        if len(path) > 1:
            current = path[1]
        else:
            break
            
    return True, total_expanded
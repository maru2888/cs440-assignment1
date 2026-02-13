from algorithms.astar import astar
from env.grid import FREE, BLOCKED, neighbors

def sense_and_update(current, true_grid, known_grid):
    r, c = current
    known_grid[r][c] = FREE
    for nr, nc in neighbors(r, c):
        known_grid[nr][nc] = true_grid[nr][nc]

def repeated_backward_astar_sense(start, goal, true_grid, tie_mode="larger_g"):
    known_grid = [[FREE for _ in range(101)] for _ in range(101)]

    current = start
    total_expanded = 0
    moves = 0

    MAX_MOVES = 101 * 101 * 4 # safety cap

    while current != goal and moves < MAX_MOVES:
        sense_and_update(current, true_grid, known_grid)

        path, expanded = astar(goal, current, known_grid, tie_mode=tie_mode)
        total_expanded += expanded

        if path is None:
            return None, total_expanded, moves

        path = list(reversed(path))  

        if len(path) <= 1:
            break
        nxt = path[1]

        if true_grid[nxt[0]][nxt[1]] == BLOCKED:
            known_grid[nxt[0]][nxt[1]] = BLOCKED
        else:
            current = nxt
            moves += 1
            
    if current != goal:
        return None, total_expanded, moves
    return True, total_expanded, moves

from algorithms.astar import astar
from env.grid import FREE, BLOCKED, neighbors

def sense_and_update(current, true_grid, known_grid):
    r, c = current
    known_grid[r][c] = FREE
    for nr, nc in neighbors(r, c):
        known_grid[nr][nc] = true_grid[nr][nc]

def repeated_forward_adaptive_astar_sense(start, goal, true_grid, tie_mode="larger_g"):
    known_grid = [[FREE for _ in range(101)] for _ in range(101)]
    h_table = {} #Adaptive heuristics: state -> h(state)

    current = start
    total_expanded = 0
    moves = 0
    MAX_MOVES = 101 * 101 * 4

    while current != goal and moves < MAX_MOVES:
        sense_and_update(current, true_grid, known_grid)

        path, expanded, closed, g = astar(
            current, goal, known_grid,
            tie_mode=tie_mode,
            h_table=h_table,
            return_closed=True
        )
        total_expanded += expanded

        if path is None:
            return None, total_expanded, moves
        
        # Adaptive update: h(s) = g(goal) - g(s) for all expanded s
        if goal in g:
            g_goal = g[goal]
            for s in closed:
                if s in g:
                    h_table[s] = g_goal - g[s]


        # move 1 step along planned path
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


    

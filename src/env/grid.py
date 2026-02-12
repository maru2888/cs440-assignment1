# grid representation + neighbors
BLOCKED = 1
FREE = 0
ROWS = 101
COLS = 101
DIRS = [(-1, 0), (1, 0), (0, -1), (0, 1)]

def in_bounds(r, c):
    return 0 <= r < ROWS and 0 <= c < COLS

def neighbors(r, c):
    for dr, dc in DIRS:
        nr, nc = r + dr, c + dc
        if in_bounds(nr, nc):
            yield nr, nc

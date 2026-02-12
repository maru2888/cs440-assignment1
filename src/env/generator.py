# Part 0: DFS maze generation
import random

BLOCKED = 1
FREE = 0
ROWS = 101
COLS = 101
DIRS = [(-1, 0), (1, 0), (0, -1), (0, 1)]

def in_bounds(r, c):
    return 0 <= r < ROWS and 0 <= c < COLS

def generate_single_world(seed, block_prob=0.3):
    """
    Generates ONE 101x101 gridworld.

    Idea:
    - Start fully blocked
    - DFS through grid
    - When a cell is first visited:
        30% chance it stays blocked
        70% chance it becomes free and DFS continues
    """
    random.seed(seed)

    grid = [[BLOCKED for _ in range(COLS)] for _ in range(ROWS)]
    visited = [[False for _ in range(COLS)] for _ in range(ROWS)]

    # random start so worlds don't all look the same
    sr = random.randrange(ROWS)
    sc = random.randrange(COLS)

    stack = [(sr, sc)]
    visited[sr][sc] = True
    grid[sr][sc] = FREE  # force starting cell free

    while stack:
        r, c = stack[-1]

        # find neighbors we haven't seen yet
        neighbors = []
        for dr, dc in DIRS:
            nr, nc = r + dr, c + dc
            if in_bounds(nr, nc) and not visited[nr][nc]:
                neighbors.append((nr, nc))

        if not neighbors:
            # dead end -> backtrack
            stack.pop()
            continue

        nr, nc = random.choice(neighbors)
        visited[nr][nc] = True

        # this is the "30% chance of blocking newly visited neighbors"
        if random.random() < block_prob:
            grid[nr][nc] = BLOCKED
        else:
            grid[nr][nc] = FREE
            stack.append((nr, nc))

    return grid


def generate_worlds(base_seed, num_worlds=50):
    """
    Generates multiple worlds deterministically.
    World i uses seed = base_seed + i
    """
    worlds = []
    for i in range(num_worlds):
        worlds.append(generate_single_world(base_seed + i))
    return worlds

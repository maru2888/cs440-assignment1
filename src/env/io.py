# save_world / load_world
def save_world(grid, path):
    """
    Saves grid as text:
    0 = free
    1 = blocked
    """
    with open(path, "w") as f:
        for row in grid:
            f.write("".join(str(cell) for cell in row) + "\n")

def load_world(path):
    grid = []
    with open(path, "r") as f:
        for line in f:
            grid.append([int(c) for c in line.strip()])
    return grid

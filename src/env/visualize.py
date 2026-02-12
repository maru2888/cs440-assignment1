# ASCII + matplotlib renderers
import matplotlib.pyplot as plt

BLOCKED = 1
FREE = 0

def render_ascii(grid, start=None, goal=None, known=None):
    """
    Simple ASCII renderer.
    known: optional grid of what agent knows later (ignored for Part 0)
    """
    for r in range(len(grid)):
        row = ""
        for c in range(len(grid[0])):
            if start == (r, c):
                row += "S"
            elif goal == (r, c):
                row += "G"
            elif grid[r][c] == BLOCKED:
                row += "#"
            else:
                row += "."
        print(row)

def render_matplotlib(grid, start=None, goal=None):
    """
    Clean visualization for screenshots / report.
    """
    plt.imshow(grid, cmap="gray_r")

    if start:
        plt.scatter(start[1], start[0], c="green", s=40)
    if goal:
        plt.scatter(goal[1], goal[0], c="red", s=40)

    plt.xticks([])
    plt.yticks([])
    plt.show()
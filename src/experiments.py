# runs all 50 worlds + collects metrics
from env.io import load_world
from algorithms.repeated_forward import repeated_forward_astar
from algorithms.repeated_backward import repeated_backward_astar

from algorithms.repeated_forward_sense import repeated_forward_astar_sense
from algorithms.repeated_backward_sense import repeated_backward_astar_sense


DATA_DIR = "data/grids"


def run_part2():
    small_g = []
    large_g = []

    start = (0, 0)
    goal = (100, 100)

    for i in range(50):
        grid = load_world(f"{DATA_DIR}/world_{i:02d}.txt")

        _, exp_small = repeated_forward_astar(start, goal, grid, "smaller_g")
        _, exp_large = repeated_forward_astar(start, goal, grid, "larger_g")

        small_g.append(exp_small)
        large_g.append(exp_large)

    print("\n===== PART 2 RESULTS =====")
    print(f"Mean expanded (smaller g): {sum(small_g)/len(small_g):.2f}")
    print(f"Mean expanded (larger g):  {sum(large_g)/len(large_g):.2f}")

# PART 3 FUNCTION
def run_part3():
    forward = []
    backward = []
    start = (0,0)
    goal = (100, 100)

    for i in range(50):
        print(f"[Part 3] Grid {i}: loading...")
        true_grid = load_world(f"{DATA_DIR}/world_{i:02d}.txt")

        true_grid[0][0] = 0
        true_grid[100][100] = 0

        print(f"[Part 3] Grid {i}: forward start")
        _, exp_f, _ = repeated_forward_astar_sense(start, goal, true_grid, "larger_g")
        print(f"[Part 3] Grid {i}: forward done (expanded={exp_f})")

        print(f"[Part 3] Grid {i}: backward start")
        _, exp_b, _ = repeated_backward_astar_sense(start, goal, true_grid, "larger_g")
        print(f"[Part 3] Grid {i}: backward done (expanded={exp_b})")

        forward.append(exp_f)
        backward.append(exp_b)
    
    print("\n===== PART 3 RESULTS =====")
    print(f"Mean expanded (forward, larger g): {sum(forward)/len(forward):.2f}")
    print(f"Mean expanded (backward, larger g): {sum(backward)/len(backward):.2f}")


# runs all 50 worlds + collects metrics
from env.io import load_world
from algorithms.repeated_forward import repeated_forward_astar

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

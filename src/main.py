# entry point (run experiments / demos)

from env.generator import generate_worlds
from env.io import save_world, load_world
from env.visualize import render_ascii, render_matplotlib
from experiments import run_part2, run_part3

import os

DATA_DIR = "data/grids"


def main():
    os.makedirs(DATA_DIR, exist_ok=True)

    if not os.listdir(DATA_DIR):
        print("No grids found — generating worlds...")
        BASE_SEED = 440
        worlds = generate_worlds(BASE_SEED)

        for i, grid in enumerate(worlds):
            path = f"{DATA_DIR}/world_{i:02d}.txt"
            save_world(grid, path)

        print("Saved 50 gridworlds.")
    else:
        print("Grids already exist — skipping generation.")

    test_world = load_world(f"{DATA_DIR}/world_00.txt")

    start = (0, 0)
    goal = (100, 100)

    print("\nASCII preview:")
    render_ascii(test_world, start=start, goal=goal)

    #print("\nMatplotlib preview:")
    #render_matplotlib(test_world, start=start, goal=goal)

    run_part2()
    run_part3()



if __name__ == "__main__":
    main()

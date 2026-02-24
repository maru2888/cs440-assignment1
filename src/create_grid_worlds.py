from env.generator import generate_worlds
import pickle
import os

worlds = generate_worlds(base_seed=440, num_worlds=50)

os.makedirs("data/grids", exist_ok=True)

with open("data/grids/worlds.pkl", "wb") as f:
    pickle.dump(worlds, f)

print("Saved 50 gridworlds.")
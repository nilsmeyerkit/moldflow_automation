"""Create a configuration file with several random models."""
import yaml
import numpy as np

# Number of models
N = 10
# Number of injection locations per model
M = 5

# Create uniformly distributed random data
x_plate = np.random.randint(20, 100, N)
y_plate = np.random.randint(20, 100, N)
n_hole = np.random.randint(0, 3, N)

models = {}

for i, (x, y, n) in enumerate(zip(x_plate, y_plate, n_hole)):
    # Holes should be in the plates
    x_holes = np.random.randint(9, x - 9, n)
    y_holes = np.random.randint(9, y - 9, n)
    r_holes = np.random.randint(2, 8, n)
    holes = [
        [float(x_h), float(y_h), float(r_h)]
        for x_h, y_h, r_h in zip(x_holes, y_holes, r_holes)
    ]

    # Injection locations should be in the plates
    x_inj = np.random.randint(0, x, M)
    y_inj = np.random.randint(0, y, M)
    injections = [
        [[float(x_i), float(y_i), 0.0], [0.0, 0.0, 1.0]]
        for x_i, y_i in zip(x_inj, y_inj)
    ]

    # build dictionary for YAML
    models[f"plate_{i}"] = {
        "thickness": 3.0,
        "plate": [float(x), float(y)],
        "holes": holes,
        "injection_locations": injections,
    }

# Write configuration file
with open("random_models.yaml", "w") as file:
    yaml.dump(models, file, default_flow_style=None)

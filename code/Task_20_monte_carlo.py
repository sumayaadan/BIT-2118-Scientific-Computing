"""BIT 2118 Scientific Computing — Task 20\nStudent: Hurley Jules\nRegistration: BSCCS/2025/56368\n"""

import numpy as np

rng = np.random.default_rng(42)
samples = rng.integers(0,101,size=100000)
threshold = 80
probability = np.mean(samples > threshold)
print("Estimated overload probability:", probability)

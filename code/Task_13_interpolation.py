"""BIT 2118 Scientific Computing — Task 13\nStudent: Hurley Jules\nRegistration: BSCCS/2025/56368\n"""

import numpy as np
from scipy.interpolate import interp1d

hours = np.array([0,4,8,12,16,20,24], dtype=float)
temperature = np.array([18,19,22,27,25,21,19], dtype=float)
query = np.linspace(0,24,49)
linear = interp1d(hours, temperature, kind="linear")
cubic = interp1d(hours, temperature, kind="cubic")
print("Interpolated at 10 hours:", float(linear(10)))
print("Cubic at 10 hours:", float(cubic(10)))

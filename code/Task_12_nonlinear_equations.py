"""BIT 2118 Scientific Computing — Task 12\nStudent: Hurley Jules\nRegistration: BSCCS/2025/56368\n"""

import numpy as np

# Intersection of x^2 + y^2 = 4 and y = x^2 - 1
# Substitute y into the circle equation and find roots numerically.
coeff = [1, -2, -3]
roots = np.roots(coeff)
for x2 in roots:
    if x2 >= 0:
        x = np.sqrt(x2)
        y = x*x - 1
        print("Intersection:", (x,y), (-x,y))

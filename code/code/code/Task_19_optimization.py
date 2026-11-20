"""BIT 2118 Scientific Computing — Task 19\nStudent: Hurley Jules\nRegistration: BSCCS/2025/56368\n"""

import scipy.optimize as opt

# Minimize a simple server operating-cost model.
def cost(x):
    return 200*x[0] + 320*x[1]
constraints = [
    {"type":"ineq","fun":lambda x: 100*x[0] + 180*x[1] - 1000},
    {"type":"ineq","fun":lambda x: 64*x[0] + 128*x[1] - 600},
]
result = opt.minimize(cost,[5,5],bounds=[(0,None),(0,None)],constraints=constraints)
print("Optimal quantities:", result.x)
print("Minimum cost:", result.fun)

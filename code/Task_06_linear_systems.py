"""BIT 2118 Scientific Computing — Task 6\nStudent: Hurley Jules\nRegistration: BSCCS/2025/56368\n"""

import numpy as np

A = np.array([[4.,2.],[8.,12.]])
b = np.array([20.,72.])
solution = np.linalg.solve(A,b)
print("Solution:", solution)
print("Verification:", A @ solution)
print("Residual:", b - A @ solution)

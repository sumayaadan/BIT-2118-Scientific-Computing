"""BIT 2118 Scientific Computing — Task 8\nStudent: Hurley Jules\nRegistration: BSCCS/2025/56368\n"""

import numpy as np
import matplotlib.pyplot as plt

A = np.array([[2.,-1.,0.],[-1.,2.,-1.],[0.,-1.,2.]])
b = np.array([80.,100.,40.])
x = np.zeros(3)
errors = []
for _ in range(50):
    old = x.copy()
    for i in range(3):
        s = sum(A[i,j]*old[j] for j in range(3) if j != i)
        x[i] = (b[i]-s)/A[i,i]
    errors.append(np.linalg.norm(x-old))
print("Jacobi-style solution:", x)
plt.plot(errors, marker="o")
plt.xlabel("Iteration"); plt.ylabel("Change"); plt.title("Iterative Convergence")
plt.grid(True); plt.show()

"""BIT 2118 Scientific Computing — Task 9\nStudent: Hurley Jules\nRegistration: BSCCS/2025/56368\n"""

import numpy as np

A = np.array([[0,1,1,0],[1,0,1,1],[1,1,0,1],[0,1,1,0]], dtype=float)
values, vectors = np.linalg.eig(A)
i = np.argmax(values.real)
print("Dominant eigenvalue:", values[i].real)
print("Corresponding eigenvector:", vectors[:,i].real)

"""BIT 2118 Scientific Computing — Task 5\nStudent: Hurley Jules\nRegistration: BSCCS/2025/56368\n"""

import numpy as np

points = np.array([[0.,0.],[1.,0.],[1.,1.],[0.,1.]])
angle = np.deg2rad(45)
rotation = np.array([[np.cos(angle),-np.sin(angle)],[np.sin(angle),np.cos(angle)]])
scale = np.array([[2.,0.],[0.,1.5]])
transformation = rotation @ scale
transformed_points = points @ transformation.T
print("Transformed points:\n", transformed_points)
print("Determinant:", np.linalg.det(transformation))

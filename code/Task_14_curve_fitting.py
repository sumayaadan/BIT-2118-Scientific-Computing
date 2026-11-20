"""BIT 2118 Scientific Computing — Task 14\nStudent: Hurley Jules\nRegistration: BSCCS/2025/56368\n"""

import numpy as np
import matplotlib.pyplot as plt

users = np.array([10,20,30,40,50,60], dtype=float)
response = np.array([0.5,0.7,1.0,1.5,2.1,2.9])
coef = np.polyfit(users, response, 2)
model = np.poly1d(coef)
print("Quadratic coefficients:", coef)
print("Predicted response at 70 users:", model(70))
plt.scatter(users,response)
plt.plot(users,model(users))
plt.xlabel("Users"); plt.ylabel("Response time (s)")
plt.title("Curve Fit"); plt.grid(True); plt.show()

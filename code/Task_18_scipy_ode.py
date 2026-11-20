"""BIT 2118 Scientific Computing — Task 18\nStudent: Hurley Jules\nRegistration: BSCCS/2025/56368\n"""

import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp

R, C, V = 1000.0, 0.001, 5.0
def model(t,y):
    return [(V-y[0])/(R*C)]
sol = solve_ivp(model,[0,5],[0.0],dense_output=True)
t = np.linspace(0,5,200)
v = sol.sol(t)[0]
print("Final capacitor voltage:", v[-1])
plt.plot(t,v)
plt.xlabel("Time (s)"); plt.ylabel("Voltage (V)")
plt.title("RC Charging using solve_ivp"); plt.grid(True); plt.show()

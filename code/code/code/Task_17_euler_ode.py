"""BIT 2118 Scientific Computing — Task 17\nStudent: Hurley Jules\nRegistration: BSCCS/2025/56368\n"""

import numpy as np
import matplotlib.pyplot as plt

# Newton cooling: dT/dt = -k(T-Ta)
T = 90.0
Ta = 25.0
k = 0.08
dt = 0.5
times = np.arange(0,20+dt,dt)
values = [T]
for _ in times[1:]:
    T = T + dt*(-k*(T-Ta))
    values.append(T)
print("Final temperature:", values[-1])
plt.plot(times,values)
plt.xlabel("Time"); plt.ylabel("Temperature")
plt.title("Euler Method - Newton Cooling"); plt.grid(True); plt.show()

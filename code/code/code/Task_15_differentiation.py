"""BIT 2118 Scientific Computing — Task 15\nStudent: Hurley Jules\nRegistration: BSCCS/2025/56368\n"""

import numpy as np
import matplotlib.pyplot as plt

time = np.array([0,1,2,3,4,5], dtype=float)
position = np.array([0,8.1,17.5,22.7,30.0,38.0])
speed = np.gradient(position,time)
print("Estimated speeds:", speed)
plt.plot(time,speed,marker="o")
plt.xlabel("Time (s)"); plt.ylabel("Speed (m/s)")
plt.title("Speed from Position Data"); plt.grid(True); plt.show()

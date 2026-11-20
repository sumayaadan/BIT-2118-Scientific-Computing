"""BIT 2118 Scientific Computing — Task 16\nStudent: Hurley Jules\nRegistration: BSCCS/2025/56368\n"""

import numpy as np
from scipy.integrate import simpson

time_hours = np.array([0,2,4,6,8,10,12], dtype=float)
power_kw = np.array([0.8,1.0,1.4,1.8,1.6,1.2,0.9])
print("Trapezoidal energy:", np.trapezoid(power_kw,time_hours), "kWh")
print("Simpson energy:", simpson(power_kw,x=time_hours), "kWh")

"""BIT 2118 Scientific Computing — Task 10\nStudent: Hurley Jules\nRegistration: BSCCS/2025/56368\n"""

import math

def f(T):
    return T - 25 - 10 * math.exp(-T/20)

a, b = 0.0, 100.0
for _ in range(60):
    c = (a+b)/2
    if f(a)*f(c) <= 0: b = c
    else: a = c
print("Bisection root:", (a+b)/2)

x = 40.0
for _ in range(50):
    x = 25 + 10 * math.exp(-x/20)
print("Fixed-point result:", x)

from random import * 
from statistics import *

# Specify parameters
a = 1
b = 8
N = 100000

# Integrand
def f(x):
    return x**2

# Find value of c
c = f(b)

# Area of rectangle
A_J = (b-a) * c

Z = [0]*N
for i in range(N):
    x = uniform(a, b) 
    y = uniform(0, c) 
    if y <= f(x):
        Z[i] = 1

A_I = mean(Z) * A_J

print("A_I = ", round(A_I, 2))  # =  169.57 (170.33)
print("Variance = ", round(variance(Z), 4)) # = 0.2352
from random import *
from math import *

k = 10
theta = 1.5

y = 0

for i in range(k):
    u = random()
    x = (-1 / theta) * log(1-u)     # Exponential variate
    y = y + x

print("Y", y)
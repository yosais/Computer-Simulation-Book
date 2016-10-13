import random as rnd
import math as M
def f(x):
    return 0.2 * M.exp(-(x - 0.2)**2.0) + 
                0.8 * M.exp(-(x - 2.0)**2.0 / 0.2)
def g(x):
    return 1    # Uniform PDF
Stop = False
while not Stop:
    x = rnd.uniform(0, 4)     # Generate x
    u = rnd.random()          # y = u * g(x)
    if u <= f(x) / g(x):      # y <= f(x)
        print x
        Stop = True
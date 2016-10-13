import random as rnd
import math
# Import file containing the normal function
from normal import *

def lognormal(mean, sigma):
    u1, u2 = rnd.random(), rnd.random()
    z1, z2 = normal(u1, u2)
    # Generate random variate from a non-standard normal distribution
    v = mean + sigma * z1
    return math.exp(v)
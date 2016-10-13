import random as rnd
import math
import matplotlib.pyplot as plt

def normal(u1,u2):  
    z1 = sqrt( -2 * log(u1) ) * cos ( 2 * pi * u2 )  
    return z1

def lognormal(mean, sigma):
    u1, u2 = rnd.random(), rnd.random()
    tmp = normal(u1,u2)
    v = mean + sigma * tmp
    return math.exp(v)

v = []
mean, sigma = 3, 1

for i in range(1000):
    v.append(lognormal(mean, sigma))
    
count, bins, ignored = plt.hist(v, 100, normed = True, align = 'mid')
plt.show()
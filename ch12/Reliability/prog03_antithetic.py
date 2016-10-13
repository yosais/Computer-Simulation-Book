from random import *
from statistics import *

q = 0.5         # Prob. of link failure
N = 100000      # Number of trials
L = 4           # Number of links

# Check if network is connected
def Phi(s):
    if s[0] == 0 and s[1] == 0 or s[0] == 0 and s[2] == 0 or \
         s[1] == 0 and s[3] == 0 or s[2] == 0 and s[3] == 0:
        return 1
    else:
        return 0

# Antithetic Monte Carlo simulation
rv = []      # Realization of a Bernoulli random variable
for i in range(N):
    s1 = [0]*L
    s2 = [0]*L
    for j in range(L):
        u = random()
        if u > q:       s1[j] = 1
        if (1 - u) > q: s2[j] = 1

    val = (Phi(s1) + Phi(s2) ) / 2
    rv.append(val)
        
# Result
print("Unreliability = ", round(mean(rv), 4))
print("Variance = ", round(variance(rv), 4))
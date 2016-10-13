from random import *
from statistics import *

q = 0.5      # Prob. of link failure
N = 100000   # Number of trials
L = 4        # Number of links

# Check if network is connected
def Phi(s):
    if s[0] == 0 and s[1] == 0 or s[0] == 0 and s[2] == 0 or \
         s[1] == 0 and s[3] == 0 or s[2] == 0 and s[3] == 0:
        return 1
    else:
        return 0

# Crude Monte Carlo simulation
rv = []      # Realization of a Bernoulli random variable
for i in range(N):
    s = [0]*L
    for j in range(L):
        if random() > q:
            s[j] = 1
    rv.append(Phi(s))
        
# Result
print("Unreliability = ", round(mean(rv), 4))
print("Variance = ", round(variance(rv), 4))
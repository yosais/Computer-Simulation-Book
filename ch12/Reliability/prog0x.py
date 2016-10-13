from random import *
from statistics import *
from math import *

q = 0.0001     # Prob. of link failure
L = 4       # Number of links
N = 100000  # Number of trials in each replication
M = 35      # Number of replications

# Check if network is connected
def Phi(s):
    if s[0] == 0 and s[1] == 0 or s[0] == 0 and s[2] == 0 or \
         s[1] == 0 and s[3] == 0 or s[2] == 0 and s[3] == 0:
        return 1
    else:
        return 0

u = []
for k in range(M):
    # Crude Monte Carlo simulation
    count = 0
    for i in range(N):
        s = [0]*L
        for j in range(L):
            if random() > q:
                s[j] = 1
        if Phi(s) == 1:
            count = count + 1
    u.append(count/N)

# Compute half width confidence interval
mean = mean(u)
std_dev = stdev(u)
t = 1.96

ci = t * (std_dev / sqrt(M))

print("Mean = ", mean)
print("CI = ", ci / float(mean) )
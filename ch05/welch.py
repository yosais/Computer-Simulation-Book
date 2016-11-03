from simLib import out_var_cum_mm1
from random import seed
from matplotlib.pyplot import *
import numpy as np

lamda = 1.3
mu = 2

n = 10000	# Number of packets to be simulated
R = 5		# Number of replications (repetitions)

Y =  np.zeros( shape = (R, n) )	# Output variable Delay

# 1. Generate sample paths
for i in range(R):
	seed()
	Y[i] = out_var_cum_mm1(lamda, mu, n)

# 2. Compute the mean
Z = []
for i in range(n):
	Z.append( sum(Y[:, i]) / R )

# Plot Y and Z
plot(Y[0], "k--", label="Y[0]")
plot(Y[1], "k--", label="Y[1]")
plot(Y[2], "k--", label="Y[2]")
plot(Y[3], "k--", label="Y[3]")
plot(Y[4], "k--", label="Y[4]")
plot(Z, "k", linewidth=2, label="Z")

xlabel("$n$", size=16)
ylabel("$W_{cum}$", size=16)
legend(loc='upper right', shadow=True)
show()
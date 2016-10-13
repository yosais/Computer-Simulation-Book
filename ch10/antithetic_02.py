from random import *
from statistics import *
from math import *

n = 10000

Z = []
Z_ = []

for i in range(n):
	u = random()
	u_ = 1 - u
	Z.append( exp(u**2) )
	Z_.append( ( exp(u**2) + exp(u_**2) ) / 2)
	
print("Mean(Z) = ",round(mean(Z), 4)) 		# 1.4592
print("Var(Z) = ",round(variance(Z), 4)) 	# 0.2241
print("Mean(Z_) = ",round(mean(Z_), 4)) 	# 1.4631
print("Var(Z_) = ",round(variance(Z_), 4)) 	# 0.0281

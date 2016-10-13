from random import *
from statistics import *

N = 100000

Z = []
for i in range(N):
	x = uniform(-1, 1)
	y = uniform(-1, 1)
	if x**2 + y**2 <= 1:
		Z.append(1)
	else:
		Z.append(0)

print ("Pi = ", 4.0 * round(mean(Z), 4))		# = 3.1452
print ("Variance = ", round(variance(Z), 4))	# = 0.1681
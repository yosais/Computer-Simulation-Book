from random import *
N = 100000
E_g = 0
def g(x):
	return 8*x
for i in range(N):
	x = random()	# Sample from p(x)
	y = normalvariate(0, 10)	# Sample from q(x)
	w = x/y		# Importance weight for current sample
	E_g = E_g + g(y) * w
print("E[g(x)] = ", round(E_g / N, 2))	# Answer = 4.0
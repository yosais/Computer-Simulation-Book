from random import *
from statistics import *

n = 1000
a = 2
b = 48

s = []		# Samples generated using the crude Monte Carlo	method
s_ = [] 	# Samples generated using the antithetic method

for i in range(n):
	v = uniform(a, b)
	s.append(v)
	v_ = a + b - v
	s_.append( (v + v_) / 2 )

print('Mean(s) = ', round(mean(s), 4))			# 24.975
print('Var(s) = ', round(variance(s), 4))		# 180.4049 
print('Mean(s_) = ', round(mean(s_), 4))		# 25.0
print('Var(s_) = ', round(variance(s_), 4))		# 0.0
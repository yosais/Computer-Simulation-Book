from random import *
from math import *
l = 1
d = 1
n = 1000000
count = 0
for i in range(n):
	a = uniform(0, d/2)
	phi = uniform(0, pi)
	b = (l/2)*sin(phi)
	if b >= a:
		count = count + 1	
print('P = ', round(count/n, 3))
print('Exact = ', round((2*l)/(pi*d), 3))

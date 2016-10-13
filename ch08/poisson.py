import random as rnd
import math
lmda = 10	# Arrival Rate
count = 0	# Number of Arrivals
b = math.exp(-lmda)
u = rnd.random()
while u >= b:
	count = count + 1
	u = u * rnd.random()	
print ('v = ' , count)
from random import expovariate
from math import inf as Infinity

Avg_IAT = 2.0				# Average Inter-Arrival Time 
Avg_ST = 1.0 				# Average Service Time 
Tot_Sim_Time = 100.0		# Total Simulation Time 
clock = 0.0 				# Current Simulation Time

N = 0	# State variable; number of customers in the system

# Time of the next arrival event
Arr_Time = expovariate(1.0/Avg_IAT)
# Time of the next departure event
Dep_Time = Infinity					

while clock <= Tot_Sim_Time:
	if Arr_Time < Dep_Time: 	# Arrival Event
		clock = Arr_Time
		N = N + 1.0
		Arr_Time = clock + expovariate(1.0/Avg_IAT)
		if N == 1:
			Dep_Time = clock + expovariate(1.0/Avg_ST) 
	else: 						# Departure Event
		clock = Dep_Time 
		N = N - 1.0
		if N > 0:
			Dep_Time = clock + expovariate(1.0/Avg_ST)
		else:
			Dep_Time = Infinity
	
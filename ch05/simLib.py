# A user-defined simulation library

from random import expovariate
from statistics import mean 
from math import inf as Infinity

# Simulation of mm1 queueing system 
# This function returns the average delay
def mm1(lamda, mu, Num_Pkts):
	count = 0			# Count number of simulated packets
	clock = 0
	N = 0				# State Variable; number of packets in system

	Arr_Time = expovariate(lamda) 
	Dep_Time = Infinity 			

	# Output Variables
	Arr_Time_Data = []   # Collect arrival times
	Dep_Time_Data = []   # Collect departure times
	Delay_Data = []		# Collect delays of individual packets

	while count < Num_Pkts:
		if Arr_Time < Dep_Time: 	# Arrival Event
			clock = Arr_Time
			Arr_Time_Data.append(clock)
			N = N + 1.0
			Arr_Time = clock + expovariate(lamda) 
			if N == 1:
				Dep_Time = clock + expovariate(mu)
		else: 						# Departure Event
			clock = Dep_Time 
			Dep_Time_Data.append(clock)
			N = N - 1.0
			count = count + 1	# Packet Simulated
			if N > 0:
				Dep_Time = clock + expovariate(mu)
			else:
				Dep_Time = Infinity

	for i in range(Num_Pkts):
		d = Dep_Time_Data[i] - Arr_Time_Data[i]
		Delay_Data.append(d)

	return mean(Delay_Data)
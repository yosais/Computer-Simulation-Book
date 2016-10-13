import random as rnd
import statistics as stat
import matplotlib.pyplot as plt
import numpy as np
import math

Avg_IAT = 1.0			# Average Inter-Arrival Time 
Avg_ST = 0.5 			# Average Service Time 
Num_Sim_Pkts = 1000 	# Number of Simulated Packets 
Infinity = math.inf 	# A very large Number

N = 0.0 				# Number of customers in the system
clock = 0.0 			# Current Simulation Time
count = 0				# Count Packets
R = 10					# Number of simulation runs (i.e., replications)

Arr_Time = 0.0 			# Time of the next arrival event
Dep_Time = Infinity 	# Time of the next departure event

Arr_Time_Out_Var = []	# Output variable for collecting arrival times
Dep_Time_Out_Var = []	# Output variable for collecting departure times

Delay = np.zeros( (R, Num_Sim_Pkts) )

for r in range(R):
	while count < Num_Sim_Pkts:
		if Arr_Time < Dep_Time: 	# Arrival Event
			clock = Arr_Time
			Arr_Time_Out_Var.append(clock)
			N = N + 1.0
			Arr_Time = clock + rnd.expovariate(1.0/Avg_IAT) 
			if N == 1:
				Dep_Time = clock + rnd.expovariate(1.0/Avg_ST) 
		else: 						# Departure Event
			clock = Dep_Time 
			Dep_Time_Out_Var.append(clock)
			N = N - 1.0
			count = count + 1	# Packet Simulated
			if N > 0:
				Dep_Time = clock + rnd.expovariate(1.0/Avg_ST)
			else:
				Dep_Time = Infinity
	
	for i in range(Num_Sim_Pkts):
		d = Dep_Time_Out_Var[i] - Arr_Time_Out_Var[i]
		Delay[r, i] = d

	# Initialize for next simulation run
	Arr_Time = 0.0
	Dep_Time = Infinity
	N = 0.0
	clock = 0.0
	count = 0
	Arr_Time_Out_Var = []
	Dep_Time_Out_Var = []
#------------------------------------------------------------
# Ensemble Average
Mean = []
for i in range(Num_Sim_Pkts):
	Mean.append(sum(Delay[:,i]) / R)

# Cumulative Ensemble Average
Cum_Ens_Avg = []
for i in range(Num_Sim_Pkts):
	s = i + 1 	# Slice
	Cum_Ens_Avg.append( sum(Mean[0:s]) / s )

# Cumulative Delay from a Single Simulation Run
Cum_Delay = []
for i in range(Num_Sim_Pkts):
	s = i + 1 	# Slice
	Cum_Delay.append( sum(Delay[0,0:s]) / s )
#-----------------------------------------------------------
x = [i for i in range(1, Num_Sim_Pkts+1)]
#plt.plot(x, Delay[0,:])
plt.plot(x, Cum_Delay, label="Cum_Delay")
#plt.plot(x, Cum_Ens_Avg, label="Cum_Ens_Avg")
plt.legend(bbox_to_anchor=(0., 1.02, 1., .102), loc=3,
           ncol=2, mode="expand", borderaxespad=0.)
plt.show()
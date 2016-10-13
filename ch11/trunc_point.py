import random as rnd
import statistics as stat
import matplotlib.pyplot as plt
import numpy as np
import math

Avg_IAT = 1.0			# Average Inter-Arrival Time 
Avg_ST = 0.5 			# Average Service Time 
Num_Sim_Pkts = 10000 	# Number of Simulated Packets 
Infinity = math.inf 	# A very large Number

N = 0.0 				# Number of customers in the system
clock = 0.0 			# Current Simulation Time
count = 0				# Count Packets
R = 5					# Number of simulation runs (i.e., replications)

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
# Average
Z = []

for i in range(Num_Sim_Pkts):
	Z.append( sum(Delay[:,i]) / R )
#-----------------------------------------------------------
# Moving Average
H = []

H.append(Z[0])

for i in range(Num_Sim_Pkts):
	j = i + 1
	H.append( sum(Z[0:j]) / j )
#-----------------------------------------------------------
# Statistics
print('Mean of the Untruncated Sequence: ', stat.mean(H))
print('Mean of the Truncated Sequence: ', stat.mean(H[4000:6000]))
#-----------------------------------------------------------
x1 = [i for i in range(len(H))]
plt.plot(x1, H, label="H")
plt.legend(bbox_to_anchor=(0., 1.02, 1., .102), loc=3, ncol=2, mode="expand", borderaxespad=0.)
plt.show()
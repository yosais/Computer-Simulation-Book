import random as rnd
import statistics as stat
import math

# Parameters
lamda = 1.0         # Lambda  
mu = 2.0            # Mu 
Num_Pkts = 5000     # Number of Simulated Packets

# Input Variables
IAT = 0.0			# Time of the next arrival event
ST = math.inf		# Time of the next departure event

# Arrival & Departure Times for the First Packet
Arr_Time = IAT 
Dep_Time = ST 			

# Output Variables
# Internal Output variable
Arr_Time_Out_Var = []   # Collect Arrival Times
Dep_Time_Out_Var = []   # Collect Departure Times

# Main Output Variable
Delay = []              # Collect Individual Delays

count = 0			# Count Number of Simulated Packets
N = 0				# State Variable; Number of Packets in Queue

while count < Num_Pkts:
	if Arr_Time < Dep_Time: 	# Arrival Event
		clock = Arr_Time
		Arr_Time_Out_Var.append(clock)
		N = N + 1.0
		IAT = rnd.expovariate(lamda)	# Next Value of Input Variable IAT
		Arr_Time = clock + IAT 
		if N == 1:
			ST = rnd.expovariate(mu)	# Next Value of Output Variable ST
			Dep_Time = clock + ST
	else: 						# Departure Event
		clock = Dep_Time 
		Dep_Time_Out_Var.append(clock)
		N = N - 1.0
		count = count + 1	# Packet Simulated
		if N > 0:
			ST = rnd.expovariate(mu)
			Dep_Time = clock + ST
		else:
			Dep_Time = math.inf

for i in range(Num_Pkts):
	d = Dep_Time_Out_Var[i] - Arr_Time_Out_Var[i]
	Delay.append(d)

print( "Average Delay = %0.2f" % stat.mean(Delay) )
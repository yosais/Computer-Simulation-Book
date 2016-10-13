import random as rnd
Avg_IAT = 2.0			# Average Inter-Arrival Time 
Avg_ST = 1.0 			# Average Service Time 
Tot_Sim_Time = 10.0 	# Total Simulation Time 
Infinity = 999999999.0 	# A large Number
N = 0.0 				# Number of customers in the system
clock = 0.0 			# Current Simulation Time
Arr_Time = 0.0 			# Time of the next arrival event
Dep_Time = Infinity 	# Time of the next departure event
while clock <= Tot_Sim_Time:
	if Arr_Time < Dep_Time: 	# Arrival Event
		clock = Arr_Time
		N = N + 1.0
		Arr_Time = clock + rnd.expovariate(1.0/Avg_IAT) 
		if N == 1:
			Dep_Time = clock + rnd.expovariate(1.0/Avg_ST) 
	else: 						# Departure Event
		clock = Dep_Time 
		N = N - 1.0
		if N > 0:
			Dep_Time = clock + rnd.expovariate(1.0/Avg_ST)
		else:
			Dep_Time = Infinity
	#------------- Trace the program execution --------------
	print( 'Current Simulation Time = ' , clock ) 
	print( 'N = ' , N )
	print( 'Next Arrival At ', Arr_Time )
	print( 'Next Departure At ', Dep_Time )
	#--------------------------------------------------------
	if Arr_Time > Tot_Sim_Time and Dep_Time > Tot_Sim_Time:
		break
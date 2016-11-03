from random import expovariate
from statistics import mean 
from math import inf as Infinity

# Parameters
lamda = 1.3       
mu = 2.0     
Num_Pkts = 1000000     
count = 0	
clock = 0
N = 0

Arr_Time = expovariate(lamda) 
Dep_Time = Infinity 

Prev_Event_Time = 0.0	# Time of last event
Area = []	# Output variable

while count < Num_Pkts:
	if Arr_Time < Dep_Time:
		clock = Arr_Time
		# Area of rectangle
		Area.append((clock - Prev_Event_Time) * N)
		Prev_Event_Time = clock
		N = N + 1.0
		Arr_Time = clock + expovariate(lamda) 
		if N == 1:
			Dep_Time = clock + expovariate(mu)
	else: 					
		clock = Dep_Time 
		# Area of rectangle
		Area.append((clock - Prev_Event_Time) * N)
		Prev_Event_Time = clock
		N = N - 1.0
		count = count + 1
		if N > 0:
			Dep_Time = clock + expovariate(mu)
		else:
			Dep_Time = Infinity

print( "E[ N(t) ] = ", round(sum(Area) / clock, 4) )
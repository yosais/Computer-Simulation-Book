import random as rnd
Avg_IAT = 2.0    # Average IAT
Sim_Time = 100    # Total simulation time
N = 0            # Count number of arrivals
cur_time = rnd.expovariate(1.0/Avg_IAT)
while cur_time <= Sim_Time:
    N = N + 1
    print 'Arrival Time = ', cur_time
    # Advance simulation timee
    cur_time = cur_time + rnd.expovariate(1.0/Avg_IAT)
print( 'Total Number of Arrivals = ', N )
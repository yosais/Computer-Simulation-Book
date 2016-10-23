from random import expovariate

Avg_IAT = 2.0    # Average IAT
Sim_Time = 100    # Total simulation time
N = 0            # Count number of arrivals
clock = 0       # Simulation time

while clock <= Sim_Time:
    N = N + 1
    # Advance simulation clock
    clock = clock + expovariate(1/Avg_IAT)

print('Total Number of Arrivals = ', N)
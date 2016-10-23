from random import expovariate
from matplotlib.pyplot import *

Avg_IAT = 2.0
Avg_ST = 1.0    # Avg service time
Sim_Time = 100  # Total simulation time
N = 0            
clock = 0   # Simulation time
X = []  # Times of events
Y = []  # Values of N

while clock <= Sim_Time:
    IAT = expovariate(1 / Avg_IAT)
    ST = expovariate(1 / Avg_ST)
    if IAT <= ST:
        N += 1
        clock = clock + IAT
        X.append(clock)
        Y.append(N)
    else:
        if N > 0:
            N -= 1
            clock = clock + ST
            X.append(clock)
            Y.append(N)

step(X, Y, Linewidth=1.2, color='black')
xlabel('Time', size=16)
ylabel('N', size=16)
xlim(0, 101)
#show()
savefig('sim_birth_death_process.pdf', format='pdf', bbox_inches='tight')
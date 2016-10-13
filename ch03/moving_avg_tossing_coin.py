### Part 1: Performing the simulation experiment
from random import choice
from statistics import mean

n = 1000
observed = []

for i in range(n):
	outcome = choice(['Head', 'Tail'])
	if outcome == 'Head':
		observed.append(1)
	else:
		observed.append(0)

print("Prob = ", round(mean(observed), 2))

### Part 2: Computing the moving average
from numpy import cumsum

cum_observed = cumsum(observed)

moving_avg = []
for i in range(len(cum_observed)):
	moving_avg.append( cum_observed[i] / (i+1) )

### Part 3: Making the plot
from matplotlib.pyplot import *
from numpy import arange

x = arange(0, len(moving_avg), 1)	# x-axis
p = [0.5 for i in range(len(moving_avg))] # Line

xlabel('Iterations', size=20)
ylabel('Probability', size=20)

plot(x, moving_avg)
plot(x, p, linewidth=2, color='black')

show()
from random import *
from matplotlib.pyplot import *
from statistics import *

def Normal():
    z = -6
    for i in range(12):
        u = random()
        z = z + u
    return z

N = 100000
v = []
for i in range(N):
    v.append( Normal() )

bins = 100

w = [1 / len(v)] * len(v)

hist(v, bins, weights = w)

xlabel('Y')
ylabel('P(y)')

# Hide numbers along y-axis
gca().axes.get_yaxis().set_ticklabels([])
# Remove ticks along y-axis
gca().axes.yaxis.set_tick_params(width=0)

savefig('normal_convolution_plot_hist.pdf', format='pdf', bbox_inches='tight')

print("Mean = ", mean(v))
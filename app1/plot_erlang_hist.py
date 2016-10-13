from random import *
from math import *
from matplotlib.pyplot import *
from statistics import *

def Erlang():
    k = 10
    theta = 1.0
    y = 0
    for i in range(k):
        u = random()
        x = (-1 / theta) * log(u)     # Exponential variate
        y = y + x

    return y

N = 100000
v = []
for i in range(N):
    v.append( Erlang() )

bins = 100

w = [1 / len(v)] * len(v)

hist(v, bins, weights = w)

xlabel('Y')
ylabel('P(y)')

# Hide numbers along y-axis
gca().axes.get_yaxis().set_ticklabels([])
# Remove ticks along y-axis
gca().axes.yaxis.set_tick_params(width=0)

savefig('erlang_plot_hist.pdf', format='pdf', bbox_inches='tight')

print("Mean = ", mean(v))
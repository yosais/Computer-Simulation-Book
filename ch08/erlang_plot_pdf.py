from random import *
from math import *
from matplotlib.pyplot import *
from numpy import *

def pdf(x):
    k = 10
    theta = 1.0
    return (x**(k-1) * theta**k * exp(-1 * theta * x)) / factorial(k-1)

X = arange(0, 50, 0.1)
Y = []
for x in X:
    Y.append( pdf(x) )

xlabel('Y')
ylabel('P(y)')

# Hide numbers along y-axis
gca().axes.get_yaxis().set_ticklabels([])
# Remove ticks along y-axis
gca().axes.yaxis.set_tick_params(width=0)

plot(X, Y, linewidth=2)
savefig('erlang_plot_pdf.pdf', format='pdf', bbox_inches='tight')

# Compute the mean
mean = 0
for i in range( len(X) ):
    mean = mean + X[i] * Y[i]

print("Mean = ", mean)
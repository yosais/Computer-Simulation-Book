from random import *
from math import *
from matplotlib.pyplot import *
from numpy import *

def pdf(x, a, b, c):
    if x < a:
        return 0    
    elif x >= a and x < c:
        return (2 * (x-a)) / ((b-a)*(c-a))
    elif x == c:
        return 2 / (b-a)
    elif x > c and x <= b:
        return (2 * (b-x)) / ((b-a)*(b-c))
    elif x > b:
        return 0
    else:
        print("Error")


a = 1
b = 10
c = 7

X = arange(0, b+1, 0.1)
Y = []

xlabel('X', fontsize=15)
ylabel('f(x)', fontsize=15)

gca().axes.get_xaxis().set_ticks( np.arange(0, b+1, 1.0) )

for x in X:
    Y.append( pdf(x, a, b, c) )

plot(X, Y, linewidth=2)

# Show figure on screen
show()

# Save figure to hard disk
savefig('triangular_pdf.pdf', format='pdf', bbox_inches='tight')
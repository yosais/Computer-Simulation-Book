from random import *
from math import *
from matplotlib.pyplot import *
from numpy import *

# Parameters
a = 1
b = 10
c = 7

def cdf(x):
    if x <= a:
        return 0    
    elif x > a and x <= c:
        return (x-a)**2 / ((b-a)*(c-a))
    elif x > c and x < b:
        return 1 - ( (b-x)**2 / ((b-a)*(b-c)) )
    elif x >= b:
        return 1
    else:
        print("Error")

def pdf(x):
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


X = arange(0, b+1, 0.1)
Y = []

for x in X:
    Y.append(pdf(x))

matplotlib.rc('xtick', labelsize=18) 
matplotlib.rc('ytick', labelsize=18) 
plot(X, Y, Linewidth=2, color='black')
xlabel('$X$', size=22)
ylabel('$f_X(x)$', size=22)
#show()
savefig('triangular_pdf.pdf', format='pdf', bbox_inches='tight')

# Clear the current figure
clf()

X = arange(0, b, 0.1)
Y = []

for x in X:
    Y.append(cdf(x))

matplotlib.rc('xtick', labelsize=18) 
matplotlib.rc('ytick', labelsize=18) 
plot(X, Y, Linewidth=2, color='black')
xlabel('$X$', size=22)
ylabel('$F_X(x)$', size=22)
#show()
savefig('triangular_cdf.pdf', format='pdf', bbox_inches='tight')
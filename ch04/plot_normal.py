from math import exp, sqrt, pi
from numpy import *
from matplotlib.pyplot import *

# Parameters
mu = 30
sigma = 10

# Plotting the PDF
def pdf(x):
    return (1 / (sigma * sqrt(2*pi)) ) * exp(-(x - mu)**2 / (2 * sigma**2))

X = arange(-100, 100, 0.1)
Y = []

for x in X:
    Y.append(pdf(x))

matplotlib.rc('xtick', labelsize=18) 
matplotlib.rc('ytick', labelsize=18) 
plot(X, Y, Linewidth=2, color='black')
xlabel('$X$', size=22)
ylabel('$f_X(x)$', size=22)
#show()
savefig('normal_pdf.pdf', format='pdf', bbox_inches='tight')

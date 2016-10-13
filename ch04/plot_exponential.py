from math import exp
from numpy import *
from matplotlib.pyplot import *

# Parameters
mu = 1.5

# Plotting the PDF
def pdf(x):
    return mu * exp(-mu * x)

X = arange(0, 10, 0.1)
Y = []

for x in X:
    Y.append(pdf(x))

matplotlib.rc('xtick', labelsize=18) 
matplotlib.rc('ytick', labelsize=18) 
plot(X, Y, Linewidth=2, color='black')
xlabel('$X$', size=22)
ylabel('$f_X(x)$', size=22)
#show()
savefig('exponential_pdf.pdf', format='pdf', bbox_inches='tight')

# Clear the current figure
clf()

# Plotting the CDF
def cdf(x):
    return 1 - exp(-mu * x)

X = arange(0, 10, 0.1)
Y = []

for x in X:
    Y.append(cdf(x))

matplotlib.rc('xtick', labelsize=18) 
matplotlib.rc('ytick', labelsize=18) 
plot(X, Y, Linewidth=2, color='black')
xlabel('$X$', size=22)
ylabel('$F_X(x)$', size=22)
#show()
savefig('exponential_cdf.pdf', format='pdf', bbox_inches='tight')
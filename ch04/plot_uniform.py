from numpy import *
from matplotlib.pyplot import *

# Parameters
a = 3
b = 10

# Plotting the PDF
def pdf(x):
    if x >= a and x <= b:
        return 1 / (b - a)
    else:
        return 0

X = arange(0, b+3, 0.1)
Y = []

for x in X:
    Y.append(pdf(x))

matplotlib.rc('xtick', labelsize=18) 
matplotlib.rc('ytick', labelsize=18) 
plot(X, Y, Linewidth=2, color='black')
xlabel('$X$', size=22)
ylabel('$f_X(x)$', size=22)
#show()
savefig('uniform_pdf.pdf', format='pdf', bbox_inches='tight')

# Clear the current figure
clf()

# Plotting the CDF
def cdf(x):
    if x < a:
        return 0
    elif x >= a and x < b:
        return (x - a) / (b - a)
    elif x >= b:
        return 1

X = arange(0, b+3, 0.1)
Y = []

for x in X:
    Y.append(cdf(x))

matplotlib.rc('xtick', labelsize=18) 
matplotlib.rc('ytick', labelsize=18) 
plot(X, Y, Linewidth=2, color='black')
xlabel('$X$', size=22)
ylabel('$F_X(x)$', size=22)
#show()
savefig('uniform_cdf.pdf', format='pdf', bbox_inches='tight')
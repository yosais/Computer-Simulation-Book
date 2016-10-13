from random import expovariate
from matplotlib.pyplot import hist, xlabel, ylabel, title, show, savefig

# Generate the data set
N = 10000
data = [expovariate(1.5) for i in range(N)]

# Decide number of bins
num_bins = 50

# Construct the histogram of the data
# To generate PDF, use normed=True
n, bins, patches = hist(data, num_bins, normed=True, facecolor='black', alpha=0.6)


xlabel('$X$', size=18)
ylabel('$f_X(x)$', size=18)
title('Histogram of exponential data: $\mu$ = 1.5', size=15)

# Show the figure or  save it 
#show()
savefig('hist_expov.pdf', format='pdf', bbox_inches='tight')
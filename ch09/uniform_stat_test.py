from random import *
from statistics import *

N = 10000
data = [random() for i in range(N)]

corr = 0
for i in range(N-1):
    corr = corr + data[i]*data[i+1]
corr = corr / N

print("Mean = ", mean(data))
print("Variance = ", variance(data))
print("Autocorrelation = ", corr)
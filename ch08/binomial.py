import random as rnd
p = 0.3             # Probability of success
n = 10              # Number of trials
count = 0           # Count number of successes
def Bernoulli(p):   # Bernoulli RVG Function
    u = rnd.random()
    if 0 <= u < p:
        return 1
    else:
        return 0
for i in range(n):
    count = count + Bernoulli(p)
print( 'v = ' , count )
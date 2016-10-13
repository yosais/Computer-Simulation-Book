>>> import random
>>> random.random() # Returns a floating-point number in
0.8545672259166788  # the range (0,1)  

>>> random.randrange(1,6)  # Returns an integer in the
4                          # range [1, 6)

>>> random.uniform(1, 3)  # Returns a floating-point number
1.290486289287417         # in the range [1, 3)

>>> random.normalvariate(1,0) # Returns a normal variate where
1.0                           # mean = 1 and stdDev = 0

>>> random.expovariate(3)     # Returns an exponential variate 
0.06953873605855697           # with mean 1/3

>>> random.choice([1,2,3,4,5,6]) # Returns a random element from
5                                 # the input sequence

>>> random.sample([1,2,3,4,5,6],  3) # Randomly choose three
[6, 1, 2]                            # elements from the given
                                     # sequence
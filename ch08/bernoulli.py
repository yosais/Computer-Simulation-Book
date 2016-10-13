import random as rnd
p = 0.5        # Probability of success
u = rnd.random()
if 0 <= u <= p:
    print( '1' )    # Sueccess
else:
    print( '0' )    # Failure
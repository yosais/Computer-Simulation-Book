import random as rnd
X = 'G'    # Initial state
for i in range(10):
    print 'Present State = ', X
    u = rnd.random()
    if X == 'G':
        if u < 0.5:
            X = 'G'
        else:
            X = 'B'
    elif X == 'B':
        if u < 0.7:
            X = 'G'
        else:
            X = 'B'
    print 'Next State = ', X
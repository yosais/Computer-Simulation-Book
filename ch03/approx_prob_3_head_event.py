import random as rnd
n = 10000
ne = 0
z = 6
for i in range(n):
heads = 0
for j in range(5):    # Generate the next event
# 1 if head; 0 if tail
heads = heads + rnd.randint(0,1)
if heads == 3:    # Check if event has occurred
ne = ne + 1
prob = float(ne) / float(n)
print(prob)


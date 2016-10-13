import random as rnd
p = [0.1, 0.2, 0.4, 0.1, 0.2]
u = rnd.random()
if (0 <= u < p[0]):
    v = 0
elif (p[0] <= u < sum(p[0:2])): 
    v = 1
elif (sum(p[0:2]) <= u < sum(p[0:3])):
    v = 2
elif (sum(p[0:3]) <= u < sum(p[0:4])):
    v = 3
else:
    v = 4
print ('u = ' , u , ' , v = ' , v)
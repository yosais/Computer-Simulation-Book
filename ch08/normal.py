# mean  = 0 & standard deviaiton = 1
from math import sqrt, log, sin, cos, pi
from random import random
def normal(u1,u2):  
    z1 = sqrt( -2 * log(u1) ) * cos ( 2 * pi * u2 )  
    z2 = sqrt( -2 * log(u1) ) * sin (2 * pi * u2 )
    return z1 , z2
u1 = random()
u2 = random()
z = normal(u1,u2)
print ('z1 = ' , z[0] , 'z2 = ', z[1])
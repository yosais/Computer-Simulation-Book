import random as rnd
p = 0.6		# Probability of success
# Number of Bernoulli trials Needed Before the First Success
count = 0
def Bernoulli(p):
	u = rnd.random()
	if 0 <= u < p:
		return 1
	else:
		return 0
while(Bernoulli(p) == 0):
	count = count + 1
print( 'v = ' , count )
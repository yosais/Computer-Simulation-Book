from random import *

Num_Trials = 100000
count = 0
p = 0.7		#Probability a block is working

def Phi(X):
	if sum(X) == 3:
		return 1
	else:
		return 0

for i in range(Num_Trials):
	X = []
	for j in range(3):
		if random() <= p: X.append(1)
		else: X.append(0)
	count = count + Phi(X)

print('Rel_sys = ', round(count / Num_Trials, 3))
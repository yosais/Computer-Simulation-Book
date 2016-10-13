from random import randint 

n = 1000000   # No. of times experiment is performed
ne = 0        # Count the occurrences of event

for i in range(n):
    outcome = randint(1, 6)
    if(outcome == 3):       # Check for event of interest
	    ne += 1             # ne = ne + 1	

print("Prob = ", round(ne / n, 4))  # = 0.1667
from random import random

n = 10
S = []

S.append('G')   # Initial state

for i in range(n):
    u = random()
    if S[i] == 'G':
        if u < 0.5:
            S.append('G')
        else:
            S.append('B')
    elif S[i] == 'B':
        if u < 0.7:
            S.append('G')
        else:
            S.append('B')

print('Sample Path: ', S)
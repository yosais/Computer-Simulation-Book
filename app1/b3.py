from random import choice
min = input('Enter smallest number: ')
max = input('Enter largest number: ')
n = input('How many numbers do you want to generate? ')
numbers = range(min, max + 1)
selection = []
for i in xrange(n):
    r = choice(numbers)
    selection.append(r)
    numbers.remove(r)
print( 'Your numbers:', selection )
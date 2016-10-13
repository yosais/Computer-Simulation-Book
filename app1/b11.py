def doIt (func, x, y):
    z = func (x, y)
    return z
	
def add (arg1, arg2):
    return arg1 + arg2

def sub (arg1, arg2):
    return arg1 - arg2

print ('Addition:')
print ( doIt (add, 2, 3) )    # Passing the name of the function 
                              # and its arguments

print ('Subtraction:')
print ( doIt (sub, 2, 3) )
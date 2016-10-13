def add():
    print ( 'Add' )
	
def sub():
    print ( 'Sub' )
	
a = [add, sub]

for i in range(len(a)):
    a [i] ( )    # Add two parenthese and include arguments, 
                 # if any
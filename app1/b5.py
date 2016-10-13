>>> a = []    # The empty list
>>> a
[]
>>> b = [1, 2.3, 'Arrival', False] # Elements of different types
>>> b[0]                # Accessing the fist element in
1                       # the list
>>> b[2]                # Accessing the third element
'Arrival'
>>> b[0:2]    # Extract a part of the list
[1, 2.3]      # Two is the size of the new list
>>> c = [0] * 6     # Creating and initializing
>>> c                # a list of size 6
[0, 0, 0, 0, 0, 0]
>>> len(c)   # Returns the size of a list
6
>>> 'Arrival' in b      # Check if an element is in the list
True
>>> d = b + b     # Combining two lists into one list
>>> d
[1, 2.3, 'Arrival', False, 1, 2.3, 'Arrival', False]
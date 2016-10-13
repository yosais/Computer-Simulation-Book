# The first field is always the time
e1 = (10, 'Arrival')
e2 = (5, 'Departure')
e3 = (2, 'Fully_Charged')
Event_List = []
Event_List += [e1]
Event_List += [e2]
Event_List += [e3]
Event_List.sort()
print(Event_List)
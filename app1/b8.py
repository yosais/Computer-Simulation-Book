import heapq
from heapq import *
Event_List =[]
heappush(Event_List, (10, 'Arrival'))
heappush(Event_List, (5, 'Departure'))
heappush(Event_List, (2, 'Fully_Charged'))
# Print the first item in the heap
print ( heappop(Event_List) )
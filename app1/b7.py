import queue
from queue import Queue
Event_List = queue.PriorityQueue()
for item in ((10, 'Arrival'), (5, 'Departure'), (2, 'Fully_Charged')):
	Event_List.put(item)
while not Event_List.empty():
	print(Event_List.get()) 
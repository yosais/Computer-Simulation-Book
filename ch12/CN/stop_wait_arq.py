import random as rnd
import queue
import statistics as stat

# Define a dictionary to hold the simulation parameters
param = {'Timeout_Duration': 1, 
		 'P' : 0.2, # Frame Error Rate (FER)
		 'Frame_Trans_Time': 1, # Frame transmission time
		 'Num_Frames': 3
		}

#-------------- Global Variables --------------
Frames_Received = 0.0
Count_Frames = 0.0
clock = 0.0
evList = queue.PriorityQueue()

#-------------- Event Generators --------------
# REG for the sender start event
def sender_start_event (clock, param):
	ev = (clock, "sender_start", sender_start_event_handler)
	return ev

# REG for the receiver start event
def receiver_start_event (clock, param):
	ev = (clock, "receiver_start", 
	                receiver_start_event_handler)
	return ev

# REG for the frame transmission event
def frame_trans_event (clock, param):
	global Count_Frames 
	if(Count_Frames < param['Num_Frames']):
		Count_Frames += 1
		ev = (clock, "transmission", 
		                frame_trans_event_handler)
		return ev

# REG for the timeout event
def timeout_event (clock, param):
	t = param['Timeout_Duration']
	ev = (clock+t, "timeout", timeout_event_handler)
	return ev

# REG for the frame reception event
def frame_reception_event (clock, param):
	t = param['Frame_Trans_Time']
	ev = (clock+t, "reception", 
	                    frame_reception_event_handler)
	return ev

# REG for the acknowledgement event
def ack_event (clock, param):
	ev = (clock, "ack", ack_reception_event_handler)
	return ev

#-------------- Event Handlers --------------
# Event handler for the sender start event
def sender_start_event_handler (clock, param):
	global Count_Frames
	Count_Frames = 0.0
	# Schedule the first frame transmission event
	schedule_event( frame_trans_event (clock, param) )

# Event handler for the receiver start event
def receiver_start_event_handler (clock, param):
	global Frames_Received
	Frames_Received = 0.0

# Event handler for the frame transmission event
def frame_trans_event_handler (clock, param):
	# Generate a frame reception event if frame is going 
	# to be succefully received
	if rnd.random() <= param['P']:
		# Frame is damaged. Generate a timeout event
		schedule_event( timeout_event (clock, param) )
	else:
		# Frame is successfully delivered
		schedule_event( 
		        frame_reception_event (clock, param) )

# Event handler for the frame reception event
def frame_reception_event_handler (clock, param):
	global Frames_Received
	Frames_Received += 1
	schedule_event( ack_event (clock, param) )

# Event handler for the ack event
def ack_reception_event_handler (clock, param):
	schedule_event( frame_trans_event (clock, param) )

# Event handler for the timeout event
def timeout_event_handler (clock, param):
	global Count_Frames
	# Re-transmit the frame again
	Count_Frames = Count_Frames - 1;
	schedule_event( frame_trans_event (clock, param) )

# Insert an event into the event list		
def schedule_event(ev):
	global evList
	if ev != None:
		evList.put(ev)

#----- Start Simulation -----

# 1. Initialize sender and receiver
schedule_event( sender_start_event (clock, param) )
schedule_event( receiver_start_event (clock, param) )

# 2. Run the simulation loop
while not evList.empty():
	ev = evList.get()
	print(ev)
	clock = ev[0]
	ev[2](clock, param)
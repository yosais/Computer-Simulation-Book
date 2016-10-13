import random as rnd
import queue
import statistics as stat
import bisect

# Define a dictionary to hold the simulation parameters
param = {'Timeout_Duration': 1, 
    'P' : 0.5,    # Frame Error Rate (FER)
    'Frame_Trans_Time': 1,    # Frame transmission time
    'Num_Frames': 1
}

#-------------- Global Variables --------------
Frames_Received = 0.0
Count_Frames = 0.0
clock = 0.0
#----------------------------------------------

evList = []

cur_timeout_event = None

def insert(ev):
    bisect.insort_right(evList, ev)

def cancel(ev):
    evList.remove(ev)

def run():
    global evList
    while evList:
        ev = evList.pop(0)
        clock = ev[0]
        ev[2](clock, param)
#-------------- Event Generators --------------
# REG for the start event
def start_event (clock, param):
    ev = (clock, "start", start_event_handler)
    return ev


# REG for the frame transmission event
def frame_trans_event (clock, param):
    global Count_Frames 
    if(Count_Frames < param['Num_Frames']):
        Count_Frames += 1
        ev = (clock, "transmission", frame_trans_event_handler)
        return ev

# REG for the timeout event
def timeout_event (clock, param):
    t = param['Timeout_Duration']
    ev = (clock+t, "timeout", timeout_event_handler)
    return ev

# REG for the frame reception event
def frame_reception_event (clock, param):
    t = param['Frame_Trans_Time']
    ev = (clock+t, "reception", frame_reception_event_handler)
    return ev

# REG for the acknowledgement event
def ack_event (clock, param):
    ev = (clock, "ack", ack_reception_event_handler)
    return ev

#-------------- Event Handlers --------------
# Event handler for the sender start event
def start_event_handler (clock, param):
    global Count_Frames, Frames_Received
    Count_Frames = 0.0
    Frames_Received = 0.0

    # Schedule the first frame transmission event
    schedule_event( frame_trans_event (clock, param) )

# Event handler for the frame transmission event
def frame_trans_event_handler (clock, param):
    global cur_timeout_event
    schedule_event( frame_reception_event (clock, param) )
    cur_timeout_event = timeout_event (clock, param)
    schedule_event( cur_timeout_event )

# Event handler for the frame reception event
def frame_reception_event_handler (clock, param):
    global Frames_Received, cur_timeout_event
    if rnd.random() > param['P']:
        # Frame is OK
        Frames_Received += 1
        schedule_event( ack_event (clock, param) )
        # Cancel the pending timeout event
        cancel(cur_timeout_event)

# Event handler for the ack event
def ack_reception_event_handler (clock, param):
    schedule_event( frame_trans_event (clock, param) )

# Event handler for the timeout event
def timeout_event_handler (clock, param):
    global Count_Frames
    # Re-transmit the frame again
    Count_Frames = Count_Frames - 1;
    schedule_event( frame_trans_event (clock, param) )

#-------------------------------------------------------
# Insert an event into the event list       
def schedule_event(ev):
    global evList
    if ev != None:
        insert(ev)

#-------------------------------------------------------
# Schedule the first frame transmission event
schedule_event( start_event (clock, param) )

# Simulation Loop
run()
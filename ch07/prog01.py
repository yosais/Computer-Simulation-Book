import random as rnd
import queue
import statistics as stat
# Compute the theoretical value using the calcualtor at
# http://www.supositorio.com/rcalc/rcalclite.htm
# Define a dictionary to hold the simulation parameters
param = {'_lambda': 0.2, 
         '_mu': 0.3,
         # Total number of arrival events
         'Num_Arrival_Ev': 100000
        }
# Define a dictionary to hold the state variables
state_var = {'q_length': 0, 
             'server_busy': False
            }
# Define a dictionary to hold the output variables
out_var = { 'arrs': [], 
            'deps': [],
            'Count_Arrival_Ev': 0
          }
# Define the global event list
evList = queue.PriorityQueue()
# REG for the arrival event
def get_next_arrival_event (clock, param):
    out_var['Count_Arrival_Ev'] += 1
    iat = rnd.expovariate(param['_lambda'])
    ev = (clock+iat, "arrival", arrival_event_handler)
    return ev
# REG for the departure event	
def get_next_departure_event (clock, param):
    st = rnd.expovariate(param['_mu'])
    ev = (clock+st, "departure", departure_event_handler)
    return ev
# Event handler for the arrival event
def arrival_event_handler (clock, state_var, out_var, param):
    state_var['q_length'] += 1
    out_var['arrs'].append(clock)	# Record arrival time
    if state_var['server_busy'] == False:
        state_var['server_busy'] = True
        schedule_event(get_next_departure_event(clock, param))
    if out_var['Count_Arrival_Ev'] < param['Num_Arrival_Ev']:	
        schedule_event(get_next_arrival_event(clock, param))
# Event handler for the departure event	
def departure_event_handler (clock, state_var, out_var, param):
    state_var['q_length'] -= 1
    out_var['deps'].append(clock)	# Record departure time
    if state_var['q_length'] == 0:
        state_var['server_busy'] = False
    else:
        state_var['server_busy'] = True
        schedule_event(get_next_departure_event(clock, param))
# Insert an event into the event list		
def schedule_event(ev):
    global evList
    evList.put(ev)
# Main simulation function
def sim(state_var, out_var, param):
    global evList
    clock = 0
    evList = queue.PriorityQueue()
    # Reset state and output variables
    state_var['q_length'] = 0
    state_var['server_busy'] = False
    out_var['arrs'] = []
    out_var['deps'] = []
    out_var['Count_Arrival_Ev'] = 0
    # Initialize (seed) the RNG	
    #rnd.seed(10)
    # Insert initial event
    ev = get_next_arrival_event(clock, param)
    schedule_event(ev)
    # Start simulation
    while not evList.empty():
        ev = evList.get()
        clock = ev[0]
        if ev[1] == "arrival":
            ev[2](clock, state_var, out_var, param)
        else:
            ev[2](clock, state_var, out_var, param)
def main():
    sim(state_var, out_var, param)
    # Print statistics
    d = list(map(lambda x,y: x-y, 
                    out_var['deps'], out_var['arrs']))
    print ("Avg Delay = ", stat.mean(d))
if __name__ == '__main__':
    main()
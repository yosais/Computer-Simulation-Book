# Inputs
T = 10.0
Arr_Times = [0.0,   1.097, 5.526, 9.258]
Dep_Times = [0.878, 2.274, 7.271, 9.477]
# Notice that the time of arrival of next customer is always 
# larger than the time of departure of the customer currently 
# at service. For example, compare 1.097 with 0.878. 
# Thus, the waiting time is zero for every customer and every 
# entry in the list w represents the service time for each
# customer
# Computing number of departures
D = len(Dep_Times)
# Computing throughput (tau)
tau = D / T
# w (time spent in system by customer) = d (departure time) - 
#                                         a (arrival time)
w = []
for d , a in zip(Dep_Times, Arr_Times):
w.append(d - a)
# Computing the server busy time
B = sum(w)
# Computing the average service time per customer
Ts = B / D
# Computing utilization
U = tau * Ts
# Computing response time
W = sum(w) / D
# Computing the average number of customers in the system
L = tau * W
# Output
print 'Throughput = ' , tau                    # = 0.4
print 'Utilization' ,  U                        # = 0.4019
print 'Response Time = ' , W                     # = 1.00475
print 'Average Number of Customers = ' , L        # = 0.4019
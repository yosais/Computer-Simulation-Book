Tot_Num_Pkt = 10
IAT = [2, 5, 1, 4, 1, 3, 3, 2, 4, 5]
ST = [12, 10, 16, 9, 10, 13, 17, 10, 8, 12]
N = 0    # Keep track of number of pkts in system
Num_Pkt_Simulated = 0    # Keep track of departed pkts
ind1 = 0    # Index for the IAT list
ind2 = 0    # Index for the ST list
Infinity = 999
Arr_Time = 0
Dep_Time_1 = Infinity
Dep_Time_2 = Infinity
# Create lists for collecting information
# List of zeros of size equal to Tot_Num_Pkt
ArrTime = [0] * Tot_Num_Pkt
DepTime = [0] * Tot_Num_Pkt
ServerAssigned = [0] * Tot_Num_Pkt
StartService = [0] * Tot_Num_Pkt
Server_1_Free = True    # Keep track of state of server 1
Server_2_Free = True    # Keep track of state of server 2
while Num_Pkt_Simulated < Tot_Num_Pkt:
if Arr_Time <= Dep_Time_1 and Arr_Time <= Dep_Time_2 and 
ind1 < Tot_Num_Pkt:
Arr_Time = Arr_Time + IAT[ind1]
ArrTime[ind1] = Arr_Time
ind1 = ind1 + 1
N = N + 1
if Server_1_Free == True:
StartService[ind2] = Arr_Time
Dep_Time_1 = Arr_Time + ST[ind2]
ServerAssigned[ind2] = 1
DepTime[ind2] = Dep_Time_1
ind2 = ind2 + 1
Server_1_Free = False
elif Server_2_Free == True:
StartService[ind2] = Arr_Time
Dep_Time_2 = Arr_Time + ST[ind2]
ServerAssigned[ind2] = 2
DepTime[ind2] = Dep_Time_2
ind2 = ind2 + 1
Server_2_Free = False
elif Dep_Time_1 <= Dep_Time_2:
Num_Pkt_Simulated = Num_Pkt_Simulated + 1
print '---> Departure at Server 1 at ' , 
Dep_Time_1
N = N - 1
if N > 0 and ind2 < Tot_Num_Pkt:
StartService[ind2] = Dep_Time_1
Dep_Time_1 = Dep_Time_1 + ST[ind2]
ServerAssigned[ind2] = 1
DepTime[ind2] = Dep_Time_1
ind2 = ind2 + 1
else:
Server_1_Free = True
Dep_Time_1 = Infinity
else:
Num_Pkt_Simulated = Num_Pkt_Simulated + 1
print '---> Departure at Server 2 at ' , 
Dep_Time_2
N = N - 1
if N > 0  and ind2 < Tot_Num_Pkt:
StartService[ind2] = Dep_Time_2
Dep_Time_2 = Dep_Time_2 + ST[ind2]
ServerAssigned[ind2] = 2
DepTime[ind2] = Dep_Time_2
ind2 = ind2 + 1
else:
Server_2_Free = True
Dep_Time_2 = Infinity
print 'Arr_Time = %d , Dep_Time_1 = %d , Dep_Time_2 = %d' 
% (Arr_Time, Dep_Time_1, Dep_Time_2)
print 'ArrTime: ' , ArrTime
print 'DepTime: ' , DepTime
print 'ServerAssigned: ' , ServerAssigned
print 'StartService: ' , StartService
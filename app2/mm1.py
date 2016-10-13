# IAT = Average Inter-Arrival Time
# ST = Average Service Time
# Size of packet is its service time (in time units not bits)
# Station contains a queue (Q) and server (S)

from scheduler import Scheduler
from simEntity import SimEntity
import random as rnd
import queue

class TrafficGen(SimEntity):

    def __init__(self, _scheduler, _station, _id, _IAT = 1.0, _ST = 1.0):
        super(TrafficGen, self).__init__(_scheduler, _id)
        self.station = _station
        self.IAT = _IAT
        self.ST = _ST
        self.schedule( self, 'Packet_Arrival', self.scheduler.time + rnd.expovariate(1.0/self.IAT) )

    def evHandler(self, ev):
        # Handle arrival event
        pkt = Packet( rnd.expovariate(1.0/self.ST) )
        pkt.Arrival_Time = self.scheduler.time
        self.schedule(self.station, pkt, self.scheduler.time)
        # Schedule next packet arrival
        self.schedule( self, 'Packet_Arrival', self.scheduler.time + rnd.expovariate(1.0/self.IAT) )


class Packet:
    def __init__(self, _size):
        self.size = _size
        self.Arrival_Time = 0.0
        self.Service_At = 0.0
        self.Departure_Time = 0.0

    # Total time spent in system
    def delay(self):
        return self.Departure_Time - self.Arrival_Time

    def info(self):
        print("Arrival_Time = %.2f, Service_At = %.2f, Service_Time = %.2f, Departure_Time = %.2f" % (self.Arrival_Time, self.Service_At, self.size, self.Departure_Time))


class Server(SimEntity):
    busy = False

    def __init__(self, _scheduler, _station, _id):
        super(Server, self).__init__(_scheduler, _id)
        self.station = _station

    def evHandler(self, ev):
        global Num_Pkts, Total_Delay

        if isinstance(ev.type, Packet):
            pkt = ev.type
            self.busy = True
            pkt.Service_At = self.scheduler.time
            pkt.Departure_Time = self.scheduler.time + pkt.size
            #pkt.info()
            Num_Pkts = Num_Pkts + 1
            Total_Delay = Total_Delay + pkt.delay()
            self.schedule(self, 'End_of_Service', self.scheduler.time + pkt.size)
        elif ev.type == 'End_of_Service':
            self.busy = False
            self.schedule(self.station, 'Server_Available', self.scheduler.time)
        else:
            print('Server is supposed to receive packets!')

    def isBusy(self):
        return self.busy


class Station(SimEntity):

    def __init__(self, _scheduler, _id):
        super(Station, self).__init__(_scheduler, _id)
        self.Q = queue.Queue()
        self.S = Server(_scheduler, self, _id)

    def evHandler(self, ev):
        # Handle arriving packet
        if isinstance(ev.type, Packet):
            pkt = ev.type
            if not self.S.isBusy():
                self.schedule(self.S, pkt, self.scheduler.time)
            else:
                self.Q.put(pkt)
        elif ev.type == 'Server_Available':
            if not self.Q.empty():
                pkt = self.Q.get()
                self.schedule(self.S, pkt, self.scheduler.time)
        else:
            print('Station is supposed to receive packets only!')

Num_Pkts = 0.0
Total_Delay = 0.0

scheduler = Scheduler(100000)
station = Station(scheduler, 1)
src = TrafficGen(scheduler, station, 2, 3.33, 2.5)
scheduler.run()

print('Avg Delay = %.2f' % (Total_Delay / Num_Pkts))
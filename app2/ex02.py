from scheduler import Scheduler
from simEntity import SimEntity

class Node(SimEntity):

    def __init__(self, _scheduler, _id):
        super(Node, self).__init__(_scheduler)
        self.id = _id
        self.schedule(self, 'Initialize', self.scheduler.time + 2.0)

    def setNeighbor(self, n):
        self.neighbor = n

    def evHandler(self, ev):
        print( ev.type + ' From ' + str(ev.src.id) + ' To ' + str(ev.target.id) + ' @ ' + str(ev.time) )
        self.schedule(self.neighbor, 'Hi', self.scheduler.time + 3.0)




scheduler = Scheduler(4)

n1 = Node(scheduler, 1)
n2 = Node(scheduler, 2)

n1.setNeighbor(n2)
n2.setNeighbor(n1)

scheduler.run()
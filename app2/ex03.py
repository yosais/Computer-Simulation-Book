# Remove n1.setNeighbor(n2) && n2.setNeighbor(n1)
# Use a link to connect the two nodes
# A link has two ends: a & b

from scheduler import Scheduler
from simEntity import SimEntity

class Node(SimEntity):

    def __init__(self, _scheduler, _id):
        super(Node, self).__init__(_scheduler, _id)
        self.schedule( self, 'Initialize', self.scheduler.time + 2.0 )

    def setNeighbor(self, n):
        self.neighbor = n

    def evHandler(self, ev):
        print( ev.type + ' From ' + str(ev.src.id) + ' To ' + str(ev.target.id) + ' @ ' + str(ev.time) )
        self.schedule( self.neighbor, 'Hi', self.scheduler.time + 3.0 )


class Link(SimEntity):

    def __init__(self, _scheduler, _id):
        super(Link, self).__init__(_scheduler, _id)

    def setNeighbors(self, _a, _b):
        self.a = _a
        self.b = _b

    def evHandler(self, ev):
        print( ev.type + ' From ' + str(ev.src.id) + ' To ' + str(ev.target.id) + ' @ ' + str(ev.time) )
        if( ev.src.id == self.a.id ):
            self.schedule( self.b, 'Hi', self.scheduler.time + 3.0 )
        else:
            self.schedule( self.a, 'Hi', self.scheduler.time + 3.0 )



scheduler = Scheduler(6)

n1 = Node(scheduler, 1)
n2 = Node(scheduler, 2)
l = Link(scheduler, 3)

n1.setNeighbor(l)
n2.setNeighbor(l)
l.setNeighbors(n1, n2)

scheduler.run()
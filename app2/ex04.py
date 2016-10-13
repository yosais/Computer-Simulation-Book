from scheduler import Scheduler
from simEntity import SimEntity
from event import Event

class Node(SimEntity):
    def __init__(self, _scheduler, _id):
        super(Node, self).__init__(_scheduler, _id)
        self.schedule(self, 'Self_Message', self.scheduler.time + 5.0)
        self.schedule(self, 'Self_Message', self.scheduler.time + 3.0)
        self.schedule(self, 'Self_Message', self.scheduler.time + 4.0)
        self.schedule(self, 'Self_Message', self.scheduler.time + 1.0)
        self.schedule(self, 'Self_Message', self.scheduler.time + 2.0)
        ev = Event(self, self, 'Self_Message', self.scheduler.time + 1.0)
        self.cancel(ev)

    def evHandler(self, ev):
        print( ev.type + ' From ' + str(ev.src.id) + ' To ' + str(ev.target.id) + ' @ ' + str(ev.time) )



scheduler = Scheduler(5)

Node(scheduler, 1)

scheduler.run()

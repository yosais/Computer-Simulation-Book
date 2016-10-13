from scheduler import Scheduler
from simEntity import SimEntity


class Node(SimEntity):
    def __init__(self, _scheduler, _id):
        super(Node, self).__init__(_scheduler, _id)
        self.schedule(self, 'Self_Message', self.scheduler.time + 2.0)

    def evHandler(self, ev):
        print( ev.type + ' From ' + str(ev.src.id) + ' To ' + str(ev.target.id) + ' @ ' + str(ev.time) )
        self.schedule(self, 'Hi', self.scheduler.time + 2.0)


scheduler = Scheduler(3)

Node(scheduler, 1)

scheduler.run()
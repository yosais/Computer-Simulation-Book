# The variable self.count_events counts events generated. The number of events executed will also be equal to this
# number.
#
# You insert event based on its time. If there are two events occurring at the same time, the second sorting
# criterion is to use the id of the target. The third sorting criterion is to use the id of the source.

from queue import PriorityQueue

class Scheduler:

    def __init__(self, _Max_Num_Events):
        self.evList = PriorityQueue()
        self.time = 0.0
        self.count_events = 0
        self.Max_Num_Events = _Max_Num_Events

    def insert(self, ev):
        if ( self.count_events < self.Max_Num_Events ):
            self.count_events = self.count_events + 1
            self.evList.put( (ev.time, self.count_events, ev) )

    def remove(self, ev):
        _evList = PriorityQueue()
        for i in range(self.evList.qsize()):
            tmp = self.evList.get()
            _ev = tmp[2]
            if not _ev == ev:
                _evList.put(tmp)
        self.evList = _evList

    def head(self):
        ev = self.evList.get()
        self.time = ev[2].time
        return ev[2]

    def run(self):
        count = 0
        while( not self.empty() ):
            ev = self.head()
            self.time = ev.time
            count += 1
            ev.target.evHandler(ev)

    def empty(self):
        return self.evList.empty()

    def reset(self):
        self.evList = None
        self.time = 0.0
        self.count_events = 0

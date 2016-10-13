from event import Event

class SimEntity:

    def __init__(self, _scheduler, _id):
        self.scheduler = _scheduler
        self.id = _id

    def schedule(self, target, type, time):
        ev = Event(self, target, type, time)
        self.scheduler.insert(ev)

    def cancel(self, ev):
        self.scheduler.remove(ev)

    def evHandler(self, ev):
        pass

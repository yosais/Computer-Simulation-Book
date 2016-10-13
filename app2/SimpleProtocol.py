from state import State
from stateMachine import StateMachine
from event import Event


class Bad(State):
    def __init__(self):
        super(Bad, self).__init__()

    def action(self):
        print("Bad State")

    def next(self, event):
        if event.type == "B":
            return self
        else:
            return Good()


class Good(State):
    def __init__(self):
        super(Good, self).__init__()

    def action(self):
        print("Good State")

    def next(self, event):
        if event.type == "G":
            return self
        else:
            return Bad()


class Protocol(StateMachine):
    def __init__(self, _initialState):
        super(Protocol, self).__init__(_initialState)


p = Protocol(Bad())
p.applyEvent(Event(None, None, "G", None))
p.applyEvent(Event(None, None, "G", None))
p.applyEvent(Event(None, None, "B", None))
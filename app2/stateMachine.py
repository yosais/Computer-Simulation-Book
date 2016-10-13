# http://python-3-patterns-idioms-test.readthedocs.org/en/latest/StateMachine.html#the-table


class StateMachine:
    def __init__(self, initialState):
        self.currentState = initialState
        self.currentState.action()

    # Make transition
    def applyEvent(self, event):
        self.currentSate = self.currentState.next(event)
        self.currentSate.action()

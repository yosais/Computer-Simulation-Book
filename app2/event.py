class Event:
    def __init__(self, _src, _target, _type, _time):
        self.src = _src
        self.target = _target
        self.type = _type
        self.time = _time

    def __eq__(self, other):
        return self.__dict__ == other.__dict__

import bisect
evList = []
def insert(ev):
    bisect.insort_right(evList, ev)
def cancel(ev):
    evList.remove(ev)
def run():
    while evList:
        ev = evList.pop(0)
        clock = ev[0]
        ev[2](clock, param)

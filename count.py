#!/usr/bin/python

import slot, queens
import sys

def count(initial):
    CLOSED = {}
    OPEN = [initial]

    while True:
        if not OPEN:
            return len(CLOSED)

        n = OPEN.pop()

        CLOSED[n] = None

        gen = n.generate()
        gen = [s for s in gen if s not in CLOSED]

        OPEN += gen

s = slot.State(slot.State.goal)

print "Slot: %d" % count(s)

for i in xrange(8):
    q = queens.State(i)
    print "Queens(%d): %d" % (i, count(q))

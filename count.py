#!/usr/bin/python

import slot, queens
import sys

def count(initial):
    CLOSED = {}
    OPEN = [initial]

    while True:
        if not OPEN:
            goals = [i for i in CLOSED if i.is_goal()]
            return (len(CLOSED), len(goals))

        n = OPEN.pop()

        CLOSED[n] = None

        gen = n.generate()
        gen = [s for s in gen if s not in CLOSED]

        OPEN += gen

s = slot.State(slot.State.goal)

c = count(s)
print "Slot: %d (goals: %d)" % c

for i in xrange(8):
    q = queens.State(i)
    c = count(q)
    print "Queens(%d): %d (goals: %d)" % ((i, ) + c)

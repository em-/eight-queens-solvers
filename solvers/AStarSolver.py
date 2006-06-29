#!/usr/bin/python2.3

from solvers import TreeSolver

import bisect

class PQueue(list):
    def __init__(self, *args, **kwds):
        list.__init__(self, *args, **kwds)
        self.counter = 0

    def add(self, item, key=None):
        # The counter is needed to keep the sorting stable
        if key:
            t = (key(item), self.counter, item)
        else:
            t = (item, self.counter, item)
        self.counter += 1
        bisect.insort(self, t)

    def pop(self):
        i = list.pop(self, 0)
        return i[2]

    def peek(self):
        return self[0][2]

class AStarSolver(TreeSolver):
    def __init__(self, initial_state):
        TreeSolver.__init__(self)
        self.OPEN = PQueue()
        self.CLOSED = []
        self.G = {}

        self.G[initial_state] = 0
        self.OPEN.add(initial_state, key=lambda x: 0)

    def solve(self):
        while True:
            if not self.OPEN:
                return None

            def f(node):
                return self.G[node] + node.heuristics()

            n = self.OPEN.pop()

            if n.is_goal():
                return self.get_track(n)

            self.CLOSED.append(n)

            successors = n.generate()

            successors = [s for s in successors if s not in self.CLOSED]
            successors = [s for s in successors if s not in self.OPEN]

            for s in successors:
                self.set_parent(s, n)
                # FIXME: use a true distance graph, instead of using "1"
                self.G[s] = self.G[n] + 1
                self.OPEN.add(s, key=f)


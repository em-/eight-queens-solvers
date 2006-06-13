#!/usr/bin/python2.3

from solvers import TreeSolver

class SortedList(list):
    def insort(self, item, key=None):
        iter = enumerate(self)

        if not key:
            key = lambda x: x

        try:
            index, value = iter.next()
            while key(value) < key(item):
                index, value = iter.next()
        except StopIteration:
            index = len(self)

        self.insert(index, item)

class AStarSolver(TreeSolver):
    def __init__(self, initial_state):
        TreeSolver.__init__(self)
        self.OPEN = SortedList()
        self.CLOSED = []
        self.G = {}

        self.G[initial_state] = 0
        self.OPEN.append(initial_state)

    def solve(self):
        while True:
            if not self.OPEN:
                return None

            def f(node):
                return self.G[node] + node.heuristics()

            n = self.OPEN.pop(0)

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
                self.OPEN.insort(s, key=f)


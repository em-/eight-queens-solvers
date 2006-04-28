#!/usr/bin/env python

from solvers import TreeSolver

class BreadthSolver(TreeSolver):
    def __init__(self, initial_state):
        TreeSolver.__init__(self)
        self.OPEN = []
        self.OPEN.append(initial_state)
        self.CLOSED = []

    def solve(self):
        while True:
            if not self.OPEN:
                return None

            n = self.OPEN.pop(0)

            if n.is_goal():
                return self.get_track(n)

            self.CLOSED.append(n)

            successors = n.generate()

            successors = [s for s in successors if s not in self.CLOSED]
            successors = [s for s in successors if s not in self.OPEN]

            for s in successors:
                self.set_parent(s, n)

            self.OPEN += successors


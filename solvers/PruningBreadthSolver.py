#!/usr/bin/env python

from solvers import TreeSolver

class PruningBreadthSolver(TreeSolver):
    def __init__(self, initial_state, beta):
        TreeSolver.__init__(self)
        self.beta = beta
        self.OPEN = []
        self.OPEN.append(initial_state)
        self.RESERVE = []
        self.CLOSED = []

    def solve(self):
        while True:
            if not self.OPEN:
                if not self.RESERVE:
                    return None
                else:
                    self.RESERVE.sort(lambda a, b: cmp(a.heuristics(), b.heuristics()))
                    self.OPEN = self.RESERVE[:self.beta] + self.OPEN
                    self.RESERVE = []

            n = self.OPEN.pop(0)

            if n.is_goal():
                return self.get_track(n)

            self.CLOSED.append(n)

            successors = n.generate()

            successors = [s for s in successors if s not in self.CLOSED]
            successors = [s for s in successors if s not in self.OPEN]

            for s in successors:
                self.set_parent(s, n)
                if s.is_goal():
                    return self.get_track(s)

            self.RESERVE += successors


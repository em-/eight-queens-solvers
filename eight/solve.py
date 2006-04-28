#!/usr/bin/env python

import unittest
from state import State

class Solver:
    def __init__(self, initial_state):
        raise NotImplementedError

    def solve(self):
        raise NotImplementedError

class TreeSolver(Solver):
    def __init__(self):
        self.tree = {}

    def set_parent(self, child, parent):
        self.tree[child] = parent

    def get_track(self, goal):
        track = [goal]
        node = goal
        while self.tree.has_key(node):
            node = self.tree[node]
            track.append(node)
        return track

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


class DepthSolver(TreeSolver):
    def __init__(self, initial_state):
        TreeSolver.__init__(self)
        self.OPEN = []
        self.OPEN.append(initial_state)
        self.CLOSED = []

    def solve(self):
        while True:
            if not self.OPEN:
                return None
            n = self.OPEN.pop()
            if n.is_goal():
                return self.get_track(n)

            self.CLOSED.append(n)

            successors = n.generate()

            successors = [s for s in successors if s not in self.CLOSED]
            successors = [s for s in successors if s not in self.OPEN]

            for s in successors:
                self.set_parent(s, n)

            self.OPEN += successors


class TestSolver:
    solver_cls = Solver

    def testgoal(self):
        goal = State(State.goal)
        solver = self.solver_cls(goal)
        solution = solver.solve()
        self.failUnlessEqual(solution[0], goal)

    def testsimplesolution(self):
        goal = State(State.goal)
        board = [
            [1, 2, 3],
            [4, 5, 6],
            [7, 0, 8]
        ]
        initial = State(board)
        solver = self.solver_cls(initial)
        solution = solver.solve()
        self.failUnlessEqual(solution[0], goal)

    def testmediumsolution(self):
        goal = State(State.goal)
        board = [
            [0, 1, 2],
            [4, 5, 3],
            [7, 8, 6]
        ]
        initial = State(board)
        solver = self.solver_cls(initial)
        solution = solver.solve()
        self.failUnlessEqual(solution[0], goal)

    def testcomplexsolution(self):
        goal = State(State.goal)
        moves = ('up', 'left', 'right', 'down')
        m = (1,1,0,0,3,2,1,2,2,1,0,1,3,2,0,3,2,0,1,3,3,0,3,2,0,0,3,3,0,3,0)
        initial = goal
        for i in m:
            try:
                initial = initial.move_empty(moves[i])
            except ValueError:
                pass
        solver = self.solver_cls(initial)
        solution = solver.solve()
        self.failUnlessEqual(solution[0], goal)


class TestBreadthSolver(TestSolver, unittest.TestCase):
    solver_cls = BreadthSolver

class TestDepthSolver(TestSolver, unittest.TestCase):
    solver_cls = DepthSolver

if __name__ == '__main__':
    unittest.main()

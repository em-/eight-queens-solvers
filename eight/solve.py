#!/usr/bin/env python

import unittest
from state import State

class Solver:
    def __init__(self, initial_state):
        raise NotImplementedError

    def solve(self):
        raise NotImplementedError


class BreadthSolver(Solver):
    def __init__(self, initial_state):
        self.OPEN = []
        self.OPEN.append(initial_state)
        self.CLOSED = []

    def solve(self):
        if self.OPEN[0].is_goal():
            return self.OPEN[0]

        while True:
            if not self.OPEN:
                return None
            n = self.OPEN.pop(0)
            self.CLOSED.append(n)

            successors = []
            moves = ('up', 'left', 'right', 'down')
            for move in moves:
                try:
                    s = n.move_empty(move)
                    successors.append(s)
                except ValueError:
                    pass

            successors = [s for s in successors if s not in self.CLOSED]
            successors = [s for s in successors if s not in self.OPEN]
            
            for s in successors:
                if s.is_goal():
                    return s

            self.OPEN += successors


class DepthSolver(Solver):
    def __init__(self, initial_state):
        self.OPEN = []
        self.OPEN.append(initial_state)
        self.CLOSED = []

    def solve(self):
        while True:
            if not self.OPEN:
                return None
            n = self.OPEN.pop()
            if n.is_goal():
                return n

            self.CLOSED.append(n)

            successors = []
            moves = ('up', 'left', 'right', 'down')
            for move in moves:
                try:
                    s = n.move_empty(move)
                    successors.append(s)
                except ValueError:
                    pass

            successors = [s for s in successors if s not in self.CLOSED]
            successors = [s for s in successors if s not in self.OPEN]

            self.OPEN += successors


class TestSolver:
    solver_cls = Solver

    def testgoal(self):
        goal = State(State.goal)
        solver = self.solver_cls(goal)
        solution = solver.solve()
        self.failUnlessEqual(goal, solution)

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
        self.failUnlessEqual(solution, goal)
    
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
        self.failUnlessEqual(solution, goal)

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
        self.failUnlessEqual(solution, goal)


class TestBreadthSolver(TestSolver, unittest.TestCase):
    solver_cls = BreadthSolver

class TestDepthSolver(TestSolver, unittest.TestCase):
    solver_cls = DepthSolver

if __name__ == '__main__':
    unittest.main()

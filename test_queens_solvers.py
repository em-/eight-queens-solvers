#!/usr/bin/env python

import unittest
from solvers import BreadthSolver, DepthSolver
from queens import State

class TestSolver:
    solver_cls = None
    queens = [
    (
        (0,1),
        (1,3),
        (2,0),
        (3,2)
    ),
    (
        (0,2),
        (1,0),
        (2,3),
        (3,1)
    )
    ]
    goals = [State(4, q) for q in queens]

    def testgoal(self):
        queens = self.queens[0]
        goal = State(4, queens)
        solver = self.solver_cls(goal)
        solution = solver.solve()
        self.failUnlessEqual(solution[0], goal)

    def testsimplesolution(self):
        queens = self.queens[0]
        goal = State(4, queens)
        initial = State(4, queens[:-1])
        solver = self.solver_cls(initial)
        solution = solver.solve()
        self.failUnlessEqual(solution[0], goal)
        self.failUnlessEqual(solution[-1], initial)
        self.failUnlessEqual(len(solution), 2)

    def testmediumsolution(self):
        initial = State(4)
        solver = self.solver_cls(initial)
        solution = solver.solve()
        self.failUnless(solution[0] in self.goals)
        self.failUnlessEqual(solution[-1], initial)

    def testcomplexsolution(self):
        initial = State(4)
        solver = self.solver_cls(initial)
        solution = solver.solve()
        self.failUnless(solution[0] in self.goals)


class TestBreadthSolver(TestSolver, unittest.TestCase):
    solver_cls = BreadthSolver

class TestDepthSolver(TestSolver, unittest.TestCase):
    solver_cls = DepthSolver

if __name__ == '__main__':
    unittest.main()

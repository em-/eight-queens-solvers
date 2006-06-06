#!/usr/bin/env python

import unittest
from solvers import BreadthSolver, DepthSolver
from queens import State

class TestSolver:
    def solver(self, initial_state):
        raise NotImplementedError

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
        solver = self.solver(goal)
        solution = solver.solve()
        self.failUnlessEqual(len(solution), 1)
        self.failUnlessEqual(solution[0], goal)

    def testsimplesolution(self):
        queens = self.queens[0]
        goal = State(4, queens)
        initial = State(4, queens[:-1])
        solver = self.solver(initial)
        solution = solver.solve()
        self.failUnlessEqual(len(solution), 2)
        self.failUnlessEqual(solution[0], goal)
        self.failUnlessEqual(solution[-1], initial)

    def testmediumsolution(self):
        initial = State(4)
        solver = self.solver(initial)
        solution = solver.solve()
        self.failUnless(solution[0] in self.goals)
        self.failUnlessEqual(solution[-1], initial)

    def testcomplexsolution(self):
        initial = State(6)
        solver = self.solver(initial)
        solution = solver.solve()
        self.failUnless(solution[0].is_goal())

    def testnosolution(self):
        initial = State(3)
        solver = self.solver(initial)
        solution = solver.solve()
        self.failUnlessEqual(solution, None)


class TestBreadthSolver(TestSolver, unittest.TestCase):
    def solver(self, initial_state):
        return BreadthSolver(initial_state)

class TestDepthSolver(TestSolver, unittest.TestCase):
    def solver(self, initial_state):
        return DepthSolver(initial_state)

if __name__ == '__main__':
    unittest.main()

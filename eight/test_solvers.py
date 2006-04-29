#!/usr/bin/env python

import unittest
from solvers import BreadthSolver, DepthSolver
from state import State

class TestSolver:
    solver_cls = None

    def testgoal(self):
        goal = State(State.goal)
        solver = self.solver_cls(goal)
        solution = solver.solve()
        self.failUnlessEqual(solution[0], goal)
        self.failUnlessEqual(len(solution), 1)

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
        self.failUnlessEqual(solution[-1], initial)
        self.failUnlessEqual(len(solution), 2)

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
        self.failUnlessEqual(solution[-1], initial)

    def testcomplexsolution(self):
        goal = State(State.goal)
        moves = ('up', 'left', 'right', 'down')
        m = (1,1,0,0,3,2,1,2,2,1,0,1,3,2,0,3,2,0,1,3,3,0,3,2,0,0,3,3,0,3,0)
        initial = goal
        for i in m:
            try:
                initial = initial.move_slot(moves[i])
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

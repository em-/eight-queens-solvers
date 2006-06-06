#!/usr/bin/env python

import unittest
from solvers import BreadthSolver, DepthSolver, PruningBreadthSolver
from slot import State

class TestSolver:
    def solver(self, initial_state):
        raise NotImplementedError

    def testgoal(self):
        goal = State(State.goal)
        solver = self.solver(goal)
        solution = solver.solve()
        self.failUnlessEqual(len(solution), 1)
        self.failUnlessEqual(solution[0], goal)

    def testsimplesolution(self):
        goal = State(State.goal)
        board = [
            [1, 2, 3],
            [4, 5, 6],
            [7, 0, 8]
        ]
        initial = State(board)
        solver = self.solver(initial)
        solution = solver.solve()
        self.failUnlessEqual(len(solution), 2)
        self.failUnlessEqual(solution[0], goal)
        self.failUnlessEqual(solution[-1], initial)

    def testmediumsolution(self):
        goal = State(State.goal)
        board = [
            [0, 1, 2],
            [4, 5, 3],
            [7, 8, 6]
        ]
        initial = State(board)
        solver = self.solver(initial)
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
                initial = initial._move_slot(moves[i])
            except ValueError:
                pass
        solver = self.solver(initial)
        solution = solver.solve()
        self.failUnlessEqual(solution[0], goal)


class TestBreadthSolver(TestSolver, unittest.TestCase):
    def solver(self, initial_state):
        return BreadthSolver(initial_state)

class TestDepthSolver(TestSolver, unittest.TestCase):
    def solver(self, initial_state):
        return DepthSolver(initial_state)

class TestPruningBreadthSolver(TestSolver, unittest.TestCase):
    def solver(self, initial_state):
        # Prune only one of 4 generated states (up, down, left, right)
        # More aggressive pruning didn't give a solution in the complex case
        return PruningBreadthSolver(initial_state, 3)

if __name__ == '__main__':
    unittest.main()

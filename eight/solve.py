#!/usr/bin/env python

import unittest
from state import State

class Solver:
    pass

class BreadthSolver(Solver):
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

            self.OPEN += successors



class TestSolver(unittest.TestCase):
    def testgoal(self):
        goal = State(State.goal)
        solver = BreadthSolver(goal)
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
        solver = BreadthSolver(initial)
        solution = solver.solve()
        self.failUnlessEqual(solution, goal)
    
    def testcomplexsolution(self):
        goal = State(State.goal)
        board = [
            [0, 1, 2],
            [4, 5, 3],
            [7, 8, 6]
        ]
        initial = State(board)
        solver = BreadthSolver(initial)
        solution = solver.solve()
        self.failUnlessEqual(solution, goal)

if __name__ == '__main__':
    unittest.main()

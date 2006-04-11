#!/usr/bin/env python

import unittest

class State:
    goal = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 0]
    ]

    def __init__(self, initial = None):
        if initial:
            if len(initial) != len(initial[0]):
                raise ValueError
            self.board = initial
        else:
            self.board = self.goal

        self.directions = ("up", "down", "left", "right")

    def _get_empty_position(self):
        i = 0
        for line in self.board:
            if 0 in line:
                return (i, line.index(0))
            i += 1
        return None
    
    def _check_range(self, position):
        for i in position:
            if i < 0 or i >= len(self.board):
                return False
        return True

    def move_empty(self, direction):
        if direction not in self.directions:
            raise ValueError
        empty = self._get_empty_position()

        moves = {
            "up":    (-1,  0),
            "down":  (+1,  0),
            "left":  ( 0, -1),
            "right": ( 0, +1)
        }

        dest = map((lambda a, b: a+b), empty, moves[direction])

        if not self._check_range(dest):
            raise ValueError

        self.board[empty[0]][empty[1]] = self.board[dest[0]][dest[1]]
        self.board[dest[0]][dest[1]]   = 0

    def is_goal(self):
        if self.board == self.goal:
            return True
        else:
            return False


class TestState(unittest.TestCase):
    def testgoal(self):
        board = [
            [1, 2, 3],
            [4, 5, 6],
            [7, 8, 0]
        ]
        state = State(board)
        self.failUnless(state.is_goal())

    def testmove(self):
        board = [
            [1, 2, 3],
            [4, 5, 6],
            [7, 8, 0]
        ]
        final = [
            [1, 2, 3],
            [4, 5, 0],
            [7, 8, 6]
        ]
        state = State(board)
        state.move_empty("up")
        self.failUnlessEqual(state.board, final)

    def testillegalmove(self):
        board = [
            [1, 2, 3],
            [4, 5, 6],
            [7, 8, 0]
        ]
        state = State(board)
        self.failUnlessRaises(ValueError, state.move_empty, "down")
    
    def testunknownmove(self):
        state = State()
        self.failUnlessRaises(ValueError, state.move_empty, "aaa")


if __name__ == '__main__':
    unittest.main()

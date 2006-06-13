#!/usr/bin/env python

import unittest
import copy
import memoize
import sets


class State(object):
    __metaclass__ = memoize.Memoized

    goal = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 0]
    ]

    directions = ("up", "left", "right", "down")

    def __init__(self, board):
        if len(board) != len(board[0]):
            raise ValueError
        self.board = board
    
    def __hash__(self):
        return hash(str(self.board))

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

    def _move_slot(self, direction):
        if direction not in self.directions:
            raise ValueError
        empty_slot = self._get_empty_position()

        moves = {
            "up":    (-1,  0),
            "down":  (+1,  0),
            "left":  ( 0, -1),
            "right": ( 0, +1)
        }

        dest = map((lambda a, b: a+b), empty_slot, moves[direction])

        if not self._check_range(dest):
            raise ValueError

        board = copy.deepcopy(self.board)

        board[empty_slot[0]][empty_slot[1]] = self.board[dest[0]][dest[1]]
        board[dest[0]][dest[1]]   = 0

        return State(board)

    def is_goal(self):
        if self.board == self.goal:
            return True
        else:
            return False

    def generate(self):
        successors = []
        for move in self.directions:
            try:
                s = self._move_slot(move)
                successors.append(s)
            except ValueError:
                pass
        return successors

    def heuristics(self):
        h = i = 0
        while i < len(self.board):
            j = 0
            while j < len(self.board[i]):
                if self.board[i][j] != self.goal[i][j]:
                    h += 2 * len(self.board) - (i+j)
                j += 1
            i += 1
        return h

    def __str__ (self):
        string = []
        for row in self.board:
            for item in row:
                if item == 0:
                    string.append(' ')
                else:
                    string.append(str(item))
            string.append('\n')
        return ''.join(string)


class TestState(unittest.TestCase):
    def testgoal(self):
        board = [
            [1, 2, 3],
            [4, 5, 6],
            [7, 8, 0]
        ]
        state = State(board)
        self.failUnless(state.is_goal())
        self.failUnlessEqual(state.heuristics(), 0)

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
        state_moved = state._move_slot("up")
        state_final = State(final)
        self.failUnlessEqual(state_moved, state_final)
        self.failUnlessEqual(state_moved.heuristics(), 2)

    def testillegalmove(self):
        board = [
            [1, 2, 3],
            [4, 5, 6],
            [7, 8, 0]
        ]
        state = State(board)
        self.failUnlessRaises(ValueError, state._move_slot, "down")

    def testunknownmove(self):
        board = [
            [1, 2, 3],
            [4, 5, 6],
            [7, 8, 0]
        ]
        state = State(board)
        self.failUnlessRaises(ValueError, state._move_slot, "aaa")

    def testgenerate(self):
        board = [
            [1, 2, 3],
            [4, 5, 6],
            [7, 8, 0]
        ]
        start = State(board)

        successors = []
        board = [
            [1, 2, 3],
            [4, 5, 6],
            [7, 0, 8]
        ]
        successors.append(State(board))
        board = [
            [1, 2, 3],
            [4, 5, 0],
            [7, 8, 6]
        ]
        successors.append(State(board))

        generated = start.generate()

        generated = sets.Set(generated)
        successors = sets.Set(successors)

        self.failUnlessEqual(successors, generated)

if __name__ == '__main__':
    unittest.main()

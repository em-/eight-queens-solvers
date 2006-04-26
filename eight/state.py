#!/usr/bin/env python

import unittest
import copy
import weakref

class State(object):
    goal = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 0]
    ]

    directions = ("up", "left", "right", "down")

    __instances = weakref.WeakValueDictionary()

    def __new__(cls, board):
        key = cls.__key(board)

        if key not in cls.__instances:
            inst = super(State, cls).__new__(cls, board)
            cls.__instances[key] = inst
        return cls.__instances[key]

    def __init__(self, board):
        if len(board) != len(board[0]):
            raise ValueError
        self.board = board
    
    def _get_empty_position(self):
        i = 0
        for line in self.board:
            if 0 in line:
                return (i, line.index(0))
            i += 1
        return None

    def __key(board):
        l = []
        [l.extend(i) for i in board]
        l = [str(i) for i in l]
        return ''.join(l)
    __key = staticmethod(__key)
    
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

        board = copy.deepcopy(self.board)

        board[empty[0]][empty[1]] = self.board[dest[0]][dest[1]]
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
                s = self.move_empty(move)
                successors.append(s)
            except ValueError:
                pass
        return successors


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
        state_moved = state.move_empty("up")
        state_final = State(final)
        self.failUnlessEqual(state_moved, state_final)

    def testillegalmove(self):
        board = [
            [1, 2, 3],
            [4, 5, 6],
            [7, 8, 0]
        ]
        state = State(board)
        self.failUnlessRaises(ValueError, state.move_empty, "down")
    
    def testunknownmove(self):
        board = [
            [1, 2, 3],
            [4, 5, 6],
            [7, 8, 0]
        ]
        state = State(board)
        self.failUnlessRaises(ValueError, state.move_empty, "aaa")

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

        generated.sort()
        successors.sort()

        self.failUnlessEqual(successors, generated)

if __name__ == '__main__':
    unittest.main()

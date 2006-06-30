#!/usr/bin/env python

import unittest
import copy
import memoize

import sets

class State(object):
    __metaclass__ = memoize.Memoized

    def __init__(self, size, coords=()):
        self.coords = list(coords)
        self.size = size

        self.rows    = [x   for x, y in coords]
        self.cols    = [y   for x, y in coords]
        self.diags_a = [x-y for x, y in coords]
        self.diags_b = [x+y for x, y in coords]

        if not self._check():
            raise ValueError

    def _check(self):
        def _check_uniq(list):
            list = list[:]
            while list:
                i = list.pop()
                if i in list:
                    return False
            return True

        if not _check_uniq(self.rows): return False
        if not _check_uniq(self.cols): return False
        if not _check_uniq(self.diags_a): return False
        if not _check_uniq(self.diags_b): return False

        return True

    def __hash__(self):
        coords = self.coords[:]
        coords.sort()
        return hash(str(self.size) + str(coords))

    def is_goal(self):
        empty_rows = [i for i in range(self.size) if i not in self.rows]
        return not empty_rows

    def generate(self):
        successors = []

        empty_rows = [i for i in range(self.size) if i not in self.rows]
        empty_cols = [i for i in range(self.size) if i not in self.cols]

        for i in empty_rows:
            for j in empty_cols:
                try:
                    coords = self.coords[:]
                    coords.append( (i, j) )
                    s = self.__class__(self.size, coords)
                    successors.append(s)
                except ValueError:
                    pass
        return successors

    def heuristics(self):
        tot = 0
        for i in xrange(self.size):
            for j in xrange(self.size):
                val = 0
                if i in self.rows:
                    val += 0.25
                if j in self.cols:
                    val += 0.25
                if i-j in self.diags_a:
                    val += 0.25
                if i+j in self.diags_b:
                    val += 0.25
                tot += val
        tot -= self.size * len(self.coords)
        return tot

    def __str__(self):
        string = []
        for i in range(self.size):
            for j in range(self.size):
                if (i, j) in self.coords:
                    string.append('o')
                else:
                    string.append(' ')
            string.append('\n')
        return ''.join(string)

class TestState(unittest.TestCase):
    def testgoal(self):
        queens = (
            (0,1),
            (1,3),
            (2,0),
            (3,2)
        )
        state = State(4, queens)
        self.failUnless(state.is_goal())

    def testgoalgenerate(self):
        queens = (
            (0,1),
            (1,3),
            (2,0),
            (3,2)
        )
        state = State(4, queens)
        self.failUnless(not state.generate())

    def testillegal(self):
        queens = (
            (0,1),
            (1,3),
            (2,0),
            (3,3)
        )
        self.failUnlessRaises(ValueError, State, 4, queens)

    def testgenerate(self):
        queens = (
            (0,1),
            (1,3),
            (2,0)
        )
        state = State(4, queens)
        successors = state.generate()
        self.failUnless(len(successors), 1)
        self.failUnless(successors[0].is_goal())


if __name__ == '__main__':
    unittest.main()

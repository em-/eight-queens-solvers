#!/usr/bin/env python

import unittest
import copy
import memoize


class State(object):
    __metaclass__ = memoize.Memoized

    def __init__(self, size, coords=None):
        self.rows = {}
        self.size = size
        if not coords:
            coords = ()
        if not self._check_valid(coords):
            raise ValueError
        for i,j in coords:
            self.rows[i] = j

    def __hash__(self):
        return hash(self.size) + hash(str(self.rows))

    def _check_valid(self, coords):
        rows = [i for i,j in coords]
        rows.sort()
        if not self._check_unique(rows):
            return False

        cols = [j for i,j in coords]
        cols.sort()
        if not self._check_unique(cols):
            return False

        diags_a = [i-j for i,j in coords]
        diags_a.sort()
        if not self._check_unique(diags_a):
            return False

        diags_b = [i+j for i,j in coords]
        diags_b.sort()
        if not self._check_unique(diags_b):
            return False

        return True

    def _check_unique(self, list):
        for i in list:
            if list.count(i) != 1:
                return False
        return True

    def _get_empty_rows(self):
        occupied = self.rows.keys()
        empty = []
        for i in range(self.size):
            if i not in occupied:
                empty.append(i)
        return empty

    def is_goal(self):
        return not self._get_empty_rows()

    def generate(self):
        successors = []
        coords = self.rows.items()
        empty_rows = self._get_empty_rows()
        for i in empty_rows:
            for j in range(self.size):
                coords.append((i,j))
                try:
                    s = State(self.size, coords)
                    successors.append(s)
                except ValueError:
                    pass
                coords.pop()
        return successors

    def heuristics(self):
        coords = self.rows.items()
        rows = [i for i,j in coords]
        cols = [j for i,j in coords]
        diags_a = [i-j for i,j in coords]
        diags_b = [i+j for i,j in coords]

        free = 0
        for i in xrange(self.size):
            for j in xrange(self.size):
                if i not in rows:
                    free += 1
                if j not in cols:
                    free += 1
                if i-j not in diags_a:
                    free += 1
                if i+j not in diags_b:
                    free += 1

        return ((self.size**2)*4 - free) - 4 * self.size * len(self.rows)

    def __str__(self):
        string = []
        for i in range(self.size):
            for j in range(self.size):
                if self.rows.get(i) == j:
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

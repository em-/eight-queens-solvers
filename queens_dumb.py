#!/usr/bin/env python

import queens

class State(queens.State):
    def heuristics(self):
        coords = self.rows.items()
        rows = [i for i,j in coords]
        cols = [j for i,j in coords]
        diags_a = [i-j for i,j in coords]
        diags_b = [i+j for i,j in coords]

        free = 0
        for i in xrange(self.size):
            for j in xrange(self.size):
                if i not in rows and j not in cols:
                    if i-j not in diags_a and i+j not in diags_b:
                        free += 1

        return free


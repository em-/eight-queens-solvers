#!/usr/bin/env python

import queens

class State(queens.State):
    def heuristics(self):
        free = 0
        for i in xrange(self.size):
            for j in xrange(self.size):
                if i not in self.rows and j not in self.cols:
                    if i-j not in self.diags_a and i+j not in self.diags_b:
                        free += 1

        return free


#!/usr/bin/env python

import slot

class State(slot.State):
    def heuristics(self):
        h = i = 0
        while i < len(self.board):
            j = 0
            while j < len(self.board[i]):
                if self.board[i][j] != self.goal[i][j]:
                    h += 1
                j += 1
            i += 1
        return h


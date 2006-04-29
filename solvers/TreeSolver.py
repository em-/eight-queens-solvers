#!/usr/bin/env python

from solvers import Solver

class TreeSolver(Solver):
    def __init__(self):
        self.tree = {}

    def set_parent(self, child, parent):
        self.tree[child] = parent

    def get_track(self, goal):
        track = [goal]
        node = goal
        while self.tree.has_key(node):
            node = self.tree[node]
            track.append(node)
        return track

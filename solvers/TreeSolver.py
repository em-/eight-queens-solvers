#!/usr/bin/env python

from solvers import Solver
import graph

class TreeSolver(Solver):
    def __init__(self):
        self.tree = graph.DiGraph()

    def set_parent(self, child, parent):
        self.tree.add_node(parent)
        self.tree.add_node(child)
        self.tree.add_edge(child, parent)

    def get_track(self, goal):
        track = [goal]
        while True:
            tail = track[-1]
            edges = self.tree.edges(tail)
            if not edges:
                return track
            track.append(edges[0][1])


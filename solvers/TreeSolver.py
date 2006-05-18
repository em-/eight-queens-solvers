#!/usr/bin/env python

from solvers import Solver
import graph

class TreeSolver(Solver):
    def __init__(self):
        self.tree = graph.Graph()

    def set_parent(self, child, parent):
        try: 
            self.tree.add_node(parent)
            self.tree.add_node(child)
        except ValueError:
            pass
        self.tree.add_edge(child, parent)


    def get_track(self, goal):
        track = [goal]
        while True:
            parents = [e.end for e in self.tree.edges if e.start == track[-1]]
            if not parents: 
                return track
            track.append(parents[0])

#!/usr/bin/python2.3

from solvers import BreadthSolver, DepthSolver, HillClimbingSolver, PruningBreadthSolver, AStarSolver
import slot
import queens

import timing


class Statistics:
    def __init__(self):
        self.algorithm = None
        self.time = None
        self.solution = None
        self.analyzed_nodes = None
        self.inmemory_nodes = None

    def run(self, function):
        timing.start()
        self.solution = function()
        timing.finish()
        self.time = timing.milli()

    def print_stat(self):
        print "Algorithm: %s" % self.algorithm
        print "Time: %s ms" % (self.time/1000.0)
        if self.solution:
            print "Solution found"
        else:
            print "Solution not found"
        print "Nodes analyzed: %s" % self.analyzed_nodes
        print "Nodes in memory: %s" % self.inmemory_nodes
        print

    def breadth(self, initial_state):
        self.algorithm = "Breadth First"
        solver = BreadthSolver(initial_state)
        self.run(solver.solve)
        self.analyzed_nodes = len(solver.CLOSED)
        self.inmemory_nodes = len(solver.CLOSED) + len(solver.OPEN)

    def depth(self, initial_state):
        self.algorithm = "Depth First"
        solver = DepthSolver(initial_state)
        self.run(solver.solve)
        self.analyzed_nodes = len(solver.CLOSED)
        self.inmemory_nodes = len(solver.CLOSED) + len(solver.OPEN)

    def hillclimbing(self, initial_state):
        self.algorithm = "Hill Climbing"
        solver = HillClimbingSolver(initial_state)
        self.run(solver.solve)
        self.analyzed_nodes = len(solver.CLOSED)
        self.inmemory_nodes = len(solver.CLOSED) + len(solver.OPEN)

    def astar(self, initial_state):
        self.algorithm = "A*"
        solver = AStarSolver(initial_state)
        self.run(solver.solve)
        self.analyzed_nodes = len(solver.CLOSED)
        self.inmemory_nodes = len(solver.CLOSED) + len(solver.OPEN)

    def pruningbreadth(self, initial_state, beta):
        self.algorithm = "Pruning Breadth First (beta = %d)" % beta
        solver = PruningBreadthSolver(initial_state, beta)
        self.run(solver.solve)
        self.analyzed_nodes = len(solver.CLOSED)
        self.inmemory_nodes = len(solver.CLOSED) + len(solver.OPEN)


class Queens(Statistics):
    def start(self):
        initial_state = queens.State(6)
        self.breadth (initial_state)
        self.print_stat()
        self.depth (initial_state)
        self.print_stat()
        self.hillclimbing (initial_state)
        self.print_stat()
        self.astar (initial_state)
        self.print_stat()
        self.pruningbreadth (initial_state, 40)
        self.print_stat()

class Slot(Statistics):
    def start(self):
        board = [
            [5, 6, 1],
            [2, 7, 0],
            [4, 8, 3]
        ]
        initial_state = slot.State(board)
        self.breadth (initial_state)
        self.print_stat()
        self.depth (initial_state)
        self.print_stat()
        self.hillclimbing (initial_state)
        self.print_stat()
        self.astar (initial_state)
        self.print_stat()
        self.pruningbreadth (initial_state, 3)
        self.print_stat()

def main():
    print 'Slot'
    print
    a = Slot()
    a.start()
    print '---------'
    print 'Queens'
    print
    b = Queens()
    b.start()

if __name__ == '__main__':
    for i in range(2):
        main()
        print '=========='

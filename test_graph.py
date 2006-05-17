#!/usr/bin/python
from graph import Graph
import unittest

class TestGraph(unittest.TestCase):
    def test_node(self):
        g = Graph()
        node = 'a'
        g.add_node(node)

        self.failUnlessEqual(len(g.nodes), 1)
        self.failUnlessEqual(g.nodes[0], node)

if __name__ == '__main__':
    unittest.main()

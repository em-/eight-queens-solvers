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

    def test_edge(self):
        g = Graph()
        a = 'a'
        b = 'b'
        g.add_node(a)
        g.add_node(b)

        g.add_edge(a,b)

        outgoing = list(g.outgoing(a))
        incoming = list(g.incoming(b))

        self.failUnlessEqual(len(outgoing), 1)
        self.failUnlessEqual(outgoing, incoming)
        self.failUnlessEqual(outgoing[0].start, a)
        self.failUnlessEqual(outgoing[0].end,   b)

if __name__ == '__main__':
    unittest.main()

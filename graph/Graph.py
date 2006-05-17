#!/usr/bin/python

class Edge(object):
    __slots__ = ['start','end','label']

    def __init__(self, start, end, label=None):
        self.start = start
        self.end   = end
        self.label = label


class Graph(object):
    def __init__(self):
        self.nodes=[]
        self.edges=[]

    def add_node(self, node):
        if node in self.nodes:
            raise ValueError('duplicate node "%s"', node)
        self.nodes.append(node)

    def delete_node(self, node):
        for i, edge in enumerate(self.edges):
            if edge.start == node or edge.end == node:
                del self.edges[i]

        index = self.nodes.index(node)
        del self.nodes[index]

    def delete_edge(self, edge):
        i = self.edges.index(edge)
        del self.edges[i]

    def add_edge(self, start, end, label=None):
        e = Edge(start, end, label)
        self.edges.append(e)
        return e

    def outgoing(self, node):
        for edge in self.edges:
            if edge.start == node:
                yield edge

    def incoming(self, node):
        for edge in self.edges:
            if edge.end == node:
                yield edge


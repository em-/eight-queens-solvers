#!/usr/bin/env python

import unittest
import weakref

class Memoized(type):
    # this is the MultiSingleton metaclass 
    # with a WeakValueDictionary instead of a simple dict
    def __call__(cls, *args, **kwds):
        cache = cls.__dict__.get('__cache__')
        if cache is None:
            cls.__cache__ = cache = weakref.WeakValueDictionary()
        
        obj = object.__new__(cls)
        obj.__init__(*args, **kwds)

        tag = hash(obj)
        if tag in cache:
            return cache[tag]

        cache[tag] = obj
        return obj


class TestMemoized(unittest.TestCase):
    def test_noargs(self):
        class Test:
            __metaclass__ = Memoized

            def __hash__(self):
                return hash(Test)

        a = Test()
        b = Test()

        self.failUnlessEqual(a,b)

    def test_args_equal(self):
        class Test:
            __metaclass__ = Memoized

            def __init__(self, value):
                self.value = value

            def __hash__(self):
                return hash(self.value)

        a = Test('a')
        b = Test('a')

        self.failUnlessEqual(a,b)

    def test_args_differ(self):
        class Test:
            __metaclass__ = Memoized

            def __init__(self, value):
                self.value = value

            def __hash__(self):
                return hash(self.value)

        a = Test('a')
        b = Test('b')

        self.failIfEqual(a,b)

    def test_singleton(self):
        class Test:
            __metaclass__ = Memoized

            def __init__(self, value):
                self.value = value

            def __hash__(self):
                return hash(Test)

        a = Test('a')
        b = Test('b')

        self.failUnlessEqual(a,b)

if __name__ == '__main__':
    unittest.main()

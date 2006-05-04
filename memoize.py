#!/usr/bin/env python

import unittest
import weakref

def Memoized(keyfunc=None):
    if not keyfunc:
        keyfunc = lambda *args, **kwds: str(args) + str(kwds)

    class MemoizedMeta(type):
        # this is the MultiSingleton metaclass 
        # with a WeakValueDictionary instead of a simple dict
        def __call__(cls, *args, **kwds):
            cache = cls.__dict__.get('__cache__')
            if cache is None:
                cls.__cache__ = cache = weakref.WeakValueDictionary()
            tag = keyfunc(*args, **kwds)
            if tag in cache:
                return cache[tag]
            obj = object.__new__(cls)
            obj.__init__(*args, **kwds)
            cache[tag] = obj
            return obj
    return MemoizedMeta
     


class TestMemoized(unittest.TestCase):
    def test_noargs(self):
        class Test:
            __metaclass__ = Memoized()
            pass

        a = Test()
        b = Test()

        self.failUnlessEqual(a,b)

    def test_args_equal(self):
        class Test:
            __metaclass__ = Memoized()
            pass

        a = Test('a')
        b = Test('a')

        self.failUnlessEqual(a,b)

    def test_args_differ(self):
        class Test:
            __metaclass__ = Memoized()
            pass

        a = Test('a')
        b = Test('b')

        self.failIfEqual(a,b)

    def test_singleton(self):
        class Test:
            __metaclass__ = Memoized(lambda arg: 'a')
            pass

        a = Test('a')
        b = Test('b')

        self.failUnlessEqual(a,b)

if __name__ == '__main__':
    unittest.main()

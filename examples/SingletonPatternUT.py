#!/usr/bin/env python3

# pylint: disable = bad-whitespace
# pylint: disable = invalid-name
# pylint: disable = missing-docstring
# pylint: disable = no-self-use
# pylint: disable = too-few-public-methods

# -------------------
# SingletonPattern.py
# -------------------

from unittest import main, TestCase

class A :
    pass

def singleton_function (c) :
    x = c()
    return lambda : x

@singleton_function
class B :
    pass

class singleton_class :
    def __init__ (self, c) :
        self.x = c()

    def __call__ (self) :
        return self.x

@singleton_class
class C :
    pass

class MyUnitTests (TestCase) :
    def test_1 (self) :
        x = A()
        y = A()
        assert x != y

    def test_2 (self) :
        x = B()
        y = B()
        assert x == y

    def test_3 (self) :
        x = C()
        y = C()
        assert x == y

if __name__ == "__main__" : # pragma: no cover
    main()

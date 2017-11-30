#!/usr/bin/env python3

# pylint: disable = bad-whitespace
# pylint: disable = invalid-name
# pylint: disable = missing-docstring
# pylint: disable = too-few-public-methods

# -------------------
# SingletonPattern.py
# -------------------

class A :
    pass

def test1 () -> None :
    x = A()
    y = A()
    assert x != y

def singleton (c) :
    x = c()
    return lambda : x

@singleton
class B :
    pass

def test2 () -> None :
    x = B()
    y = B()
    assert x == y

if __name__ == "__main__" : # pragma: no cover
    print("SingletonPattern.py")
    test1()
    test2()
    print("Done.")

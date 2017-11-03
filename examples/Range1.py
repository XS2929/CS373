#!/usr/bin/env python3

# pylint: disable = bad-whitespace
# pylint: disable = invalid-name
# pylint: disable = missing-docstring

# ---------
# Range1.py
# ---------

# https://docs.python.org/3/library/functions.html#func-range

def test () -> None :
    x = range(2, 2)
    p = iter(x)
    assert x is not p
    assert p is iter(p)
    try :
        next(p)
    except StopIteration :
        pass

    x = range(2, 3)
    p = iter(x)
    assert x is not p
    assert p is iter(p)
    assert next(p) == 2
    try :
        next(p)
    except StopIteration :
        pass

    x = range(2, 4)
    p = iter(x)
    assert x is not p
    assert p is iter(p)
    assert next(p) == 2
    assert next(p) == 3
    try :
        next(p)
    except StopIteration :
        pass

    x = range(2, 5)
    assert list(x) == [2, 3, 4]
    assert list(x) == [2, 3, 4]

if __name__ == "__main__" : # pragma: no cover
    print("Range1.py")
    test()
    print("Done.")

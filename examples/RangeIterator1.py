#!/usr/bin/env python3

# pylint: disable = bad-whitespace
# pylint: disable = invalid-name
# pylint: disable = missing-docstring

# -----------------
# RangeIterator1.py
# -----------------

from typing import Iterator

def range_iterator (b: int, e: int) -> Iterator[int] :
    while b != e :
        yield b
        b += 1

def test () -> None :
    p = range_iterator(2, 2)
    assert p is iter(p)
    try :
        next(p)
    except StopIteration :
        pass

    p = range_iterator(2, 3)
    assert p is iter(p)
    assert next(p) == 2
    try :
        next(p)
    except StopIteration :
        pass

    p = range_iterator(2, 4)
    assert p is iter(p)
    assert next(p) == 2
    assert next(p) == 3
    try :
        next(p)
    except StopIteration :
        pass

    p = range_iterator(2, 5)
    assert list(p) == [2, 3, 4]
    assert list(p) == []

if __name__ == "__main__" : # pragma: no cover
    print("RangeIterator1.py")
    test()
    print("Done.")

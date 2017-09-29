#!/usr/bin/env python3

# pylint: disable = bad-whitespace
# pylint: disable = invalid-name
# pylint: disable = missing-docstring

# -----------
# IsPrime1.py
# -----------

from math import sqrt

def is_prime (n: int) -> bool :
    assert n > 0
    if (n == 1) or ((n % 2) == 0) :
        return False
    for i in range(3, int(sqrt(n))) :
        if (n % i) == 0 :
            return False
    return True

def test (f) :
    print("IsPrime1.py")

    assert not f(1)
    assert not f(2)
    assert     f(3)
    assert not f(4)
    assert     f(5)
    assert     f(7)
    assert     f(9)
    assert not f(27)
    assert     f(29)

    print("Done.")

if __name__ == "__main__" : # pragma: no cover
    test(is_prime)

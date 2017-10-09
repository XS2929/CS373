#!/usr/bin/env python3

# pylint: disable = bad-whitespace
# pylint: disable = invalid-name
# pylint: disable = missing-docstring

# ------------
# Factorial1.py
# ------------

# https://docs.python.org/3.4/library/math.html

from math import factorial

def test () -> None :
    assert factorial(0) == 1
    assert factorial(1) == 1
    assert factorial(2) == 2
    assert factorial(3) == 6
    assert factorial(4) == 24
    assert factorial(5) == 120

if __name__ == "__main__" : # pragma: no cover
    print("Factorial1.py")
    test()
    print("Done.")

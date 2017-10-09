#!/usr/bin/env python3

# pylint: disable = bad-whitespace
# pylint: disable = consider-using-enumerate
# pylint: disable = invalid-name
# pylint: disable = missing-docstring

# ----------
# Reduce1.py
# ----------

from functools import reduce
from operator  import add, concat, mul

def test () :
    assert reduce(add,    [2, 3, 4],  0)   == 9
    assert reduce(mul,    [2, 3, 4],  1)   == 24
    assert reduce(concat, ["b", "c"], "a") == "abc"
    assert reduce(None,   [],         2)   == 2

if __name__ == "__main__" : # pragma: no cover
    print("Reduce1.py")
    test()
    print("Done.")

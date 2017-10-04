#!/usr/bin/env python3

# pylint: disable = bad-whitespace
# pylint: disable = invalid-name
# pylint: disable = missing-docstring

# ------------
# Factorial1.py
# ------------

# https://docs.python.org/3.4/library/math.html

from functools import reduce
from math      import factorial
from operator  import mul
from typing    import Callable, TypeVar

T = TypeVar("T")

# recursive procedure
# linear recursive process
def factorial_recursion (n: int) -> int :
    assert n >= 0
    if n < 2 :
        return 1
    return n * factorial_recursion(n - 1)

# recursive procedure
# linear iterative process
def factorial_tail_recursion (n: int) -> int :
    assert n >= 0
    def f (n, v) :
        assert n >= 0
        assert v >= 1
        if n < 2 :
            return v
        return f(n - 1 , n * v)
    return f(n, 1)

# iterative procedure
# linear iterative process
def factorial_while (n: int) -> int :
    assert n >= 0
    v = 1
    while n > 1 :
        v *= n
        n -= 1
    return v

# iterative procedure
# linear iterative process
def factorial_range_for (n: int) -> int :
    assert n >= 0
    v = 1
    for i in range(1, n + 1) :
        v *= i
    return v

# iterative procedure
# linear iterative process
def factorial_range_iterator (n: int) -> int :
    assert n >= 0
    v = 1
    p = iter(range(1, n + 1))
    try :
        while True :
            i  = next(p)
            v *= i
    except StopIteration :
        pass
    return v

# iterative procedure
# linear iterative process
def factorial_range_reduce (n: int) -> int :
    assert n >= 0
    return reduce(mul, range(1, n + 1), 1)

def test (f: Callable[[int], int]) -> None :
    assert f(0) == 1
    assert f(1) == 1
    assert f(2) == 2
    assert f(3) == 6
    assert f(4) == 24
    assert f(5) == 120

if __name__ == "__main__" : # pragma: no cover
    print("Factorial1.py")

    test(factorial_recursion)
    test(factorial_tail_recursion)
    test(factorial_while)
    test(factorial_range_for)
    test(factorial_range_iterator)
    test(factorial_range_reduce)
    test(factorial)

    print("Done.")

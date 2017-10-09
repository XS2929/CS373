#!/usr/bin/env python3

# pylint: disable = bad-whitespace
# pylint: disable = consider-using-enumerate
# pylint: disable = invalid-name
# pylint: disable = missing-docstring
# pylint: disable = pointless-string-statement
# pylint: disable = too-few-public-methods

# -------
# Map2.py
# -------

# https://docs.python.org/3/library/functions.html#map

from timeit   import timeit
from unittest import main, TestCase
from typing   import Callable, Iterable, Iterator, Sequence, TypeVar

T = TypeVar("T")

class map_iterator (Iterator[T]) :
    def __init__ (self, uf: Callable[[T], T], a: Iterable[T]) -> None :
        self.uf = uf
        self.p  = iter(a)

    def __iter__ (self) -> Iterator[T] :
        return self

    def __next__ (self) -> T :
        return self.uf(next(self.p))

def map_for_range (uf: Callable[[T], T], a: Sequence[T]) -> Iterator[T] :
    for i in range(len(a)) :
        yield uf(a[i])

def map_for (uf: Callable[[T], T], a: Iterable[T]) -> Iterator[T] :
    for v in a :
        yield uf(v)

def map_generator (uf: Callable[[T], T], a: Iterable[T]) -> Iterator[T] :
    return (uf(v) for v in a)

class MyUnitTests (TestCase) :
    def setUp (self) :
        self.a = [
            map_iterator,
            map_for_range,
            map_for,
            map_generator,
            map]

    def test_1 (self) :
        for f in self.a :
            with self.subTest(msg=f.__name__) :
                m = f(lambda v : v ** 2, (2, 3, 4))
                self.assertEqual(list(m), [4, 9, 16])
                self.assertEqual(list(m), [])

    def test_2 (self) :
        p = 2
        for f in self.a :
            with self.subTest(msg=f.__name__) :
                m = f(lambda v : v ** p, (2, 3, 4))
                self.assertEqual(list(m), [4, 9, 16])
                self.assertEqual(list(m), [])

    def test_3 (self) :
        for f in self.a :
            with self.subTest(msg=f.__name__) :
                print()
                print(f.__name__)
                if f.__name__ == "map" :
                    t = timeit(
                        "list(" + f.__name__ + "(lambda v : v ** 2, 10000 * [5]))",
                        "",
                        number = 100)
                else :
                    t = timeit(
                        "list(" + f.__name__ + "(lambda v : v ** 2, 10000 * [5]))",
                        "from __main__ import " + f.__name__,
                        number = 100)
                print("{:.2f} milliseconds".format(t * 1000))

if __name__ == "__main__" : # pragma: no cover
    main()

""" #pragma: no cover
% MapT
....
map_iterator
645.18 milliseconds

map_for_range
439.34 milliseconds

map_for
401.45 milliseconds

map_generator
395.14 milliseconds

map
320.15 milliseconds
.
----------------------------------------------------------------------
Ran 5 tests in 2.433s

OK
"""

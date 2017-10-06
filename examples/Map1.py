#!/usr/bin/env python3

# pylint: disable = bad-whitespace
# pylint: disable = consider-using-enumerate
# pylint: disable = invalid-name
# pylint: disable = missing-docstring
# pylint: disable = too-few-public-methods

# -------
# Map1.py
# -------

# https://docs.python.org/3/library/functions.html#map

from typing import Callable, Iterable, Sequence, TypeVar

T = TypeVar("T")

class Map_Iterator :
    def __init__ (self, uf: Callable[[T], T], a: Iterable[T]) -> None :
        self.uf = uf
        self.p  = iter(a)

    def __iter__ (self) :
        return self

    def __next__ (self) -> T :
        return self.uf(next(self.p))

def map_for_range (uf: Callable[[T], T], a: Sequence[T]) -> Iterable[T] :
    for i in range(len(a)) :
        yield uf(a[i])

def map_for (uf: Callable[[T], T], a: Iterable[T]) -> Iterable[T] :
    for v in a :
        yield uf(v)

def map_generator (uf: Callable[[T], T], a: Iterable[T]) -> Iterable[T] :
    return (uf(v) for v in a)

def test (f: Callable) -> None :
    g = lambda v : v ** 2
    x = f(g, (2, 3, 4))
    assert list(x) == [4, 9, 16]
    assert list(x) == []

    p = 2
    g = lambda v : v ** p
    x = f(g, (2, 3, 4))
    assert list(x) == [4, 9, 16]
    assert list(x) == []

if __name__ == "__main__" : # pragma: no cover
    test(Map_Iterator)
    test(map_for_range)
    test(map_for)
    test(map_generator)
    test(map)

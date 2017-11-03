#!/usr/bin/env python3

# pylint: disable = bad-whitespace
# pylint: disable = invalid-name
# pylint: disable = missing-docstring
# pylint: disable = too-few-public-methods

# ---------
# Range2.py
# ---------

# https://docs.python.org/3/library/functions.html#func-range

from typing   import Iterable, Iterator
from unittest import main, TestCase

def range_iterator (b: int, e: int) -> Iterator[int] :
    while b != e :
        yield b
        b += 1

class range_1 (Iterable[int]) :
    def __init__ (self, b: int, e: int) -> None :
        self.b = b
        self.e = e

    def __iter__ (self) -> Iterator[int] :
        return range_iterator(self.b, self.e)

class range_2 (Iterable[int]) :
    def __init__ (self, b: int, e: int) -> None :
        self.b = b
        self.e = e

    def __iter__ (self) -> Iterator[int] :
        b = self.b
        while b != self.e :
            yield b
            b += 1

class MyUnitTests (TestCase) :
    def setUp (self) :
        self.a = [
            range_1,
            range_2,
            range]

    def test_1 (self) :
        for f in self.a :
            with self.subTest(msg=f.__name__) :
                x = f(2, 2)
                p = iter(x)
                self.assertIsNot(x, p)
                self.assertIs(p, iter(p))
                self.assertRaises(StopIteration, next, p)

    def test_2 (self) :
        for f in self.a :
            with self.subTest(msg=f.__name__) :
                x = f(2, 3)
                p = iter(x)
                self.assertIsNot(x, p)
                self.assertIs(p, iter(p))
                self.assertEqual(next(p), 2)
                self.assertRaises(StopIteration, next, p)

    def test_3 (self) :
        for f in self.a :
            with self.subTest(msg=f.__name__) :
                x = f(2, 4)
                p = iter(x)
                self.assertIsNot(x, p)
                self.assertIs(p, iter(p))
                self.assertEqual(next(p), 2)
                self.assertEqual(next(p), 3)
                self.assertRaises(StopIteration, next, p)

    def test_4 (self) :
        for f in self.a :
            with self.subTest(msg=f.__name__) :
                x = f(2, 5)
                self.assertEqual(list(x), [2, 3, 4])
                self.assertEqual(list(x), [2, 3, 4])

if __name__ == "__main__" :
    main()

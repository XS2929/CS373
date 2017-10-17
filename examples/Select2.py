#!/usr/bin/env python3

# pylint: disable = bad-whitespace
# pylint: disable = invalid-name
# pylint: disable = missing-docstring

# ----------
# Select2.py
# ----------

# http://en.wikipedia.org/wiki/Selection_(relational_algebra)

from typing   import Callable, Dict, Iterable, Iterator
from unittest import main, TestCase

def select_yield (
        r: Iterable[Dict[str, int]],
        f: Callable[[Dict[str, int]], bool]) \
        -> Iterator[Dict[str, int]]          :
    for d in r :
        if f(d) :
            yield d

def select_generator (
        r: Iterable[Dict[str, int]],
        f: Callable[[Dict[str, int]], bool]) \
        -> Iterator[Dict[str, int]]          :
    return (d for d in r if f(d))

def select_filter (
        r: Iterable[Dict[str, int]],
        f: Callable[[Dict[str, int]], bool]) \
        -> Iterator[Dict[str, int]]          :
    return filter(f, r)

class MyUnitTests (TestCase) :
    def setUp (self) :
        self.a = [
            select_yield,
            select_generator,
            select_filter]

        self.r = [
            {"A" : 1, "B" : 4, "C" : 3},
            {"A" : 2, "B" : 5, "C" : 2},
            {"A" : 3, "B" : 6, "C" : 1}]

    def test_1 (self) :
        for f in self.a :
            with self.subTest(msg=f.__name__) :
                self.assertEqual(
                    list(f(self.r, lambda d : False)),
                    [])

    def test_2 (self) :
        for f in self.a :
            with self.subTest(msg=f.__name__) :
                self.assertEqual(
                    list(f(self.r, lambda d : True)),
                    [{"A" : 1, "B" : 4, "C" : 3},
                     {"A" : 2, "B" : 5, "C" : 2},
                     {"A" : 3, "B" : 6, "C" : 1}])

    def test_3 (self) :
        for f in self.a :
            with self.subTest(msg=f.__name__) :
                self.assertEqual(
                    list(f(self.r, lambda d : d["B"] > 4)),
                    [{'A': 2, 'B': 5, 'C': 2},
                     {'A': 3, 'B': 6, 'C': 1}])

    def test_4 (self) :
        for f in self.a :
            with self.subTest(msg=f.__name__) :
                self.assertEqual(
                    list(f(self.r, lambda d : d["A"] > d["C"])),
                    [{'A': 3, 'B': 6, 'C': 1}])

if __name__ == "__main__" :
    main()

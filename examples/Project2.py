#!/usr/bin/env python3

# pylint: disable = bad-whitespace
# pylint: disable = invalid-name
# pylint: disable = missing-docstring

# -----------
# Project2.py
# -----------

# http://en.wikipedia.org/wiki/Projection_(relational_algebra)

from typing   import Dict, Iterable, Iterator
from unittest import main, TestCase

def project_yield (
        r: Iterable[Dict[str, int]],
        *t: str)                     \
        -> Iterator[Dict[str, int]]  :
    for d in r :
        x = {}
        for a in t :
            if a in d :
                x[a] = d[a]
        yield x

def project_comprehension (
        r: Iterable[Dict[str, int]],
        *t: str)                     \
        -> Iterator[Dict[str, int]]  :
    for d in r :
        yield {a : d[a] for a in t if a in d}

def project_generator (
        r: Iterable[Dict[str, int]],
        *t: str)                     \
        -> Iterator[Dict[str, int]]  :
    return ({a : d[a] for a in t if a in d} for d in r)

class MyUnitTests (TestCase) :
    def setUp (self) :
        self.a = [
            project_yield,
            project_comprehension,
            project_generator]

        self.r = [
            {"A" : 1, "B" : 4, "C" : 3},
            {"A" : 2, "B" : 5, "C" : 2},
            {"A" : 3, "B" : 6, "C" : 1}]

    def test_1 (self) :
        for f in self.a :
            with self.subTest(msg=f.__name__) :
                self.assertEqual(
                    list(f(self.r, "D")),
                    [{}, {}, {}])

    def test_2 (self) :
        for f in self.a :
            with self.subTest(msg=f.__name__) :
                self.assertEqual(
                    list(f(self.r, "B")),
                    [{'B': 4},
                     {'B': 5},
                     {'B': 6}])

    def test_3 (self) :
        for f in self.a :
            with self.subTest(msg=f.__name__) :
                self.assertEqual(
                    list(f(self.r, "A", "C")),
                    [{'A': 1, 'C': 3},
                     {'A': 2, 'C': 2},
                     {'A': 3, 'C': 1}])

if __name__ == "__main__" :
    main()

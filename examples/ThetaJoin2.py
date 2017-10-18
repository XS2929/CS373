#!/usr/bin/env python3

# pylint: disable = bad-whitespace
# pylint: disable = invalid-name
# pylint: disable = missing-docstring

# -------------
# ThetaJoin2.py
# -------------

# http://en.wikipedia.org/wiki/Relational_algebra#.CE.B8-join_and_equijoin

from typing   import Callable, Dict, Iterable, Iterator
from unittest import main, TestCase

def theta_join_yield (
        r: Iterable[Dict[str, int]],
        s: Iterable[Dict[str, int]],
        f: Callable[[Dict[str, int], Dict[str, int]], bool]) \
        -> Iterator[Dict[str, int]]                          :
    for u in r :
        for v in s :
            if f(u, v) :
                yield dict(u, **v)

def theta_join_generator (
        r: Iterable[Dict[str, int]],
        s: Iterable[Dict[str, int]],
        f: Callable[[Dict[str, int], Dict[str, int]], bool]) \
        -> Iterator[Dict[str, int]]                          :
    return (dict(u, **v) for u in r for v in s if f(u, v))

class MyUnitTests (TestCase) :
    def setUp (self) :
        self.a = [
            theta_join_yield,
            theta_join_generator]

        self.r = [
            {"A" : 1, "B" : 4},
            {"A" : 2, "B" : 5},
            {"A" : 3, "B" : 6}]

        self.s = [
            {"C" : 2, "D" : 7},
            {"C" : 3, "D" : 5},
            {"C" : 3, "D" : 6},
            {"C" : 4, "D" : 6}]

    def test_1 (self) :
        for f in self.a :
            with self.subTest() :
                self.assertEqual(
                    list(f(self.r, self.s, lambda u, v : False)),
                    [])

    def test_2 (self) :
        for f in self.a :
            with self.subTest() :
                self.assertEqual(
                    list(f(self.r, self.s, lambda u, v : True)),
                    [{'A': 1, 'B': 4, 'C': 2, 'D': 7},
                     {'A': 1, 'B': 4, 'C': 3, 'D': 5},
                     {'A': 1, 'B': 4, 'C': 3, 'D': 6},
                     {'A': 1, 'B': 4, 'C': 4, 'D': 6},
                     {'A': 2, 'B': 5, 'C': 2, 'D': 7},
                     {'A': 2, 'B': 5, 'C': 3, 'D': 5},
                     {'A': 2, 'B': 5, 'C': 3, 'D': 6},
                     {'A': 2, 'B': 5, 'C': 4, 'D': 6},
                     {'A': 3, 'B': 6, 'C': 2, 'D': 7},
                     {'A': 3, 'B': 6, 'C': 3, 'D': 5},
                     {'A': 3, 'B': 6, 'C': 3, 'D': 6},
                     {'A': 3, 'B': 6, 'C': 4, 'D': 6}])

    def test_3 (self) :
        for f in self.a :
            with self.subTest() :
                self.assertEqual(
                    list(f(self.r, self.s, lambda u, v : u["A"] == v["C"])),
                    [{'A': 2, 'B': 5, 'C': 2, 'D': 7},
                     {'A': 3, 'B': 6, 'C': 3, 'D': 5},
                     {'A': 3, 'B': 6, 'C': 3, 'D': 6}])

if __name__ == "__main__" :
    main()

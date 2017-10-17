#!/usr/bin/env python3

# pylint: disable = bad-whitespace
# pylint: disable = invalid-name
# pylint: disable = missing-docstring

# -----------
# Project1.py
# -----------

# http://en.wikipedia.org/wiki/Projection_(relational_algebra)

def project (r, *t) :
    return ({a : d[a] for a in t if a in d} for d in r)

def test () :
    r = [
        {"A" : 1, "B" : 4, "C" : 3},
        {"A" : 2, "B" : 5, "C" : 2},
        {"A" : 3, "B" : 6, "C" : 1}]

    assert                    \
        list(project(r, "D")) \
        ==                    \
        [{}, {}, {}]

    assert                    \
        list(project(r, "B")) \
        ==                    \
        [{'B': 4},
         {'B': 5},
         {'B': 6}]

    assert                         \
        list(project(r, "A", "C")) \
        ==                         \
        [{'A': 1, 'C': 3},
         {'A': 2, 'C': 2},
         {'A': 3, 'C': 1}]

if __name__ == "__main__" :
    print("Project1.py")
    test()
    print("Done.")

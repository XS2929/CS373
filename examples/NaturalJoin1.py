#!/usr/bin/env python3

# pylint: disable = bad-whitespace
# pylint: disable = invalid-name
# pylint: disable = missing-docstring

# ---------------
# NaturalJoin1.py
# ---------------

# http://en.wikipedia.org/wiki/Relational_algebra#.CE.B8-join_and_equijoin

def natural_join (r, s) :
    def bp (u, v) :
        return all(u[k] == v[k] for k in u if k in v)
    return (dict(u, **v) for u in r for v in s if bp(u, v))

def test1 () :
    r = [
        {"A" : 1, "B" : 4},
        {"A" : 2, "B" : 5},
        {"A" : 3, "B" : 6}]

    s = [
        {"C" : 2, "D" : 7},
        {"C" : 3, "D" : 5},
        {"C" : 3, "D" : 6},
        {"C" : 4, "D" : 6}]

    assert                                 \
        list(natural_join(r, s))           \
        ==                                 \
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
         {'A': 3, 'B': 6, 'C': 4, 'D': 6}]

def test2 () :
    r = [
        {"A" : 1, "B" : 4, "C" : 7},
        {"A" : 2, "B" : 5, "C" : 8},
        {"A" : 3, "B" : 6, "C" : 9}]

    s = [
        {"A" : 4, "B" : 4, "D" : 7},
        {"A" : 5, "B" : 5, "D" : 5},
        {"A" : 6, "B" : 6, "D" : 6},
        {"A" : 7, "B" : 7, "D" : 6}]

    assert                       \
        list(natural_join(r, s)) \
        ==                       \
        []

def test3 () :
    r = [
        {"A" : 1, "B" : 4, "C" : 7},
        {"A" : 2, "B" : 5, "C" : 8},
        {"A" : 3, "B" : 6, "C" : 9}]

    s = [
        {"A" : 2, "B" : 4, "D" : 7},
        {"A" : 3, "B" : 5, "D" : 5},
        {"A" : 3, "B" : 6, "D" : 6},
        {"A" : 4, "B" : 7, "D" : 6}]

    assert                       \
        list(natural_join(r, s)) \
        ==                       \
        [{'A': 3, 'B': 6, 'C': 9, 'D': 6}]

if __name__ == "__main__" :
    print("NaturalJoin1.py")
    test1()
    test2()
    test3()
    print("Done.")

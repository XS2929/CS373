#!/usr/bin/env python3

# pylint: disable = bad-whitespace
# pylint: disable = invalid-name
# pylint: disable = missing-docstring

# -------------
# ThetaJoin1.py
# -------------

# http://en.wikipedia.org/wiki/Relational_algebra#.CE.B8-join_and_equijoin

def theta_join (r, s, bp) :
    return (dict(u, **v) for u in r for v in s if bp(u, v))

def test () :
    r = [
        {"A" : 1, "B" : 4},
        {"A" : 2, "B" : 5},
        {"A" : 3, "B" : 6}]

    s = [
        {"C" : 2, "D" : 7},
        {"C" : 3, "D" : 5},
        {"C" : 3, "D" : 6},
        {"C" : 4, "D" : 6}]

    assert                                          \
        list(theta_join(r, s, lambda u, f : False)) \
        ==                                          \
        []

    assert                                         \
        list(theta_join(r, s, lambda u, f : True)) \
        ==                                         \
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

    assert                                                     \
        list(theta_join(r, s, lambda u, v : u["A"] == v["C"])) \
        ==                                                     \
        [{'A': 2, 'B': 5, 'C': 2, 'D': 7},
         {'A': 3, 'B': 6, 'C': 3, 'D': 5},
         {'A': 3, 'B': 6, 'C': 3, 'D': 6}]

if __name__ == "__main__" :
    print("ThetaJoin1.py")
    test()
    print("Done.")

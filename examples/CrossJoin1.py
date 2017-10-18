#!/usr/bin/env python3

# pylint: disable = bad-whitespace
# pylint: disable = invalid-name
# pylint: disable = missing-docstring

# -------------
# CrossJoin1.py
# -------------

# http://en.wikipedia.org/wiki/Cartesian_product

def cross_join (r, s) :
    return (dict(u, **v) for u in r for v in s)

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

    assert                                 \
        list(cross_join(r, s))             \
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

if __name__ == "__main__" :
    print("CrossJoin1.py")
    test()
    print("Done.")

#!/usr/bin/env python3

# pylint: disable = bad-whitespace
# pylint: disable = invalid-name
# pylint: disable = missing-docstring

# ----------
# Select1.py
# ----------

# http://en.wikipedia.org/wiki/Selection_(relational_algebra)

def select (r, f) :
    return filter(f, r)

def test () :
    r = [
        {"A" : 1, "B" : 4, "C" : 3},
        {"A" : 2, "B" : 5, "C" : 2},
        {"A" : 3, "B" : 6, "C" : 1}]

    assert                                \
        list(select(r, lambda d : False)) \
        ==                                \
        []

    assert                               \
        list(select(r, lambda d : True)) \
        ==                               \
        [{"A" : 1, "B" : 4, "C" : 3},
         {"A" : 2, "B" : 5, "C" : 2},
         {"A" : 3, "B" : 6, "C" : 1}]

    assert                                     \
        list(select(r, lambda d : d["B"] > 4)) \
        ==                                     \
        [{'A': 2, 'B': 5, 'C': 2},
         {'A': 3, 'B': 6, 'C': 1}]

    assert                                          \
        list(select(r, lambda d : d["A"] > d["C"])) \
        ==                                          \
        [{'A': 3, 'B': 6, 'C': 1}]

if __name__ == "__main__" :
    print("Select1.py")
    test()
    print("Done.")

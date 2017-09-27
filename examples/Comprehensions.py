#!/usr/bin/env python3

# pylint: disable = bad-whitespace
# pylint: disable = cell-var-from-loop
# pylint: disable = invalid-name
# pylint: disable = missing-docstring
# pylint: disable = no-name-in-module

# -------------
# Indexables.py
# -------------

from types import GeneratorType

print("Comprehensions.py")

x = [2, 3, 4]
y = []
for v in x :
    y += [v * 5]
assert x == [ 2,  3,  4]
assert y == [10, 15, 20]

x = [2, 3, 4]
y = [v * 5 for v in x]            # list comprehension
assert isinstance(y, list)
assert not hasattr(y, "__next__")
assert     hasattr(y, "__iter__")
assert x == [2,   3,  4]
assert y == [10, 15, 20]

x = [2, 3, 4]
g = (v * 5 for v in x)              # generator
assert isinstance(g, GeneratorType)
assert hasattr(g, "__next__")
assert hasattr(g, "__iter__")
assert x       == [2,   3,  4]
assert list(g) == [10, 15, 20]
assert list(g) == []

x = [2, 3, 4]
m = map(lambda v : v * 5, x)
assert hasattr(m, "__next__")
assert hasattr(m, "__iter__")
assert x       == [2,   3,  4]
assert list(m) == [10, 15, 20]
assert list(m) == []

x = [2, 3, 4]
g = (v * 5 for v in x)
x += [5]
assert x       == [ 2,  3,  4,  5]
assert list(g) == [10, 15, 20, 25]
assert list(g) == []
x += [5]
assert list(g) == []

x = [2, 3, 4]
m = map(lambda v : v * 5, x)
x += [5]
assert x       == [2,   3,  4,  5]
assert list(m) == [10, 15, 20, 25]
assert list(m) == []
x += [5]
assert list(m) == []

x = [2, 3, 4, 5, 6]
y = []
for v in x :
    if v % 2 :
        y += [v * 5]
assert x == [2,  3,  4,  5,  6]
assert y == [   15,     25]

x = [2, 3, 4, 5, 6]
y = [v * 5 for v in x if v % 2]
assert x == [ 2,  3,  4,  5,  6]
assert y == [    15,     25]

x = [2, 3, 4, 5, 6]
g = (v * 5 for v in x if v % 2)
assert x       == [ 2,  3,  4,  5,  6]
assert list(g) == [    15,     25]
assert list(g) == []

x = [2, 3, 4, 5, 6]
f = filter(lambda v : v % 2, x)
assert hasattr(f, "__next__")
assert hasattr(f, "__iter__")
m = map(lambda v : v * 5, f)
assert x       == [ 2,  3,  4,  5,  6]
assert list(m) == [    15,     25]
assert list(f) == []
assert list(m) == []

x = [2, 3, 4]
y = [4, 5]
z = []
for v in x :
    for w in y :
        z += [v + w]
assert x == [2, 3, 4]
assert y == [4, 5]
assert z == [2+4, 2+5, 3+4, 3+5, 4+4, 4+5]
assert z == [  6,   7,   7,   8,   8,   9]

x = [2, 3, 4]
y = [4, 5]
z = [v + w for v in x for w in y]
assert x == [2, 3, 4]
assert y == [4, 5]
assert z == [2+4, 2+5, 3+4, 3+5, 4+4, 4+5]
assert z == [  6,   7,   7,   8,   8,   9]

x = [2, 3, 4]
y = [4, 5]
g = (v + w for v in x for w in y)
assert x       == [2, 3, 4]
assert y       == [4, 5]
assert list(g) == [2+4, 2+5, 3+4, 3+5, 4+4, 4+5]
assert list(g) == []

s = {2, 3, 4}
t = set()
for v in s :
    t |= {v * 5}
assert s == { 2,  3,  4}
assert t == {10, 15, 20}

s = {2, 3, 4}
t = {v * 5 for v in s}   # set comprehension
assert s == { 2,  3,  4}
assert t == {10, 15, 20}

d = {2: "abc", 3: "def", 4: "ghi"}
e = {}
for k in d :
    e[k + 1] = d[k] + "xyz"
assert d == {2: "abc",    3: "def",    4: "ghi"}
assert e == {3: "abcxyz", 4: "defxyz", 5: "ghixyz"}

d = {2: "abc", 3: "def", 4: "ghi"}
e = {k + 1: d[k] + "xyz" for k in d}                # dict comprehension
assert isinstance(e, dict)
assert not hasattr(e, "__next__")
assert     hasattr(e, "__iter__")
assert d == {2: "abc",    3: "def",    4: "ghi"}
assert e == {3: "abcxyz", 4: "defxyz", 5: "ghixyz"}

a = "Nothing to be done."
b = [c.lower() for c in a]
assert "".join(b) == "nothing to be done."

print("Done.")

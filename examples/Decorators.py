#!/usr/bin/env python3

# pylint: disable = bad-whitespace
# pylint: disable = invalid-name
# pylint: disable = missing-docstring
# pylint: disable = too-few-public-methods

# -------------
# Decorators.py
# -------------

print("Decorators.py")

def f1 (n) :
    return n + 1

assert f1(2) == 3

def debug_function (g) :
    def h (n) :
        print(g.__name__)
        print("input =", n)
        m = g(n)
        print("output =", m)
        return m
    return h

f1 = debug_function(f1)

assert f1(2) == 3 # f1 input = 2 output = 3

@debug_function
def f2 (n) :
    return n + 1

assert f2(2) == 3 # f2 input = 2 output = 3

class debug_class :
    def __init__ (self, g) :
        self.g = g

    def __call__ (self, n) :
        print(self.g.__name__)
        print("input =", n)
        m = self.g(n)
        print("output =", m)
        return m

@debug_class
def f3 (n) :
    return n + 1

assert f3(2) == 3 # f3 input = 2 output = 3

print("Done.")

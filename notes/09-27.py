# -----------
# Wed, 27 Sep
# -----------

"""
factorial()
iteration

reduce()
more iteration
"""

class A :
    def __init__ (self, v)
        self.v = v

x = A(2)    # x = A.__init__(2)
p = iter(x) # p = x.__iter__()

a = ???      # must be iterable
for v in a :
    ...

a = ???         # must be an iterable over iterables of size 2
for u, v in a :
    ...

"""
Questions
    What attribute makes something an iterable?
    What attribute makes something an iterator?
    What attribute makes something indexable?
    Why do containers not support next() directly?
    When iterating over an iterable (not indexing) what must be true to be able to modify the elements of the iterable?
    What's the relationship between a dict and the result of the keys(), values(), and item() methods on the dict?
"""

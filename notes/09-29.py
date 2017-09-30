# -----------
# Fri, 29 Sep
# -----------

"""
more iteration
iterable vs iterator
comprehensions
"""

a = [2, 3, 4]
a[1] = 5      # l-value

a = (2, 3, 4)
a[1] = 5      # not ok; r-value

x = range(...)
x[1] = 5      # not ok; r-value

a = [2, 3, 5]
print(type(a)) # list, iterable, not an iterator

p = iter(a)
print(type(p)) # list iterator, iterator and iterable!

assert(a is p) # false; a is a list; p is a list iterator

q = iter(p)
assert(p is q) # true; iter(p) returns itself

for v in a : # new list iterator
    print(v) # 2 3 4

for v in a : # new list iterator
    print(v) # 2 3 4; does not get exhausted

for v in p : # iter(p) returns p
    print(v) # 2 3 4

for v in p : # old iterator
    print(v) # <nothing>; exhausted

a = <iterable object>
p = iter(a)

# special processing for the first 3 elements
f(next(p))
f(next(p))
f(next(p))

# different processing for the remaining elements
for v in p :
    g(v)

"""
Questions
    What is the l-value / r-value nature of the [] operator for list, range, str, and tuple?
    What makes something iterable?
    What makes something an iterator?
    Are iterators iterable? How?
"""

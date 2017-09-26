# -----------
# Mon, 25 Sep
# -----------

"""
operator functions
is vs ==
list  +=, +
tuple +=, +

Factorial
iteration
"""

"""
i += j
is the same as
i = i + j
for immutables, but not mutables
"""

a = [2, 3, 4]

for v in a :
    print(v) # 2 3 4

i = 0
while (i < len(a)) :
    print(a[i])      # 2 3 4
    i += 1

a = {2, 3, 4}

for v in a :
    print(v) # 2 3 4

# not for set
i = 0
while (i < len(a)) :
    print(a[i])      # 2 3 4
    i += 1

p = iter(a)
print(type(p)) # set iterator

try :
    while True :
        print(next(p)) # 2 3 4
except StopIteration
    pass

"""
definition of iterable is that it responds to
iter() and results in an iterator

definition of iterator is that it responds to
next() until exhausted and then raises a StopIteration exception
"""

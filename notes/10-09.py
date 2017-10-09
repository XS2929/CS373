# -----------
# Mon,  9 Oct
# -----------

"""
Test #1
RangeIterator
Range
parameter passing
"""

"""
Test #1
multiple-choice questions on Canvas
write-code      questions on HackerRank
bring laptop on Wed for practice test on HackerRank
"""

"""
three tokens
    =, *, **
two contexts
    function call
    function definition
six stories
"""

"""
=  in the call: pass by name
=  in the def:  default arguments, don't use mutables

*  in the call: unpacking an iterable, can only happen once
*  in the def:  forcing the rest of the arguments to be by name
*  in the def:  packing a tuple

** in the call: unpacking a dict
** in the def:  packing a dict
"""

def map (f, *a) # many things

print(list(map(lambda v : v ** 2, [2, 3, 4])))
# 4 9 16

print(list(map(lambda x, y : x + y, [2, 3, 4], [5, 6, 7])))
# 7 9 11

def reduce (f, a, s=None) # one way to default
def reduce (f, a, *s)     # better way to default
    if not s :
        # no seed

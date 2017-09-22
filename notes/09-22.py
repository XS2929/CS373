# -----------
# Fri, 22 Sep
# -----------

"""
operators
variables
"""

from operator import gt

sort(..., >)  # not ok
sort(..., gt)

(i + j)     # doesn't make sense
k = (i + j)
(i + j) = k # not ok

i += j
k = (i += j) # not ok in Python; ok in Java, C, C++
(i += j) = k # not ok in Python, Java, C; ok in C++

"""
subscript on list  returns an l-value
subscript on tuple returns an r-value

Java   overloads a little, does not let me extend that
Python overloads more,     does    let me extend that

is in Python is analogous to ==      in Java
== in Python is analagous to .equals in Java

list += takes any iterable on the right
list +  only takes another list

tuple += only takes another tuple
tuple +  only takes another tuple
"""

i = 2
j = 3
i += j
print(i) # 5
print(j) # 3

i = 2
j = 3
i = (i + j)
print(i) # 5
print(j) # 3

"""
Questions
    What's the benefit of function wrappers of operators?
    What's the difference between is vs ==?
    How does List += differ from Tuple +=?
    How does List +  differ from Tuple +?
"""

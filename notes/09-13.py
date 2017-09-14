# -----------
# Wed, 13 Sep
# -----------

"""
exercise
    demonstrate that bad tests can hide bad code

user errors
    exceptions

exceptions
types

Python
    my exceptions have to extend BaseException

Java
    my exceptions have to implemet Throwable
"""

a = [2, 3, 4]
print(type(a)) # list

a = [2]
print(type(a)) # list

a = []
print((type(a)) # list

a = (2, 3, 4)
print((type(a)) # tuple, basically an immutable list

a = (2)
print((type(a)) # int

a = (2,)
print((type(a)) # tuple

a = ()
print((type(a)) # tuple

a = [2, 3, 4]
b = [2, 3, 4]

print(a == b) # True;  in Java: .equals()
print(a is b) # False; in Java: ==

# in Java

class class

class A { # creates an instance of class class
    ...}

class T {
    public static void main (...) {
        x = new A(...); # creates an instance of class A

# in Python

class type :
    ...

class A : # creates an instance of type type
    pass

x = A() # creates an instance of type A

x = {}
print(type(x)) # dict

"""
in terms of mutability
    set       is like list
    frozenset is like tuple

in Java
    TreeSet: red black binary search tree
    usual cost: O(log n)

    HashSet: hash table
    usual cost: O(1)

in Python
    set, dict: hash table

    the hashables are the immutables

    immutables
        tuple
        str
        frozenset

    mutables
        list
        set
        dict

Questions:
    What Java   operator compares identity?
    What Python operator compares identity?
    What Java   operator compares value?
    What Python operator compares value?
    How do you specify a one-arg tuple?
    What does isinstance() do?
    What does issubclass() do?
    What constraints does set have, compared to list?
"""

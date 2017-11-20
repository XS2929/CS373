#!/usr/bin/env python3

#pylint: disable = no-self-use, too-few-public-methods

# -------------
# Reflection.py
# -------------

print("Reflection.py")

class A () :
    def f (self) :
        return "A.f()"

x = A()
assert isinstance(x, A)
assert x.f() == "A.f()"

c1 = type(A())
assert isinstance(c1, type)
assert c1 is type(A())
x = c1()
assert isinstance(x, A)
assert x.f() == "A.f()"

c2 = A().__class__
assert isinstance(c2, type)
assert c2 is A().__class__
assert c1 is c2
x = c2()
assert isinstance(x, A)
assert x.f() == "A.f()"

d = globals()
assert isinstance(d, dict)
c3 = d["A"]
assert isinstance(c3, type)
assert c3 is d["A"]
assert c1 is c3
x = c3()
assert isinstance(x, A)
assert x.f() == "A.f()"

class B () :
    def __init__ (self, v) :
        self.v = v

try :
    x = globals()["B"]()
    assert False
except TypeError as e :
    assert isinstance(e,      TypeError)
    assert isinstance(e.args, tuple)
    assert len(e.args)  is     1
    assert e.args       is not ("__init__() missing 1 required positional argument: 'v'",)
    assert e.args       ==     ("__init__() missing 1 required positional argument: 'v'",)

try :
    x = globals()["C"]
    assert False
except KeyError as e :
    assert isinstance(e,      KeyError)
    assert isinstance(e.args, tuple)
    assert len(e.args)  is     1
    assert e.args       is not ('C',)
    assert e.args       ==     ('C',)

print("Done.")

# -----------
# Fri,  6 Oct
# -----------

"""
yield
map()
iterables
"""

"""
if 'yield' is in the body of a function
then calling the function does NOT run the function
instead a generator is built and returned
"""

def f () :
    print("abc")
    yield 2
    print("def")
    yield 3
    print("ghi")

x = f()        # <nothing>
print(type(x)) # <generator>

print(x is iter(x)) # true

v = next(x) # abc
print(v)    # 2
v = next(x) # def
print(v)    # 3
v = next(x) # ghi; raise a StopIteration exception

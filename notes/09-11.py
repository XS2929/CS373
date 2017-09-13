# -----------
# Mon, 11 Sep
# -----------

"""
Piazza
    weekly blog
    pay attention to my responses

Docker
    autopep8
    cmake
    vim

Collatz
    type annotations
    you're not required to use

unit testing with Python's unittest
coverage
Collatz optimizations

exercise
    demonstrate that bad tests can hide bad code

user errors
    exceptions

IsPrime
    1. identify the bad tests
    2. fix the tests
    3. identify the bad code
    4. fix the code
"""

# using return

def f (...) :
    ...
    if (<something wrong>) :
        return -1
    ...

def g (...) :
    ...
    x = f(...)
    if x == -1 :
        <something wrong>
    ...

...
...g(...)...
...

# using global

h = 0

def f (...) :
    global h
    h = 0
    ...
    if (<something wrong>) :
        h = -1
        return ...
    ...

def g (...) :
    ...
    x = f(...)
    if h == -1 :
        <something wrong>
    ...

...
...g(...)...
...

# using parameter

def f (..., e2) :
    ...
    if (<something wrong>) :
        e2[0] = -1
        return ...
    ...

def g (...) :
    ...
    e = [0]
    x = f(..., e)
    if e[0] == -1 :
        <something wrong>
    ...

...
...g(...)...
...

"""
three avenues of communication
    1. returns
    2. globals
    3. parameters

assertions bad
    because they'll halt the code

returns, globals, parameters bad
    because they can be ignored
"""

# using exceptions

def f (...) :
    ...
    if (<something wrong>) :
        raise E(...)
    ...

def g (...) :
    ...
    try :
        ...
        x = f(...)
        ...
    except (E as e) :
        <something wrong>
    else :                # only for (1), below
        ...
    finally :             # always
    ...

...
...g(...)...
...

"""
1. no exception was raised
2. exception was raised and handled
3. exception was raised and not handled

a raise in an except clause always goes to the next higher try block

except clauses of types in a class hierarchy must list children first

Questions:
    What were the two bugs in IsPrime1?
    What was the inefficiency in IsPrime1?
    In using a parameter for error handling, why was a list passed?
    Could an int have been passed?
    Could a tuple have been passed?
    What's the diffence between code in an else clause and code after the try block?
    What's the diffence between code in a finally clause and code after the try block?
"""

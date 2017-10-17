# -----------
# Mon, 16 Oct
# -----------

"""
relational algebra is an algebra

algebras are set of elements and operations

algebras are closed vs. open

integers are closed on addition, subtraction, multiplication
integers are open   on division

relational algebra
    relations (tables)
    select
    project
    join
        cross
        theta
        natural
    is closed on all operations

a relation is a set of rows
a row is a set of attributes and values

movie
    title
    year
    actors
    director
    genre

"shane" 1953 "alan ladd" "george stevens" western
"star wars" 1977 "harrison ford" "george lucas" western
"""

r = [
    {"title":"shane",
     "year": 1953,
     "actors": "alan ladd",
     "director": "george stevens",
     "genre": "western"}
     ...
     ]

"""
select
    input
        a relation, r
        a unary predicate, up
    output
        a relation (a subset of the rows in r)
"""

s = select(
        r,
        lambda movie : movie["year"] == 1977)

def select (r, up) :
    for x in r :
        if up(x) :
            yield x

def select (r, up) :
    return (x for x in r if up(x))

def select (r, up) :
    return filter(up, r)

"""
project
    input
        a relation, r
        a sequence of attributes, *a
    output
        a relation (a subset of the cols in r)
"""

p = project(
        r,
        "genre",
        "year")

def project (r, *a) :
    for x in r :
        d = {}
        for col in a :          # O(n), a very small n
            if col in x :       # O(1)
                d[col] = x[col]
        yield d

def project (r, *a) :
    for x in r :
        yield {col: x[col] for col in a if col in x}

def project (r, *a) :
    return ({col: x[col] for col in a if col in x} for x in r)

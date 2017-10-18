# -----------
# Wed, 18 Oct
# -----------

"""
join
    cross
    theta
"""

"""
movie table
    "shane", 1953, "george stevens", "western"
    "star wars", 1977, "george lucas", "sci-fi"
"""

"""
director table (ids are primary keys)
    1, "george lucas"
    2, "george stevens"

movie table (director ids are foreign keys)
    "shane", 1953, 2, "western"
    "star wars", 1977, 1, "sci-fi"
"""

"""
some DB engines do foreign key validation
"""

list([...])
list((...))
list({...})

dict(ghi: 4, def: 5, ...)
d = dict([["abc", 2], ("def", 3)], ghi: 4, def: 5, ...)
dict(d, ghi: 4, def: 5, ...)

# -----------
# Fri, 20 Oct
# -----------

"""
join
    natural
"""

"""
select(r, <unary predicate>)
project(r, a...)
cross_join(r, s)
theta_join(r, s, <binary predicate>)
    cross_join
    select
natural_join(r, s)
    theta_join(r, s, <hand-build binary predicate>)
"""

def natural_join (r, s) :
    def match (u, v) :
        for x in u :
            if x in v :
                if u[x] != v[x]
                    return False
        return True
    return theta_join(r, s, match)

def natural_join (r, s) :
    def match (u, v) :
        return all(u[x] == v[x] for x in u if x in v)
    return theta_join(r, s, match)

def natural_join (r, s) :
    return
        theta_join(
            r,
            s,
            lambda u, v : all(u[x] == v[x] for x in u if x in v))

all([1, True, 2.5]) # True
all((1, True, 0.0)) # False

def all (a) :
    for v in a :
        if not v :
            return False
    return True

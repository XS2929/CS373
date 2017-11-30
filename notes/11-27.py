# -----------
# Mon, 27 Nov
# -----------

"""
@foo
bar
"""

class A :
    pass

x = A()

def singleton (c) :
    x = c()
    def f () :
        return x
    return f

"""
think about lru_cache
"""














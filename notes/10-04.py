# -----------
# Wed,  4 Oct
# -----------

"""
finish comprehensions
map()
"""

a = [2, 3, 4]
a += [5]      # inline list concatenation

a = {2, 3, 4}
a |= {2}      # inline set union

x = f(...)    # function? constructor?

class my_map :
    def __init__ (self, uf, a) :
        self.p  = iter(a)
        self.uf = uf

    def __next__ (self) :
        return self.uf(next(self.p))

    def __iter__ (self) :
        return self

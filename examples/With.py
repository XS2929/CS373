#!/usr/bin/env python3

# pylint: disable = bad-whitespace
# pylint: disable = invalid-name
# pylint: disable = missing-docstring
# pylint: disable = too-few-public-methods

# -------
# With.py
# -------

# https://docs.python.org/3/reference/compound_stmts.html#the-with-statement

def test1 () :
    f = open("With.py")
    try :
        assert f.readline() == "#!/usr/bin/env python3\n"
    finally :
        print("closing file")
        f.close()

class my_file :
    def __init__ (self, s) :
        self.s = s
        self.f = None

    def __enter__ (self) :
        self.f = open(self.s)
        return self.f

    def __exit__ (self, *a) :
        print("exiting my_file")
        self.f.close()

def test2 () :
    x = my_file("With.py")
    f = x.__enter__()
    try :
        assert f.readline() == "#!/usr/bin/env python3\n"
    finally :
        x.__exit__()

def test3 () :
    with my_file("With.py") as f :
        assert f.readline() == "#!/usr/bin/env python3\n"

def test4 () :
    with open("With.py") as f :
        assert f.readline() == "#!/usr/bin/env python3\n"

if __name__ == "__main__" : # pragma: no cover
    print("With.py")
    test1()
    test2()
    test3()
    test4()
    print("Done.")

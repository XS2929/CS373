#!/usr/bin/env python3

# pylint: disable = bad-whitespace
# pylint: disable = invalid-name
# pylint: disable = missing-docstring
# pylint: disable = too-few-public-methods

# ---------
# SQLite.py
# ---------

import sqlite3

def test1 () :
    x = sqlite3.connect("example.db")
    assert isinstance(x, sqlite3.Connection)

    try :
        c = x.cursor()
        assert isinstance(c, sqlite3.Cursor)
        assert hasattr(c, "__iter__")
        assert hasattr(c, "__next__")
        p = iter(c)
        assert p is c
        assert list(c) == []

        c.execute(
            """
            create table Student (
                sID    int,
                sName  text,
                GPA    float,
                sizeHS int);
            """)
        assert list(c) == []

        c.execute(
            """
            insert into Student values (123, 'Amy', 3.9, 1000);
            """)
        assert list(c) == []

        c.execute(
            """
            insert into Student values (234, 'Bob', 3.6, 1500);
            """)
        assert list(c) == []

        c.execute("select * from Student where (GPA > 3.7);")
        assert list(c) == [(123, 'Amy', 3.9, 1000)]
        assert list(c) == []

        c.execute("drop table Student;")
        assert list(c) == []

        c.close()

    finally :
        x.commit()
        x.close()

def test2 () :
    with sqlite3.connect("example.db") as x :
        assert isinstance(x, sqlite3.Connection)

        c = x.cursor()
        assert isinstance(c, sqlite3.Cursor)
        assert hasattr(c, "__iter__")
        assert hasattr(c, "__next__")
        p = iter(c)
        assert p is c
        assert list(c) == []

        c.execute(
            """
            create table Student (
                sID    int,
                sName  text,
                GPA    float,
                sizeHS int);
            """)
        assert list(c) == []

        c.execute(
            """
            insert into Student values (123, 'Amy', 3.9, 1000);
            """)
        assert list(c) == []

        c.execute(
            """
            insert into Student values (234, 'Bob', 3.6, 1500);
            """)
        assert list(c) == []

        c.execute("select * from Student where (GPA > 3.7);")
        assert list(c) == [(123, 'Amy', 3.9, 1000)]
        assert list(c) == []

        c.execute("drop table Student;")
        assert list(c) == []

        c.close()

class my_table :
    def __init__ (self, x) :
        self.x = x
        self.c = None

    def __enter__ (self) :
        print("entering my_table")
        self.c = self.x.cursor()
        assert isinstance(self.c, sqlite3.Cursor)
        assert hasattr(self.c, "__iter__")
        assert hasattr(self.c, "__next__")
        p = iter(self.c)
        assert p is self.c
        assert list(self.c) == []

        self.c.execute(
            """
            create table Student (
                sID    int,
                sName  text,
                GPA    float,
                sizeHS int);
            """)
        assert list(self.c) == []
        return self.c

    def __exit__ (self, *a) :
        print("exiting my_table")
        self.c.execute("drop table Student;")
        assert list(self.c) == []

def test3 () :
    with sqlite3.connect("example.db") as x :
        assert isinstance(x, sqlite3.Connection)

        with my_table(x) as c :
            c.execute(
                """
                insert into Student values (123, 'Amy', 3.9, 1000);
                """)
            assert list(c) == []

            c.execute(
                """
                insert into Student values (234, 'Bob', 3.6, 1500);
                """)
            assert list(c) == []

            c.execute("select * from Student where (GPA > 3.7);")
            assert list(c) == [(123, 'Amy', 3.9, 1000)]
            assert list(c) == []

if __name__ == "__main__" : # pragma: no cover
    print("SQLite.py")
    test1()
    test2()
    test3()
    print("Done.")
